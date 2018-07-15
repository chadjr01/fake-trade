import os

import gdax

key = os.getenv("KEY")
secret = os.getenv('SECRET')
passphrase = os.getenv('PASSPHRASE')

auth_client = gdax.AuthenticatedClient(key, secret, passphrase,
                                  api_url="https://api-public.sandbox.gdax.com")

print(auth_client.get_accounts())
