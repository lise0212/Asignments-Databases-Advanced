import pymongo as mongo
import redis
import pandas as pd
import time
import zlib
import pickle

r = redis.Redis()

# call mongo
client = mongo.MongoClient("mongodb://127.0.0.1:8081")

# make db for bitcoin
bitcoin_db = client["Bitcoin"]
    
# make collection
col_highest = bitcoin_db["data"]

def GetValue():
    # get data from redis
    df = pickle.loads(zlib.decompress(r.get("key"))) 

    #convert string to df
    #df = pd.read_csv(str(df_string))
    #df = pd.read_csv('dataframe.csv')

    # name columns
    df.columns=['hash','hour','amountBTC', 'amountUSD']

    #get highest value
    for i in df['amountUSD']:
        df['amountUSD'] = df['amountUSD'].replace("$","").replace(",","")
    df['amountUSD'] = [item.replace("$","").replace(",","") for item in df['amountUSD']]
    df['amountUSD'] = df['amountUSD'].astype(float)

    # sorteer df van hoog naar laag
    df = df.sort_values(by=['amountUSD'], axis=0, ascending=False, inplace=False)

    # neem eerste rij
    max_result = df.head(1)

    # slaag gegevens op
    hash = max_result._get_value(0, 'hash')
    hour = max_result._get_value(0, 'hour')
    amountBTC = max_result._get_value(0, 'amountBTC')
    amountUSD = max_result._get_value(0, 'amountUSD')
    data_max = {'Hash': hash, 'Time': hour, 'Amount_BTC': amountBTC, 'Amount_USD': amountUSD}

    # data in collection
    col_highest.insert_one(data_max)

GetValue()

while True:
    GetValue()
    time.sleep(60)

