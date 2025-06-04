from datetime import datetime, UTC


class DateManager:
    @staticmethod
    def get_current_datetime_utc():
        return datetime.now(UTC)
