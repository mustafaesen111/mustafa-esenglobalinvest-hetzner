# Mimari Sabitliği Sağlayan Unsurlar:
# Sabit görev modeli: add_task() ile görev eklenir, start() ile başlatılır.
# Sabit zamanlama mantığı: Her görev belirli aralıklarla çalışır.
# Sabit iş akışı: Görevleri sırayla çalıştırır, hata yönetimi içerir.
# Bağımsız yapı: Dış sistemlerden etkilenmeden çalışır, sadece fonksiyon alır.
#Bu yapı sayesinde sistemin belirli aralıklarla otomatik işlem yapması sağlanır. Örneğin her 60 saniyede bir copy-trade eşleşmesi kontrol edilebilir.
python
import time
import threading

class Scheduler:
    def __init__(self, interval_seconds=60):
        """
        interval_seconds: Görevlerin ne sıklıkla çalışacağını belirler (varsayılan: 60 saniye)
        """
        self.interval = interval_seconds
        self.tasks = []
        self.running = False

    def add_task(self, task_func):
        """
        task_func: Zamanlanmış olarak çalıştırılacak fonksiyon
        """
        self.tasks.append(task_func)

    def _run_tasks(self):
        while self.running:
            print(f"[SCHEDULER] {len(self.tasks)} görev çalıştırılıyor...")
            for task in self.tasks:
                try:
                    task()
                except Exception as e:
                    print(f"[SCHEDULER] Görev hatası: {e}")
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self._run_tasks, daemon=True)
            thread.start()
            print("[SCHEDULER] Zamanlayıcı başlatıldı.")

    def stop(self):
        self.running = False
        print("[SCHEDULER] Zamanlayıcı durduruldu.")
