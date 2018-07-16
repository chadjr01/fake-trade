class AccountModel:
    def __init__(self, id, currency, balance, available, hold, profile_id):
        self._id = id
        self._currency = currency
        self._balance = balance
        self._available = available
        self._hold = hold
        self._profile_id = profile_id

    @property
    def id(self):
        return self._id

    @property
    def currency(self):
        return self._currency

    @property
    def balance(self):
        return self._balance

    @property
    def available(self):
        return self._available

    @property
    def hold(self):
        return self._hold

    @property
    def profile_id(self):
        return self._profile_id
