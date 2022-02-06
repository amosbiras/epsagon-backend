from functools import lru_cache
from aiocache import cached as async_cache

from src.db import AsyncMySQLClient
from src.utils.decorators import exception_decorator
from configuration import Queries, ConfigurationPaths, load_yaml, MySQLConfig


@async_cache()
@exception_decorator
async def async_mysql_client() -> AsyncMySQLClient:
    async_mysql = AsyncMySQLClient(MySQLConfig(**load_yaml(ConfigurationPaths.DB)))
    await async_mysql.connect()
    return async_mysql


@lru_cache()
def queries() -> Queries:
    return Queries(**load_yaml(ConfigurationPaths.QUERIES))
