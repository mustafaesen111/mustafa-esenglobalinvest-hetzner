# backend/app.py
python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_home_data():
    return {
        "status": "ok",
        "message": "Anasayfa verileri başarıyla alındı.",
        "features": [
            "Copy Trade işlemleri",
            "Portföy görüntüleme",
            "Hisse puanlamaları",
            "Abonelik yönetimi"
        ]
}
