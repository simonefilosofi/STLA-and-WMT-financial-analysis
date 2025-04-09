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
    balance_sheet = wmt.balance_sheet
    income_statement = wmt.financials
    balansheet_to_csv = balance_sheet.to_csv('Dataset/wmt_balance_sheet.csv')
    income_statement_to_csv = income_statement.to_csv('Dataset/wmt_income_statement.csv')
    print("Walmart Balance sheet data saved to wmt_balance_sheet.csv")
    print("Walmart Income statement data saved to wmt_income_statement.csv")

    # Fetching Stellantis financial data
    print("Fetching Stellantis financial data...")

    ticker = "STLA"
    stla = yf.Ticker(ticker)
    balance_sheet = stla.balance_sheet
    income_statement = stla.financials
    balansheet_to_csv = balance_sheet.to_csv('Dataset/stla_balance_sheet.csv')
    income_statement_to_csv = income_statement.to_csv('Dataset/stla_income_statement.csv')
    print("Stellantis Balance sheet data saved to stla_balance_sheet.csv")
    print("Stellantis Income statement data saved to stla_income_statement.csv")


if __name__ == "__main__":
    main()
