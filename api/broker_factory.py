python
from api.ibkr import IBKRClient
from api.oanda import OANDAClient

def get_broker(broker_name: str, credentials: dict):
    if broker_name == "IBKR":
        return IBKRClient()
    elif broker_name == "OANDA":
        return OANDAClient(
            token=credentials.get("token"),
            account_id=credentials.get("account_id")
)
    else:
        raise ValueError(f"Desteklenmeyen broker: {broker_name}")
