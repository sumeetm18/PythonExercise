stocks = {"GOOG": (613.30, 625.86, 610.50),
        "MSFT": (30.25, 30.70, 30.19)}

stocks.setdefault("GOOG", "INVALID")
stocks.setdefault("BERRY",(10,20,30,40))
stocks.setdefault("HCLT", (10,20,30,40))

print(stocks)

for items in stocks.items():
    print(items[0],items[1])