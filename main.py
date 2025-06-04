from instrument import Instrument, InstrumentType
from portfolio import Portfolio
from risk_profiles import RiskProfiles

if __name__ == '__main__':
    nvidia_stock = Instrument(
        InstrumentType.STOCK, 'NVDA', 'Nvidia', 1)
    apple_stock = Instrument(
        InstrumentType.STOCK, 'APPL', 'Apple', 2)
    risky_norris_found = Instrument(
        InstrumentType.FOUND, 'RISKY_NORRIS', 'FONDO MUTUO FINTUAL RISKY NORRIS', 1.5)

    my_portfolio = Portfolio(RiskProfiles.RISK)

    my_portfolio.buy_instrument(nvidia_stock, 2.3)
    my_portfolio.buy_instrument(apple_stock, 1)

    # dia siguiente
    nvidia_stock.current_price(3)
    my_portfolio.buy_instrument(nvidia_stock, 2)

    # dia siguiente
    apple_stock.current_price(4)
    my_portfolio.buy_instrument(apple_stock, 2)
    nvidia_stock.current_price(5)
    my_portfolio.buy_instrument(risky_norris_found, 2)

    my_portfolio.analize()
