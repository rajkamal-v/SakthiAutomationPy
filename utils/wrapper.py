import functools
import time

import allure
from allure_commons.types import AttachmentType


def screenshot_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            a = func(*args, **kwargs)
        except Exception as ex:
            time_str = time.strftime("%Y%m%d-%H%M%S")
            allure.attach(args[0].driver.get_screenshot_as_png(), name=f"{func.__name__}_{time_str}",
                          attachment_type=AttachmentType.PNG)
            raise ex
        return a
    return wrapper

