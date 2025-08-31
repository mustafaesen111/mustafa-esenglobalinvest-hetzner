python
class AdminBrokerTools:
    def __init__(self, broker_client):
        self.client = broker_client

    def force_sync(self):
        # Admin tarafından tetiklenen manuel senkronizasyon
        print("[ADMIN] İşlem senkronizasyonu başlatıldı.")
        # Örnek: fiyat verisi çekilip loglanabilir
        if hasattr(self.client, "get_price"):
            data = self.client.get_price("EUR_USD")
            print(f"[ADMIN] Fiyat verisi: {data}")
        else:
            print("[ADMIN] Bu broker fiyat verisi sağlamıyor.")

    def audit_log(self):
        # Admin loglama işlemi
        print("[ADMIN] Broker logları denetleniyor...")
        # Gerçek sistemde burada log dosyaları veya API çağrıları olur
