import requests
import pandas as pd
import matplotlib.pyplot as plt

class StockDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
    
    def get_stock_data(self, symbol, interval='5min'):
        """
        Fetch real-time stock data for a given symbol from Alpha Vantage.
        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        print("Status Code:", response.status_code)  # Print status code to verify connection
        data = response.json()

        # Check if the 'Time Series' key is in the data response
        time_series_key = f'Time Series ({interval})'
        if time_series_key in data:
            stock_data = pd.DataFrame.from_dict(data[time_series_key], orient='index')
            stock_data = stock_data.rename(columns={
                '1. open': 'Open',
                '2. high': 'High',
                '3. low': 'Low',
                '4. close': 'Close',
                '5. volume': 'Volume'
            })
            stock_data.index = pd.to_datetime(stock_data.index)
            return stock_data.astype(float)
        else:
            # Print detailed error message to troubleshoot
            print("Error fetching data:", data)
            return None

    def calculate_moving_average(self, stock_data, window=20):
        """
        Calculate the moving average for the stock data.
        """
        stock_data['Moving Average'] = stock_data['Close'].rolling(window=window).mean()
        return stock_data
    
    def plot_stock_data(self, stock_data, symbol):
        """
        Plot the stock prices and moving averages using matplotlib.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Close'], label='Close Price')
        if 'Moving Average' in stock_data.columns:
            plt.plot(stock_data['Moving Average'], label=f'Moving Average ({len(stock_data["Moving Average"].dropna())})')
        plt.title(f'{symbol} Stock Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    api_key = 'your_alpha_vantage_api_key'  # Use your actual API key here
    fetcher = StockDataFetcher(api_key)
    symbol = 'IBM'  # Example stock symbol for Apple
    stock_data = fetcher.get_stock_data(symbol, interval='5min')  # Fetch data with 5min interval
    if stock_data is not None:
        stock_data = fetcher.calculate_moving_average(stock_data, window=20)  # Calculate 20-period MA
        fetcher.plot_stock_data(stock_data, symbol)
