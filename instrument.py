from dataclasses import dataclass
from datetime import datetime
from utils.date_manager import DateManager
from enum import Enum


class InstrumentType(Enum):
    STOCK = 1
    FOUND = 2
    FIXED_INCOME = 3


@dataclass
class InstrumentValue:
    value: float
    timestamp: datetime


class Instrument:
    instrument_type: InstrumentType
    code: str
    name: str
    history_values: list[InstrumentValue]

    def __init__(self, instrument_type: InstrumentType, code: str, name: str, current_price_value: float):
        self.instrument_type = instrument_type
        self.code = code
        self.name = name
        self.history_values = []
        self.current_price(current_price_value)

    def current_price(self, value: float):
        current_datetime = DateManager.get_current_datetime_utc()
        instrumentValue = InstrumentValue(value, current_datetime)
        self.history_values.append(instrumentValue)

    def get_last_value(self):
        return self.history_values[-1].value

    def get_instrument_type(self):
        return self.instrument_type
