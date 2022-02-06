from typing import Dict


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def dict(self) -> Dict:
        return {
            'status_code': self.status_code,
            'exception': self.message
        }


class NoDataException(HTTPException):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(status_code, message)
