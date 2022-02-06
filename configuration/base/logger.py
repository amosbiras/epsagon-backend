from pydantic import BaseModel


class LoggerConfig(BaseModel):
    level: int
    format: str
