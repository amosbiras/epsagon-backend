import aiomysql

from typing import NoReturn, Type, Generator, Dict, Any, Optional
from types import TracebackType

from aiomysql import DictCursor, Connection as AsyncMYSQLConnection
from pymysql import MySQLError

from configuration import MySQLConfig


class AsyncMySQLClient:
    def __init__(self, mysql_config: MySQLConfig):
        self.__mysql_config = mysql_config
        self.__mysql_connector: AsyncMYSQLConnection = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> NoReturn:
        self.close()

    async def connect(self) -> NoReturn:
        self.__mysql_connector = await aiomysql.connect(**self.__mysql_config.dict())

    def close(self) -> NoReturn:
        self.__mysql_connector.close()

    async def execute_query(self, query: str, size: Optional[int] = None, **query_params: Any) \
            -> Generator[Dict, None, None]:
        cursor: DictCursor = await self.__mysql_connector.cursor(DictCursor)
        try:
            await cursor.execute(query, query_params)
            await self.__mysql_connector.commit()
            return (result for result in await cursor.fetchmany(size=size))
        except MySQLError as e:
            raise e
        finally:
            if await self.__mysql_connector.ping():
                await cursor.close()
