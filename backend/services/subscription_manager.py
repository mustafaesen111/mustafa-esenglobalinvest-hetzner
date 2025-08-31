# Abonelik kontrol servisi
# Bu dosya, kullanıcıların abonelik durumlarını kontrol eden, işlem yetkilerini yöneten ve sistemin abonelik mantığını sabit bir şekilde uygulayan modüldür.
# Mimari Sabitliği Sağlayan Unsurlar:
# Sabit veri yapısı: user_subscription_data sözlük formatında beklenir.
# Sabit plan kontrolü: free, standard, premium planları sabitlenmiştir.
# Sabit iş akışı: Aktiflik kontrolü → plan kontrolü → işlem yetkisi → limit belirleme.
# Bağımsız yapı: Veritabanı veya dış sistemlere bağlı olmadan çalışır.
# Bu modül, copy-trade işlemlerinin kullanıcı bazlı kontrolünü sağlar. Örneğin bir kullanıcı “free” planındaysa işlem yapamaz, “standard” ise günde 5 işlem yapabilir. 
# Kod sabit kaldığı sürece sistem büyüse bile bu mantık değişmez.
python
class SubscriptionManager:
    def __init__(self, user_subscription_data):
        """
        user_subscription_data: dict → {'user_id': 'abc123', 'plan': 'premium', 'active': True}
        """
        self.subscription = user_subscription_data

    def is_active(self):
        return self.subscription.get("active", False)

    def get_plan(self):
        return self.subscription.get("plan", "free")

    def can_copy_trade(self):
        plan = self.get_plan()
        if not self.is_active():
            return False
        return plan in ["standard", "premium"]

    def get_trade_limit(self):
        plan = self.get_plan()
        if plan == "free":
            return 0
        elif plan == "standard":
            return 5
        elif plan == "premium":
            return 20
        return 0
