from functools import wraps
from signal import signal, alarm, SIGALRM


def timeout(timeout_seconds: int):
    """
    Return a decorator that raises a TimedOutExc exception
    after timeout seconds, if the decorated function did not return.
    """

    def decorate(f):
        def handler(signum, frame):
            raise TimeoutError(f'Function timeout after {timeout_seconds} seconds!')

        @wraps(f)  # Preserves the documentation, name, etc.
        def new_f(*args, **kwargs):
            old_handler = signal(SIGALRM, handler)
            alarm(timeout_seconds)

            result = f(*args, **kwargs)  # f() always returns, in this scheme

            signal(SIGALRM, old_handler)  # Old signal handler is restored
            alarm(0)  # Alarm removed

            return result

        return new_f

    return decorate
