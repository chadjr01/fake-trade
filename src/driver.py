import json
import os

import gdax

from src.currency import Currency
from src.models.account_model import AccountModel

key = os.getenv("KEY")
secret = os.getenv('SECRET')
passphrase = os.getenv('PASSPHRASE')

auth_client = gdax.AuthenticatedClient(key, secret, passphrase, api_url="https://api-public.sandbox.gdax.com")

accounts_string = json.dumps(auth_client.get_accounts())
accounts_json = json.loads(accounts_string)
accounts_models = [AccountModel(account['id'], Currency[account['currency']], account['balance'], account['available'], account['hold'], account['profile_id']) for account in accounts_json]

for account in accounts_models:
    print(account)
