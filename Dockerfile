# Versiyon sabitleme: requirements.txt ile sağlandı
# Otomatik başlatma: restart: always ile container her zaman ayağa kalkar
# Log yönlendirme: volumes ve logging ayarları Promtail uyumlu
# Image versiyonlama: container_name: copytrade_api_v1 ile versiyon takibi kolay
dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

COPY..

ENV LOG_LEVEL=info

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
