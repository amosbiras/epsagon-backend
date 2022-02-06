from pydantic import BaseModel


class Queries(BaseModel):
    insert_request_metric: str
    select_request_by_id: str
    select_request_in_timeframe: str
    select_most_visited_website: str
