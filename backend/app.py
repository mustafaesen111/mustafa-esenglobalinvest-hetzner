# backend/app.py
# Sabit FastAPI yapısı: app.py dosyası modüler route’ları sabit prefix’lerle bağlar.
# Sabit endpoint mantığı: Her route kendi dosyasında, tek sorumluluk ilkesine uygun.
# Sabit veri formatı: JSON çıktılar standart yapıda döner.
# Sabit genişleme yöntemi: Yeni route’lar eklenebilir ama mevcut yapı değişmez.
python
from fastapi import FastAPI
from backend.routes import home, portfolio, rankings, copytrade

app = FastAPI(title="Copy Trade Platform API")

# Sabit route kayıtları
app.include_router(home.router, prefix="/home")
app.include_router(portfolio.router, prefix="/portfolio")
app.include_router(rankings.router, prefix="/rankings")
app.include_router(copytrade.router, prefix="/copytrade")

@app.get("/")
def root():
    return {"message": "Copy Trade Platform API çalışıyor."}
