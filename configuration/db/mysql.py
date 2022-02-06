from pydantic import BaseModel


class MySQLConfig(BaseModel):
    host: str = 'localhost'
    port: int = 3306
    user: str
    password: str
    db: str
    connect_timeout: int = 60  # Timeout in seconds
