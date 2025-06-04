# Fintual Test

Fintual Test is a Python-based tool for simulating and analyzing investment portfolios. It allows users to create portfolios, buy financial instruments (such as stocks and funds), and analyze their portfolio distribution according to different risk profiles.

## Features

- **Portfolio Management:** Add and track multiple financial instruments in a portfolio.
- **Instrument Tracking:** Supports stocks, funds, and fixed income instruments with historical price tracking.
- **Risk Profile Analysis:** Analyze your portfolio's distribution and receive recommendations based on predefined risk profiles (Risk, Moderate, Conservative).
- **Transaction History:** Each instrument keeps a record of all buy transactions with timestamps.
- **Extensible Design:** Easily add new instrument types or risk profiles.

## Usage

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AlvaroGutierrezR/fintual_test.git
   cd fintual_test
   ```

2. **Run the main script:**
   ```sh
   python main.py
   ```

3. **Example Output:**
   ```
   Porfolio current total value: 36.5
   Current ditribution of portfolio
   ---- STOCK ----
   Current: Total buyed: 33.5 units, that is equivalent 92.0% to your portfolio
   Recomendation: Reduce 22.0% to be in 70.0%
   ---- FOUND ----
   Current: Total buyed: 3.0 units, that is equivalent 8.0% to your portfolio
   Recomendation: Up 12.0% to be in 20.0%
   ---- FIXED_INCOME ----
   Current: Total buyed: 0 units, that is equivalent 0% to your portfolio
   Recomendation: Add at least 10.0% of your total
   ```

## Project Structure

- `main.py` — Example usage and simulation.
- `portfolio.py` — Portfolio logic and operations.
- `instrument.py` — Instrument and price history definitions.
- `instrument_operations.py` — Transaction and instrument management.
- `risk_profiles.py` — Risk profile definitions and analysis logic.
- `utils/date_manager.py` — Utility for handling UTC timestamps.

## Project Structure

- `main.py` — Example usage and simulation.
- `portfolio.py` — Portfolio logic and operations.
- `instrument.py` — Instrument and price history definitions.
- `instrument_operations.py` — Transaction and instrument management.
- `risk_profiles.py` — Risk profile definitions and analysis logic.
- `utils/date_manager.py` — Utility for handling UTC timestamps.

## References

Web searching:  
- https://docs.python.org/3/library/datetime.html  
- https://www.w3schools.com/python/python_comments.asp  
- https://docs.python.org/es/3.13/library/__main__.html  
- https://docs.python.org/3/library/dataclasses.html  
- https://www.digitalocean.com/community/tutorials/python-static-method  
- https://docs.python.org/3/library/enum.html  

LLM:  
- create a README for this files.
- add output of the script to readme.md

## License

This project is licensed under the MIT License.