python
import requests

class OANDAClient:
    def __init__(self, token: str, account_id: str):
        self.base_url = "https://api-fxpractice.oanda.com/v3"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
}
        self.account_id = account_id

    def get_price(self, instrument: str):
        url = f"{self.base_url}/pricing?instruments={instrument}&accountId={self.account_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            prices = response.json().get("prices", [])
            if prices:
                bid = prices[0].get("bids", [{}])[0].get("price")
                ask = prices[0].get("asks", [{}])[0].get("price")
                return {"bid": bid, "ask": ask}
        return None
