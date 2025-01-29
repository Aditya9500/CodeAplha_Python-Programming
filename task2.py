import requests
from prettytable import PrettyTable

# Alpha Vantage API key (Get your free API key from https://www.alphavantage.co/)
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

# Portfolio dictionary to store stock data
portfolio = {}

def get_stock_price(symbol):
    """Fetch the latest stock price using Alpha Vantage API."""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except KeyError:
        print("Error fetching stock data. Check the symbol and try again.")
        return None

def add_stock(symbol, quantity, purchase_price):
    """Add a stock to the portfolio."""
    if symbol in portfolio:
        portfolio[symbol]["quantity"] += quantity
        portfolio[symbol]["purchase_price"] = (portfolio[symbol]["purchase_price"] + purchase_price) / 2
    else:
        portfolio[symbol] = {"quantity": quantity, "purchase_price": purchase_price}
    print(f"Added {quantity} shares of {symbol} at ₹{purchase_price} each.")

def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from the portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")

def view_portfolio():
    """Display the stock portfolio with real-time prices and profit/loss."""
    table = PrettyTable(["Stock", "Quantity", "Purchase Price", "Current Price", "Profit/Loss"])
    
    total_investment = 0
    total_current_value = 0

    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price is None:
            continue
        
        investment = data["quantity"] * data["purchase_price"]
        current_value = data["quantity"] * current_price
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        table.add_row([symbol, data["quantity"], f"₹{data['purchase_price']:.2f}", f"₹{current_price:.2f}", f"₹{profit_loss:.2f}"])
    
    print(table)
    print(f"Total Investment: ₹{total_investment:.2f}")
    print(f"Current Portfolio Value: ₹{total_current_value:.2f}")
    print(f"Total Profit/Loss: ₹{total_current_value - total_investment:.2f}")

# Example Usage
add_stock("AAPL", 10, 150)
add_stock("GOOGL", 5, 2800)
view_portfolio()
remove_stock("GOOGL")
view_portfolio()
