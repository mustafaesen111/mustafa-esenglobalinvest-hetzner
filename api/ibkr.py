python
#Mimari Sabitliği Sağlayan Unsurlar:Bu kod, Interactive Brokers TWS veya IB Gateway ile bağlantı kurar, belirli bir sembol için piyasa verisi çeker ve mimarisi sabit kalacak şekilde yapılandırılmıştır.
# - Sabit sembol: Kodda “AAPL” sabit olarak tanımlanmıştır.
# - Sabit bağlantı: 127.0.0.1:7497 adresi IB Gateway/TWS için varsayılan bağlantıdır.
# - Sabit veri tipi: Sadece tickPrice verisi alınır.
# - Sabit iş akışı: Bağlan → veri iste → bekle → bağlantıyı kes.
# - Sabit yapı: Kod tek dosyada, modülerlik veya dış bağımlılık olmadan çalışır.
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

