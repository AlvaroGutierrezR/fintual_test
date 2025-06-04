from enum import Enum
from instrument import InstrumentType
from instrument_operations import BuyedInstrument


class RiskProfiles(Enum):
    RISK = 'RISK'
    MODERATE = 'MODERATE'
    CONSERVATIVE = 'CONSERVATIVE'


class ProfileRecomendedDistribution:
    PROFILES = {
        RiskProfiles.RISK: {
            InstrumentType.STOCK: 0.7,
            InstrumentType.FOUND: 0.2,
            InstrumentType.FIXED_INCOME: 0.1
        },
        RiskProfiles.MODERATE: {
            InstrumentType.STOCK: 0.5,
            InstrumentType.FOUND: 0.5
        },
        RiskProfiles.CONSERVATIVE: {
            InstrumentType.STOCK: 0.8,
            InstrumentType.FOUND: 0.2
        }
    }


class ProfileFactoryAnalizer:
    @staticmethod
    def makeProfile(profile: RiskProfiles):
        return PorfolioAnalizer(
            ProfileRecomendedDistribution.PROFILES[profile])


class PorfolioAnalizer():
    recomended_distribution: ProfileRecomendedDistribution

    def __init__(self, recomended_distribution: ProfileRecomendedDistribution):
        self.recomended_distribution = recomended_distribution

    def format_percentage(self, percentage: float):
        return f"{round(percentage, 2)*100}%"

    def analize(self, buyed_instruments: dict[str, BuyedInstrument]):
        instrument_categories = {}
        total_invested = 0
        for code, buyed_instrument in buyed_instruments.items():
            instrument_type = buyed_instrument.get_instrument_type()

            if instrument_type not in instrument_categories:
                instrument_categories[instrument_type] = 0

            invested = buyed_instrument.get_total_unit_buyed() * buyed_instrument.get_last_value()
            instrument_categories[instrument_type] += invested
            total_invested += invested

        print('Porfolio current total value:', total_invested)
        print('Current ditribution of portfolio')

        for instrument_type in self.recomended_distribution:
            print('----', instrument_type.name, '----')
            if instrument_type not in instrument_categories:
                print(
                    f"Current: Total buyed: 0 units, that is equivalent 0% to your portfolio")
                print(
                    f"Recomendation: Add at least {self.recomended_distribution[instrument_type]*100}% of your total")
                continue

            value = instrument_categories[instrument_type]
            percentage = value/total_invested
            formated_percentage = self.format_percentage(percentage)
            print(
                f"Current: Total buyed: {value} units, that is equivalent {formated_percentage} to your portfolio")

            recomended = "Recomendation: "
            if percentage > self.recomended_distribution[instrument_type]:
                formated_percentage = self.format_percentage(
                    percentage - self.recomended_distribution[instrument_type])
                recomended += f"Reduce {formated_percentage} to be in {self.recomended_distribution[instrument_type]*100}%"
            else:
                formated_percentage = self.format_percentage(
                    self.recomended_distribution[instrument_type] - percentage)
                recomended += f"Up {formated_percentage} to be in {self.recomended_distribution[instrument_type]*100}%"
            print(recomended)
