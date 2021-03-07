import pymongo as mongo
import redis
import pandas as pd
import time

r = redis.Redis()
# get data from redis
df_string = r.get('key')

#convert string to df
df = pd.read_csv(df_string)

client = mongo.MongoClient("mongodb://127.0.0.1:27017/")

# make db for bitcoin
bitcoin_db = client["Bitcoin"]
 
# make collection
col_highest = bitcoin_db["amounts"]

#get highest value
for i in df[3]:
    df[3] = df[3].replace("$","").replace(",","")
df[3] = [item.replace("$","").replace(",","") for item in df[3]]
df[3] = df[3].astype(float)

max_result = df[3].max()

#find index of max_result
index_max = df.loc[df['AmountUSD'] == max_result].index[0]

#whole row of max_result
data_max = df.loc[index_max]

# data in collection
data_max[0] = hash
data_max[1] = hour
data_max[2] = amountBTC
data_max = {'Hash': hash, 'Time': hour, 'Amount_BTC': amountBTC, 'Amount_USD': max_result}
col_highest.insert_one(data_max)

#clear na minuut
r.expire('key', 60)
