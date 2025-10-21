from datetime import datetime
class Helpers:

    """
    Вспомогательный класс с методами для работы с датой и временем
    """

    @classmethod
    def SetDateTimeNow(cls):
        pass
        """
        Возвращает текущую дату и время в формате YYYYMMDD_HHMMSS

        Returns:
            str: Текущий timestamp, например '20251021_221500'
        """
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")