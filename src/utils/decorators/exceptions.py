import logging

from functools import wraps
from typing import Callable, Any

from fastapi import status

from src.exceptions import HTTPException

logger = logging.getLogger(__name__)


def exception_decorator(function: Callable) -> Any:
    @wraps(function)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = await function(*args, **kwargs)
            return result
        except HTTPException as e:
            logger.error(f'{e.status_code}, {type(e).__name__} -  {e.message}', exc_info=True,
                         extra={'exception_type': type(e).__name__}.update(e.dict()))
            raise e
        except Exception as e:
            logger.error(
                f'An unexpected error occurred. {status.HTTP_500_INTERNAL_SERVER_ERROR}, {type(e).__name__} - {e}',
                exc_info=True, extra={'exception_type': type(e).__name__, 'exception': e,
                                      'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR})
            raise e

    return wrapper
