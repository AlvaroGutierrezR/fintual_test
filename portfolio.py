from instrument_operations import BuyedInstrument, InstrumentTransaction
from instrument import Instrument
from utils.date_manager import DateManager
from risk_profiles import RiskProfiles, ProfileFactoryAnalizer


class Portfolio:
    buyed_instruments: dict[str, BuyedInstrument]
    total_invest: float
    risk_profile: RiskProfiles

    def __init__(self, risk_profile: RiskProfiles):
        self.risk_profile = risk_profile
        self.buyed_instruments = {}
        self.total_invest = 0

    def buy_instrument(self, instrument: Instrument, number_of_instruments_buyed: float):
        self.__create_if_not_exist_instrument_code(instrument)

        instrument_transaction = self.__create_instrument_transaction(
            instrument, number_of_instruments_buyed)
        self.total_invest += instrument_transaction.get_total_invest()

        self.buyed_instruments[instrument.code].add_transaction(
            instrument_transaction)

    def __create_if_not_exist_instrument_code(self, instrument: Instrument):
        instrument_code = instrument.code
        if instrument_code not in self.buyed_instruments:
            self.buyed_instruments[instrument_code] = BuyedInstrument(
                instrument)

    def __create_instrument_transaction(self, instrument: Instrument, number_of_instruments_buyed: float):
        current_instrument_value = instrument.get_last_value()
        current_datetime = DateManager.get_current_datetime_utc()
        return InstrumentTransaction(current_instrument_value, number_of_instruments_buyed, current_datetime)

    def analize(self):
        porfolio_analizer = ProfileFactoryAnalizer.makeProfile(
            self.risk_profile)
        return porfolio_analizer.analize(self.buyed_instruments)
