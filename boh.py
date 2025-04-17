import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

walmart_df = pd.read_csv('Dataset/Investing.com/Walmart Stock Price History.csv')
stellantis_df = pd.read_csv('Dataset/Investing.com/Stellantis NV Stock Price History.csv')
sp500_df = pd.read_csv('Dataset/Investing.com/S&P 500 Historical Data.csv')

for df in [walmart_df, stellantis_df, sp500_df]:
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df.sort_values('Date', inplace=True)


def clean_price_column(df):
    df['Price'] = df['Price'].astype(str).str.replace(',', '', regex=False).astype(float) 
    return df
    
walmart_df = clean_price_column(walmart_df)
stellantis_df = clean_price_column(stellantis_df)
sp500_df = clean_price_column(sp500_df)


walmart_df['Return'] = walmart_df['Price'].pct_change()
stellantis_df['Return'] = stellantis_df['Price'].pct_change()
sp500_df['Return'] = sp500_df['Price'].pct_change()

returns_df = pd.merge(walmart_df[['Date', 'Return']],
                      stellantis_df[['Date', 'Return']],
                      on='Date', suffixes=('_Walmart', '_Stellantis'))
returns_df = pd.merge(returns_df,
                      sp500_df[['Date', 'Return']],
                      on='Date')
returns_df.rename(columns={'Return': 'Return_SP500'}, inplace=True)
returns_df.dropna(inplace=True)

X = returns_df[['Return_SP500']].values

y_walmart = returns_df['Return_Walmart'].values
beta_walmart = LinearRegression().fit(X, y_walmart).coef_[0]

y_stellantis = returns_df['Return_Stellantis'].values
beta_stellantis = LinearRegression().fit(X, y_stellantis).coef_[0]

print("Walmart Beta:", beta_walmart)
print("Stellantis Beta:", beta_stellantis)


avg_return_walmart = returns_df['Return_Walmart'].mean()
avg_return_stellantis = returns_df['Return_Stellantis'].mean()
std_walmart = returns_df['Return_Walmart'].std()
std_stellantis = returns_df['Return_Stellantis'].std()

print("Average Return Walmart:", avg_return_walmart)
print("Average Return Stellantis:", avg_return_stellantis)
print("Standard Deviation Walmart:", std_walmart)
print("Standard Deviation Stellantis:", std_stellantis)

cov_matrix = returns_df[['Return_Walmart', 'Return_Stellantis']].cov().values

weights = np.linspace(0, 1, 101)
portfolio_returns = []
portfolio_stds = []

for w in weights:
    w_walmart = w
    w_stellantis = 1 - w
    port_return = w_walmart * avg_return_walmart + w_stellantis * avg_return_stellantis
    port_variance = (
        w_walmart**2 * std_walmart**2 +
        w_stellantis**2 * std_stellantis**2 +
        2 * w_walmart * w_stellantis * cov_matrix[0, 1]
    )
    port_std = np.sqrt(port_variance)
    
    portfolio_returns.append(port_return)
    portfolio_stds.append(port_std)


from matplotlib import pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(portfolio_stds, portfolio_returns, label='Portfolio Curve')
plt.scatter(std_walmart, avg_return_walmart, color='red', label='Walmart', zorder=5)
plt.scatter(std_stellantis, avg_return_stellantis, color='blue', label='Stellantis', zorder=5)
plt.title('Risk-Return Profile: Walmart, Stellantis, and Portfolios')
plt.xlabel('Standard Deviation (Risk)')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True)
plt.show()