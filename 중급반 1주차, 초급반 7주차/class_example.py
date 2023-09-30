class Stock:

    market = "KOSPI"
    
    @classmethod
    def from_tuple(cls, tup):
        return cls(tup[0])
    
    @classmethod
    def from_list(cls, lis):
        return cls(lis[0])
    
    @classmethod
    def show_market(cls):
        return cls.market
    
    def __init__(self, code):
        self.code = code
        self.price = 68400

    def buy(self, price):
        return self.price//price

    def sell(self, count):
        return self.price*count
    
    def __add__(self, target):
        return self.price + target.price
    def __sub__(self, target):
        return self.price - target.price
    def __mul__(self, target):
        return self.price * target.price
    def __truediv__(self, target):
        return self.price/target.price

samsung = Stock("005930")
samsung_from_tuple = Stock.from_tuple(("005930"))
samsung_from_list = Stock.from_list(["005930"])
print(samsung.code, samsung.price)

lg = Stock("066570"); lg.price = 100900

Stock.market = "KOSDAQ"
print(samsung.market, lg.market)

print(samsung.sell(100), samsung.buy(68400))
print(Stock.show_market())
print(samsung+lg, samsung-lg, samsung*lg, samsung/lg)