from datetime import datetime

from pydantic import BaseModel


class RequestsMetric(BaseModel):
    id: str
    timestamp: datetime
    duration: float
    target_url: str
    response_code: int
