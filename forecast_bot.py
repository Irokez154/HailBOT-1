import os
from telegram import Bot
from datetime import datetime

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID")

def generate_forecast_text():
    today = datetime.utcnow().strftime("%d.%m.%Y")
    return f"""📅 Прогноз града по США на ближайшие 3 дня (сгенерировано {today})

Техас
17 мая — Даллас — размер града: 5 см — дилеров: 85
17 мая — Арлингтон — размер града: 4 см — дилеров: 23

Оклахома
17 мая — Оклахома-Сити — размер града: 6 см — дилеров: 15
17 мая — Норман — размер града: 5 см — дилеров: 6

📌 Отчет по прошедшему граду за предыдущие два дня (15–16 мая 2025 года)

Техас
15 мая — Форт-Уэрт — размер града: 3 см — дилеров: 52
16 мая — Уэйко — размер града: 2 см — дилеров: 11
"""

def send_forecast():
    bot = Bot(token=TELEGRAM_TOKEN)
    text = generate_forecast_text()
    bot.send_message(chat_id=TELEGRAM_USER_ID, text=text)

if __name__ == "__main__":
    send_forecast()