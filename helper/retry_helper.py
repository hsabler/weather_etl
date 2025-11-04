import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
import requests

"""
    Класс, который обрабатывает логику повторных попыток с использованием библиотеки tenacity
    """

class RetryHelper:
    def __init__(self, max_attempts=3, delay=2):
        self.max_attempts = max_attempts
        self.delay = delay
        self.logger = logging.getLogger(__name__)

    def get_retry_decorator(self):
        """
        Возвращает декоратор для повторных попыток с параметрами
        """
        return retry(
            stop=stop_after_attempt(self.max_attempts),
            wait=wait_fixed(self.delay),
            retry=retry_if_exception_type(requests.exceptions.RequestException),
            before=self.before_retry,
            after=self.after_retry
        )

    def before_retry(self, retry_state):
        attempt = retry_state.attempt_number
        self.logger.info(f"Попытка {attempt}/{self.max_attempts}: Начинаем выполнение запроса...")

    def after_retry(self, retry_state):
        attempt = retry_state.attempt_number
        if retry_state.outcome.failed:
            self.logger.error(f"Попытка {attempt}/{self.max_attempts} завершена с ошибкой.")
        else:
            self.logger.info(f"Попытка {attempt}/{self.max_attempts} выполнена успешно.")
