python
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

class IBKRClient(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}

    def tickPrice(self, reqId, tickType, price, attrib):
        self.data[reqId] = price
        print(f"[VERİ] ReqId: {reqId} | TickType: {tickType} | Fiyat: {price}")

def sabit_kontrat():
    kontrat = Contract()
    kontrat.symbol = "AAPL"           # Sabit sembol
    kontrat.secType = "STK"           # Sabit enstrüman tipi
    kontrat.exchange = "SMART"        # Sabit borsa
    kontrat.currency = "USD"          # Sabit para birimi
    return kontrat

def baslat_ibkr():
    istemci = IBKRClient()
    istemci.connect("127.0.0.1", 7497, clientId=0)  # Sabit bağlantı noktası

    def calistir():
        istemci.run()

    thread = threading.Thread(target=calistir, daemon=True)
    thread.start()

    time.sleep(1)  # Bağlantı için kısa bekleme

    kontrat = sabit_kontrat()
    istemci.reqMktData(1, kontrat, "", False, False, [])

    time.sleep(10)  # Verinin alınması için bekleme

    istemci.disconnect()

if __name__ == "__main__":
    baslat_ibkr()

