from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)

print(stock.symbol)
print(stock.current)
print(stock.high)
print(stock.low)