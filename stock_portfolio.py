import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=[
            "Ticker", "Shares", "Price Bought", "Current Price", "Total Value", "Profit/Loss"
        ])

    def add_stock(self, ticker, shares, price_bought):
        """
        Adds a stock to the portfolio.

        Args:
            ticker (str): Ticker symbol of the stock (uppercase).
            shares (int): Number of shares purchased.
            price_bought (float): Price per share at purchase.

        Raises:
            ValueError: If shares or price_bought are not positive.
        """
        if shares <= 0 or price_bought <= 0:
            raise ValueError("Shares and price must be positive values.")

        ticker = ticker.upper()
        stock = yf.Ticker(ticker)
        try:
            current_price = stock.history(period='1d').iloc[0]['Close']
        except (ConnectionError, KeyError):
            print(f"Error fetching data for {ticker}. Skipping...")
            return

        total_value = shares * current_price
        profit_loss = (current_price - price_bought) * shares

        new_data = {
            "Ticker": ticker,
            "Shares": shares,
            "Price Bought": price_bought,
            "Current Price": current_price,
            "Total Value": total_value,
            "Profit/Loss": profit_loss
        }

        # Create a DataFrame from new_data and ensure it has no empty or all-NA columns
        new_row_df = pd.DataFrame([new_data])
        new_row_df.dropna(axis=1, how='all', inplace=True)

        # Use pd.concat to add the new row to the DataFrame
        self.portfolio = pd.concat([self.portfolio, new_row_df], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at {price_bought} to the portfolio.")


    def remove_stock(self, ticker):
        ticker = ticker.upper()
        if ticker in self.portfolio["Ticker"].values:
            self.portfolio = self.portfolio[self.portfolio["Ticker"] != ticker]
            print(f"Removed {ticker} from the portfolio.")
        else:
            print(f"Ticker {ticker} not found in the portfolio.")

    def update_portfolio(self):
        for index, row in self.portfolio.iterrows():
            ticker = row["Ticker"]
            try:
                stock = yf.Ticker(ticker)
                current_price = stock.history(period='1d').iloc[0]['Close']
            except (ConnectionError, KeyError):
                print(f"Error fetching data for {ticker}. Skipping...")
                continue

            self.portfolio.at[index, "Current Price"] = current_price
            self.portfolio.at[index, "Total Value"] = row["Shares"] * current_price
            self.portfolio.at[index, "Profit/Loss"] = (current_price - row["Price Bought"]) * row["Shares"]

    def show_portfolio(self):
        self.update_portfolio()
        print(self.portfolio)


def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions: add, remove, show, quit")
        option = input("Choose an option: ").strip().lower()

        if option == "add":
            ticker = input("Enter the stock ticker: ").strip().upper()
            shares = int(input("Enter the number of shares: "))
            price_bought = float(input("Enter the price you bought the shares at: "))
            try:
                portfolio.add_stock(ticker, shares, price_bought)
            except ValueError as e:
                print(e)

        elif option == "remove":
            ticker = input("Enter the stock ticker to remove: ").strip().upper()
            portfolio.remove_stock(ticker)

        elif option == "show":
            portfolio.show_portfolio()

        elif option == "quit":
            print("Exiting the portfolio tracker.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()