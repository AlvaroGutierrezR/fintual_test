from dataclasses import dataclass
from datetime import datetime
from instrument import Instrument


@dataclass
class InstrumentTransaction:
    entrance_value: float
    number_of_units_buyed: float
    timestamp: datetime

    def get_total_invest(self):
        return self.entrance_value * self.number_of_units_buyed

    def get_number_of_units_buyed(self):
        return self.number_of_units_buyed


@dataclass
class BuyedInstrument:
    instrument: Instrument
    transactions: list[InstrumentTransaction]
    total_invest: float
    total_units: float

    def __init__(self, instrument: Instrument):
        self.instrument = instrument
        self.transactions = []
        self.total_invest = 0
        self.total_units = 0

    def add_transaction(self, transaction: InstrumentTransaction):
        self.total_invest += transaction.get_total_invest()
        self.total_units += transaction.get_number_of_units_buyed()
        self.transactions.append(transaction)

    def get_last_value(self):
        return self.instrument.get_last_value()

    def get_instrument_type(self):
        return self.instrument.get_instrument_type()

    def get_total_unit_buyed(self):
        return self.total_units
