from .threading import StoppableThread
from functools import wraps
from logbook import Logger
from typing import Callable, Optional, Any


def thread_function(func: Callable[[Any], Any] = None, /, **kwargs) -> StoppableThread:
    """_summary_

    Args:
        func (Callable[[Any], Any], optional): _description_. Defaults to None.

    Returns:
        StoppableThread: _description_
    """

    def get_function(func_=None) -> StoppableThread:
        return StoppableThread(target=func_, **kwargs)

    if func is None:
        return get_function
    return get_function(func)


class FunctionLog:
    """Logging for your functions when they start and stop or end
you need to create a handler
in functions you get log attr for sending more logs
and flag attr to show that function have been stopped or ended
    """

    _logger: Logger
    _name: str

    def __init__(self, name: str, *, logger: Optional[Logger] = None) -> None:
        self._name = name

        if logger is None:
            self._logger = Logger(self._name)
        else:
            self._logger = logger

    @property
    def log(self) -> Logger:
        return self._logger

    @log.setter
    def log(self, logger: Logger) -> None:
        if not isinstance(logger, Logger):
            raise TypeError('')
        self._logger = logger

    def __call__(self, func: Optional[Callable[[Any], Any]] = None, *,
                 logger: Logger = None, info: Any = None) -> Callable[[Any], Any]:
        def get_function(func_: Optional[Callable[[Any], Any]] = None) -> Callable[[Any], Any]:
            @wraps(func_)
            def wraps_(*args, **kwargs):

                logger.info(f'{func_.__name__}-start')

                wraps_.__setattr__("log", logger)
                wraps_.__setattr__("error", False)

                result = func_(*args, **kwargs)

                if wraps_.__getattribute__("error"):
                    logger.error(f'{func_.__name__}-stopped')
                else:
                    logger.info(f'{func_.__name__}-end')

                wraps_.__delattr__("log")
                wraps_.__delattr__("error")

                return result

            return wraps_

        if logger is None:
            logger = self.log

        if func is None:
            return get_function
        return get_function(func)
