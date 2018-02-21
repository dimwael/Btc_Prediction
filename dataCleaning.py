import numpy as np
import pandas as pd
import pickle
import quandl
from datetime import datetime

quandKey = "scAeUJ4rxYFvkrSkUFKn"
quandl.ApiConfig.api_key = quandKey
def get_quandl_data(quandl_id):
    '''Download and cache Quandl dataseries'''
    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)
        print('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        print('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(quandl_id, returns="pandas")
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(quandl_id, cache_path))
    return df

btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')

#reduce the weighted price by 1000
btc_usd_price_kraken['Weighted Price'] = btc_usd_price_kraken['Weighted Price']/1000

#Save the actual Data in csv file:
btc_usd_price_kraken.to_csv('btc_kraken.csv',index=False)

#Create the column datetime for the index :
btc_usd_price_kraken["datetime"] = btc_usd_price_kraken.index

#Convert date to pandas datetime
#btc_usd_price_kraken.dt = pd.to_datetime(btc_usd_price_kraken.datetime)

#Fill the empty spot in the data
btc_usd_price_kraken.fillna(0)

# create new columns for date information
btc_usd_price_kraken["year"]  = btc_usd_price_kraken ["datetime"].dt.year
btc_usd_price_kraken["month"] = btc_usd_price_kraken ["datetime"].dt.month
btc_usd_price_kraken["day"]   = btc_usd_price_kraken ["datetime"].dt.day

# take rows with no missing Weighted Prices
btc_usd_price_kraken = btc_usd_price_kraken[np.isfinite(btc_usd_price_kraken['Weighted Price'])]

# drop unnecessary columns
btc_usd_price_kraken = btc_usd_price_kraken.drop('Open',1)
btc_usd_price_kraken = btc_usd_price_kraken.drop('High',1)
btc_usd_price_kraken = btc_usd_price_kraken.drop('Low',1)
btc_usd_price_kraken = btc_usd_price_kraken.drop('Close',1)
btc_usd_price_kraken = btc_usd_price_kraken.drop('Volume (BTC)',1)
btc_usd_price_kraken = btc_usd_price_kraken.drop('Volume (Currency)',1)

#delete the datetime column
btc_usd_price_kraken = btc_usd_price_kraken.drop('datetime',1)
# rename target variable as class
btc_usd_price_kraken.rename(columns={'Weighted Price': 'class'}, inplace=True)

#save to_csv
btc_usd_price_kraken.to_csv('cleaned_btc_kraken.csv',index=False)
