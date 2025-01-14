from typing import Callable
from functools import wraps
import time


def timeout(timeout_seconds: int):
    """Simple decorator that fails a test that takes longer than time_seconds to run.

    Args:
        timeout_seconds (int): Maximum amount of time, in seconds, your test should run

    Returns:
        Returns nothing but does assert a failure if the test takes longer to run than timeout_seconds
    """

    def inner_timeout_decorater(test_function: Callable):

        @wraps(test_function)
        def timer_wrapper(self, *args, **kwargs):
            start = time.perf_counter()
            test_function(self, *args, **kwargs)
            end = time.perf_counter()
            self.assertLessEqual(
                end - start,
                timeout_seconds,
                msg=
                f"{test_function.__name__} ran in {end - start:0.4f} seconds but needed to run sub {timeout_seconds}"
            )

        return timer_wrapper

    return inner_timeout_decorater
