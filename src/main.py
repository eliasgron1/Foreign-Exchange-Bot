import requests
import pandas as pd

import defs, utils, oanda_api, instruments

session = requests.Session()
url = f"{defs.OANDA_URL}accounts/{defs.ACCOUNT_ID}/instruments"
response = session.get(url, params=None, headers=defs.SECURE_HEADER)


print("Status check: ", response.status_code)



for pair in utils.get_currency_pairs():
    print(pair, pd.read_pickle(utils.get_historic_candles_filename(pair)))


