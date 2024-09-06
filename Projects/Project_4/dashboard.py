import streamlit as st
from stock_data import StockDataFetcher

class StockDashboard:
    def __init__(self, api_key):
        """
        Initialize the dashboard with a StockDataFetcher instance.
        """
        self.fetcher = StockDataFetcher(api_key)
    
    def run_dashboard(self):
        """
        Run the Streamlit dashboard for real-time stock data analysis.
        """
        st.title("Real-Time Stock Market Analysis")

        # Get stock symbol from user input
        symbol = st.text_input("Enter Stock Symbol", "AAPL")

        if symbol:
            stock_data = self.fetcher.get_stock_data(symbol)
            if stock_data is not None:
                # Calculate the moving average
                stock_data = self.fetcher.calculate_moving_average(stock_data)
                
                # Display the data and charts
                st.line_chart(stock_data['Close'])
                st.line_chart(stock_data['Moving Average'])
                st.write(stock_data.head())
            else:
                st.error("Error fetching stock data.")

# Example usage
if __name__ == "__main__":
    api_key = 'your_alpha_vantage_api_key'  # Replace with your Alpha Vantage API key
    dashboard = StockDashboard(api_key)
    dashboard.run_dashboard()