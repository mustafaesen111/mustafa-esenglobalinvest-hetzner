# Oranlı kopyalama (%50, %75)   Mimari Sabitliği Sağlayan Unsurlar:
# Sabit veri yapısı: source_trade ve target_account sözlük formatında beklenir.
# Sabit eşleştirme mantığı: Oranlı işlem hesaplama calculate_target_quantity() ile yapılır.
# Sabit iş akışı: Al → Hesapla → Oluştur → Uygula.
# Broker bağımsızlığı: Broker API çağrısı dışarıdan entegre edilir, bu dosya değişmez.
python
class TradeSyncService:
    def __init__(self, source_trade, target_account, sync_ratio=1.0):
        """
        source_trade: dict → {'symbol': 'AAPL', 'action': 'BUY', 'quantity': 100}
        target_account: dict → {'id': 'user123', 'broker': 'IBKR'}
        sync_ratio: float → 0.5 for 50%, 0.75 for 75%, etc.
        """
        self.source_trade = source_trade
        self.target_account = target_account
        self.sync_ratio = sync_ratio

    def calculate_target_quantity(self):
        original_qty = self.source_trade.get("quantity", 0)
        synced_qty = int(original_qty * self.sync_ratio)
        return max(synced_qty, 1)  # En az 1 işlem yapılmalı

    def generate_synced_trade(self):
        synced_trade = {
            "symbol": self.source_trade["symbol"],
            "action": self.source_trade["action"],
            "quantity": self.calculate_target_quantity(),
            "account_id": self.target_account["id"],
            "broker": self.target_account["broker"]
}
        return synced_trade

    def execute_trade(self):
        trade = self.generate_synced_trade()
        print(f"[SYNC] İşlem eşleştirildi: {trade}")
        # Gerçek sistemde burada broker API çağrısı yapılır
        return trade
