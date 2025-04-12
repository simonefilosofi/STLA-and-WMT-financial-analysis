import yfinance as yf
import pandas as pd


def main():
    """
    Main function to fetch and save financial data for Walmart.
    This function retrieves the balance sheet and income statement data for Walmart using the yfinance library,
    and saves the data to CSV files.

    """
    print("Hello from stla-and-wmt-financial-analysis!")

    # Fetching Walmart financial data
    print("Fetching Walmart financial data...")
    
    ticker = "WMT"
    wmt = yf.Ticker(ticker)

    # Storing Walmart data in variables
    historical_data = wmt.history(interval="1mo", period="5y")
    balance_sheet = wmt.balance_sheet
    income_statement = wmt.financials

    # Saving Walmart data to CSV files
    balansheet_to_csv = balance_sheet.to_csv('Dataset/wmt_balance_sheet.csv')
    income_statement_to_csv = income_statement.to_csv('Dataset/wmt_income_statement.csv')
    historical_data_to_csv = historical_data.to_csv('Dataset/wmt_historical_data.csv')

    # Printing messages to indicate successful saving of data
    print("Walmart historical data saved to wmt_historical_data.csv")
    print("Walmart Balance sheet data saved to wmt_balance_sheet.csv")
    print("Walmart Income statement data saved to wmt_income_statement.csv")



    # Fetching Stellantis financial data
    print("Fetching Stellantis financial data...")

    ticker = "STLA"
    stla = yf.Ticker(ticker)

    # Storing Stellantis data in variables
    historical_data = stla.history(interval="1mo", period="5y")
    balance_sheet = stla.balance_sheet
    income_statement = stla.financials

    # Saving Stellantis data to CSV files
    historical_data.to_csv('Dataset/stla_historical_data.csv')
    balance_sheet.to_csv('Dataset/stla_balance_sheet.csv')
    income_statement.to_csv('Dataset/stla_income_statement.csv')

    # Printing messages to indicate successful saving of data
    print("Stellantis Balance sheet data saved to stla_balance_sheet.csv")
    print("Stellantis Income statement data saved to stla_income_statement.csv")
    print("Stellantis historical data saved to stla_historical_data.csv")


    # Fetching S$&P 500 financial data
    print("Fetching S&P 500 financial data...")

    ticker = "^GSPC"
    sp500 = yf.Ticker(ticker)

    # Storing S&P 500 data in variables
    historical_data = sp500.history(interval="1mo", period="5y")
    balance_sheet = sp500.balance_sheet
    income_statement = sp500.financials

    # Saving S&P 500 data to CSV files
    historical_data.to_csv('Dataset/sp500_historical_data.csv')

    # Printing messages to indicate successful saving of data
    print("S&P 500 historical data saved to sp500_historical_data.csv")


if __name__ == "__main__":
    main()
