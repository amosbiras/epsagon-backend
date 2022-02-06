from typing import NoReturn, Dict, List
from datetime import datetime

from fastapi import APIRouter, status, Depends

from src.db import AsyncMySQLClient
from src.models import RequestsMetric
from src.api.cache import async_mysql_client, queries
from src.api.routers.constants import RequestsMetricsAPI
from src.utils.decorators import exception_decorator
from src.exceptions import NoDataException
from configuration import Queries

requests_metrics_router = APIRouter(tags=['requests-metrics'])


@requests_metrics_router.post(RequestsMetricsAPI.POST_REQUEST_METRIC, status_code=status.HTTP_201_CREATED)
@exception_decorator
async def collect_requests_metric(requests_metric: RequestsMetric,
                                  async_mysql: AsyncMySQLClient = Depends(async_mysql_client),
                                  queries: Queries = Depends(queries)) -> NoReturn:
    await async_mysql.execute_query(queries.insert_request_metric, **requests_metric.dict())


@requests_metrics_router.get(RequestsMetricsAPI.GET_REQUEST_BY_ID, status_code=status.HTTP_200_OK,
                             response_model=RequestsMetric)
@exception_decorator
async def get_request_by_id(request_id: str, async_mysql: AsyncMySQLClient = Depends(async_mysql_client),
                            queries: Queries = Depends(queries)) -> RequestsMetric:
    try:
        request_metric = next(await async_mysql.execute_query(queries.select_request_by_id, id=request_id))
        return RequestsMetric(**request_metric)
    except StopIteration as e:
        raise NoDataException(status_code=status.HTTP_404_NOT_FOUND,
                              message=f"There is no request metric whose id is '{request_id}'.") from e


@requests_metrics_router.get(RequestsMetricsAPI.GET_REQUESTS_IN_TIMEFRAME, status_code=status.HTTP_200_OK,
                             response_model=List[RequestsMetric])
@exception_decorator
async def get_requests_in_timeframe(start_time: datetime, end_time: datetime, offset: int = 0, limit: int = 10,
                                    async_mysql: AsyncMySQLClient = Depends(async_mysql_client),
                                    queries: Queries = Depends(queries)) -> List[RequestsMetric]:
    data = await async_mysql.execute_query(queries.select_request_in_timeframe, size=limit, offset=offset, limit=limit,
                                           start_time=start_time, end_time=end_time)
    return [RequestsMetric(**request_metric) for request_metric in data]


@requests_metrics_router.get(RequestsMetricsAPI.GET_MOST_VISITED_WEBSITE, status_code=status.HTTP_200_OK)
@exception_decorator
async def get_most_visited_website(async_mysql: AsyncMySQLClient = Depends(async_mysql_client),
                                   queries: Queries = Depends(queries)) -> Dict[str, str]:
    most_visited_website = next(await async_mysql.execute_query(queries.select_most_visited_website))
    return most_visited_website
