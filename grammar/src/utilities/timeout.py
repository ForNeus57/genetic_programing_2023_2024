from functools import wraps
from signal import signal, alarm, SIGALRM
from types import FrameType
from typing import NoReturn, Any, Callable


def timeout(timeout_seconds: int, default: Any = None) -> Callable:
    """
    Return a decorator that raises a TimedOutExc exception
    after timeout seconds, if the decorated function did not return.
    """

    def decorate(function: Callable) -> Callable:
        def handler(signum: int, frame: FrameType | None) -> NoReturn:
            raise TimeoutError(f'Function ({function.__name__}) timeout after {timeout_seconds} seconds!')

        @wraps(function)
        def new_f(*args, **kwargs):
            old_handler = signal(SIGALRM, handler)
            alarm(timeout_seconds)

            try:
                result = function(*args, **kwargs)  # f() always returns, in this scheme
            except TimeoutError as error:
                print(error)
                result = default
            finally:
                alarm(0)  # Alarm removed
                signal(SIGALRM, old_handler)  # Old signal handler is restored

            return result

        return new_f

    return decorate
