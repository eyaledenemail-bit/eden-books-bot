import requests
from datetime import datetime

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'
PROFILE_IDS = ['69a00b534be271803d6c88c4', '69a00b894be271803d6c8938', '69a00cd24be271803d6c9595']

# רשימת המדיה שלך (קישורים ישירים)
media_links = [
    "https://drive.google.com/uc?export=download&id=1yUzXKQIFDePnNuTNhaVj6c68sdnlK8SN",
    "https://drive.google.com/uc?export=download&id=1apuf0UzMEQxZxudid0k0D4jLq1CnN_ap",
    "https://drive.google.com/uc?export=download&id=1H4IDzt683V8MBaWgEIpbAmO4JPTJFi7W",
    "https://drive.google.com/uc?export=download&id=1SqJI7NsEjba54C4EWO5gZlvnvNucwJgr",
    "https://drive.google.com/uc?export=download&id=1qr9PrYh5j057vGD9MY7HX1UwXlRe2o_W",
    "https://drive.google.com/uc?export=download&id=1YDtgOF5AN9FDrueujH_s0mZilA-TSizq",
    "https://drive.google.com/uc?export=download&id=1ZUCC3UPJCf0MiwG9PY_vSr8c_24Ki2aG",
    "https://drive.google.com/uc?export=download&id=1AeaQ_pEqqzuxwSQD9qPyWKZiCUqVAaHg",
    "https://drive.google.com/uc?export=download&id=1D2G65cEAVfSlNAiLK1sksK6w_u0yugwg",
    "https://drive.google.com/uc?export=download&id=1z-7viMXR-HT_Y413gA1Zk_Z6QKzSsqXQ"
]

# בנק הודעות ל-30 יום
messages = [
    "🇮🇱 השיבה הביתה - מסע למקור הנשמה. ✨ nivbook.co.il/product/כוח-החיים-הגאולה/\n🇺🇸 Return Home - A journey to the source. 🌌 amzn.to/3vX\n🇪🇸 Regreso al Hogar - Un viaje al origen. ❤️ amzn.to/3yZ",
    "🇮🇱 פורטל לאינסוף - גלו מה מחכה מעבר לשמש. ☀️ nivbook.co.il/product/כוח-החיים-הגאולה/\n🇺🇸 Portal to Infinity - What lies beyond the sun? 🌌 amzn.to/3vX\n🇪🇸 Portal al Infinito - ¿Qué hay más allá del sol? ❤️ amzn.to/3yZ",
    "🇮🇱 פרח החיים - הגיאומטריה של הבריאה. 🌸 nivbook.co.il/product/כוח-החיים-הגאולה/\n🇺🇸 The Flower of Life - Sacred geometry. 🌸 amzn.to/3vX\n🇪🇸 La Flor de la Vida - Geometría sagrada. ❤️ amzn.to/3yZ",
    # ניתן להוסיף כאן עוד 27 שורות באותו פורמט
]

def post_daily():
    day = (datetime.now().day - 1) % len(messages)
    m_index = (datetime.now().day - 1) % len(media_links)
    
    data = {
        'access_token': TOKEN,
        'profile_ids[]': PROFILE_IDS,
        'text': messages[day],
        'media[video]': media_links[m_index],
        'shorten': 'false'
    }
    r = requests.post("https://api.bufferapp.com/1/updates/create.json", data=data)
    print(r.json())

if __name__ == "__main__":
    post_daily()