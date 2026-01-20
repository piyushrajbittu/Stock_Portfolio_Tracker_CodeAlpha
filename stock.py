# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish adding stocks\n")

while True:
    stock = input("Enter stock name: ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available. Try again.\n")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment
    
    print(f"Added {quantity} shares of {stock}\n")

print("\n📊 Portfolio Summary")
print("----------------------")

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - Quantity: {qty}, Value: ${value}")

print("----------------------")
print(f"💰 Total Investment Value: ${total_investment}")

# Save to file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("----------------------\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}, Quantity: {qty}, Value: ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    
    print("✅ Portfolio saved to portfolio.txt")