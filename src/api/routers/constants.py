from enum import Enum

REQUESTS_METRICS_ENDPOINT: str = '/api/v1/requests-metrics'


class RequestsMetricsAPI(str, Enum):
    POST_REQUEST_METRIC: str = REQUESTS_METRICS_ENDPOINT
    GET_REQUEST_BY_ID: str = REQUESTS_METRICS_ENDPOINT
    GET_REQUESTS_IN_TIMEFRAME: str = f'{REQUESTS_METRICS_ENDPOINT}/timeframe'
    GET_MOST_VISITED_WEBSITE: str = f'{REQUESTS_METRICS_ENDPOINT}/most-visited-website'
