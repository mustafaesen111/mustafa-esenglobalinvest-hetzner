# Admin işlem mantığı. Bu dosya, admin kullanıcılarının özel işlem mantığını sabit bir yapıyla yönetmek üzere tasarlanmıştır. Sistem büyüse bile bu dosya, admin işlemlerinin temelini değiştirmeden korur.
# Mimari Sabitliği Sağlayan Unsurlar:
# Sabit işlem modeli: execute_admin_trade, override_trade, cancel_trade fonksiyonları sabit.
# Broker bağımsızlığı: Her broker client ile çalışabilir, kod değişmez.
# Sabit iş akışı: Admin tetikler → işlem oluşturulur → opsiyonel override veya iptal yapılır.
# Genişlemeye açık ama değişmeye gerek duymaz: Yeni brokerlar eklense bile bu yapı korunur.
python
class AdminExecutor:
    def __init__(self, broker_client):
        """
        broker_client: IBKRClient, OANDAClient veya benzeri broker nesnesi
        """
        self.client = broker_client

    def execute_admin_trade(self, symbol, action, quantity):
        """
        Admin tarafından manuel işlem tetikleme
        """
        trade = {
            "symbol": symbol,
            "action": action,
            "quantity": quantity
}
        print(f"[ADMIN] Manuel işlem tetiklendi: {trade}")
        # Gerçek sistemde burada broker API çağrısı yapılır
        return trade

    def override_trade(self, original_trade, new_quantity):
        """
        Admin tarafından işlem miktarını geçersiz kılma
        """
        overridden = original_trade.copy()
        overridden["quantity"] = new_quantity
        print(f"[ADMIN] İşlem override edildi: {overridden}")
        return overridden

    def cancel_trade(self, trade_id):
        """
        Admin tarafından işlem iptali (simülasyon)
        """
        print(f"[ADMIN] İşlem iptal edildi: trade_id={trade_id}")
        # Gerçek sistemde burada iptal API çağrısı olur
        return {"status": "cancelled", "trade_id": trade_id}
