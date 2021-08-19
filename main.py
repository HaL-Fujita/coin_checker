import pybitflyer
import time

api_key = 'GAbjEQZ798rNsv6WYfUmfC'
api_secret = 'Xmc9ZLltUB6T4ezZP2Hm+BqkGOvi5t/u7szuKC6eMWc='

api = pybitflyer.API(api_key=api_key, api_secret=api_secret)

#直近のBTC取引価格
base_price = api.ticker(product_code="BTC_JPY")["ltp"]
print("bot開始時の価格は"+str(base_price)+"です。")


while True:
    time.sleep(5)
    price_now = api.ticker(product_code="BTC_JPY")["ltp"]
    print("現在のBTCJPYは "+str(price_now)+" です。")
    if base_price*0.95 >= price_now:
        print("bitcoin価格が下落しています。")
        base_price = price_now

    elif base_price*1.05 <= price_now:
        print("bitcoin価格が上昇しています。")
        base_price = price_now

    else:
        print("bitcoin価格に大きな変動はありません。")
