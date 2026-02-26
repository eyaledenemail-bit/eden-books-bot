import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'
CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads
]

# --- בנק מדיה (13 קבצים) ---
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
    "https://drive.google.com/uc?export=download&id=1z-7viMXR-HT_Y413gA1Zk_Z6QKzSsqXQ",
    "https://drive.google.com/uc?export=download&id=17FO7xqyctMsEdGBu3HH5QU92Nr5tJenZ",
    "https://drive.google.com/uc?export=download&id=1bdM-Cb3x2afG3YIMLsqEPWJk6seWHJLK",
    "https://drive.google.com/uc?export=download&id=16r8LEv57QBquxddCd6o89bpkhV0MSdAD"
]

# --- בנק הודעות ל-30 יום (מבוסס על הספר "כוח החיים") ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה, אל מקור הנשמה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Are you ready for the journey back home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Estás listo para el viaje de regreso a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לעולם שכולו אור. ✨ [קישור]\n🇺🇸 Beyond time and space, there is a gate to a world of light. 🌌 [Link]\n🇪🇸 Más allá del tiempo y el espacio, hay una puerta de luz. ❤️ [Link]",
    "🇮🇱 הגיאומטריה המקודשת של הטבע היא המפה של הלב. 🌸 [קישור]\n🇺🇸 Sacred geometry is the map of the heart. 🌸 [Link]\n🇪🇸 La geometría sagrada es el mapa del corazón. ❤️ [Link]",
    "🇮🇱 הזמן אינו אויב, הוא הכלי שלנו לגדילה רגשית עמוקה. ⏳ [קישור]\n🇺🇸 Time is our tool for deep emotional growth. ⏳ [Link]\n🇪🇸 El tiempo es nuestra herramienta de crecimiento. ❤️ [Link]",
    "🇮🇱 האור שאתם רואים בשמים הוא רק קצה הקרחון של המציאות. ☀️ [קישור]\n🇺🇸 The light you see is just the tip of the iceberg. 🌌 [Link]\n🇪🇸 La luz que ves es solo la punta del iceberg. ❤️ [Link]",
    "🇮🇱 שלוש הכוחות של הכלי המקודש מחכים להתגלות בתוככם. 💎 [קישור]\n🇺🇸 The three powers of the Sacred Vessel await you. 💎 [Link]\n🇪🇸 Los tres poderes de la Vasija Sagrada te esperan. ❤️ [Link]",
    "🇮🇱 הנשמה זורמת בנהר נצחי של אהבה ובריאה. 🌊 [קישור]\n🇺🇸 The soul flows in an eternal river of love. 🌊 [Link]\n🇪🇸 El alma fluye en un río eterno de amor. ❤️ [Link]",
    "🇮🇱 סיפור האהבה העתיק ביותר ביקום – איחוד המלך והמלכה. 👑 [קישור]\n🇺🇸 The oldest love story – the King and Queen. 👑 [Link]\n🇪🇸 La historia de amor más antigua – el Rey y la Reina. ❤️ [Link]",
    "🇮🇱 כל נשמה היא יהלום נדיר בכתרו של הבורא. 💎 [קישור]\n🇺🇸 Every soul is a rare diamond. 💎 [Link]\n🇪🇸 Cada alma es un diamante raro. ❤️ [Link]",
    "🇮🇱 גאולה אישית מתחילה במעשה אחד קטן של חסד. 🕊️ [קישור]\n🇺🇸 Personal redemption begins with kindness. 🕊️ [Link]\n🇪🇸 La redención comienza con la bondad. ❤️ [Link]",
    # ... (הקוד ימשיך להשתמש ב-30 הודעות אלו במחזוריות)
]

def post_to_buffer_v2():
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    # שאילתת יצירת פוסט (Mutation)
    mutation = """
    mutation CreateUpdate($input: CreateUpdateInput!) {
      createUpdate(input: $input) {
        success
        message
      }
    }
    """
    
    variables = {
        "input": {
            "channelIds": CHANNEL_IDS,
            "text": messages[day_idx],
            "media": {"video": media_links[media_idx]}
        }
    }
    
    print(f"--- שולח פוסט ליום {datetime.now().day} ---")
    response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
    print(f"סטטוס: {response.status_code}")
    print(f"תשובה: {response.json()}")

if __name__ == "__main__":
    post_to_buffer_v2()
