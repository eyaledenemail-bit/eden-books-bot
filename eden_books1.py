import requests
from datetime import datetime

# --- הגדרות מערכת ---
# הדבק כאן את המפתח שלך (זה שנגמר ב-kaTu) בתוך הגרשיים
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' 

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (עובד!)
]

# --- בנק מדיה (13 קבצים מהגוגל דרייב) ---
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

# --- בנק הודעות משודרג (3 שפות + לינקים) ---
# הוספתי 3 וריאציות כדי שהפוסטים לא יהיו זהים כל יום
messages = [
    # וריאציה 1: השיבה הביתה
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ הספר \"כוח החיים - הגאולה\" הוא מפה רוחנית למסע חזרה אל הנשמה.\n🛒 לרכישה: https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%9ה/\n\n🇺🇸 Ready for the journey home? 🌌 \"The Power of Life - Redemption\" invites you to explore the secrets of the soul.\n🛒 Amazon: https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n\n🇪🇸 ¿Listo para el viaje a casa? ❤️ \"El Poder de la Vida - Redención\" te lleva a los secretos del alma.\n🛒 Amazon ES: https://www.amazon.es/dp/B0GNHN9X1T\n\n#כוחהחיים #גאולה #EyalEden #ThePowerOfLife",

    # וריאציה 2: סודות הממלכה
    "🇮🇱 הצצה אל מעבר לשמש... אל ממלכת המלכים העליונה. ✨ גלו את סודות הגיאומטריה המקודשת שבתוככם.\n🛒 לרכישה: https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%9ה/\n\n🇺🇸 A glimpse beyond the sun... to the Supreme Kingdom. ✨ Discover the secrets of sacred geometry within.\n🛒 Amazon: https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n\n🇪🇸 Una mirada más allá del sol... al Reino Supremo. ✨ Descubre los secretos de la geometría sagrada.\n🛒 Amazon ES: https://www.amazon.es/dp/B0GNHN9X1T\n\n#BookLaunch #Redemption #SpiritualJourney",

    # וריאציה 3: שלוש שפות, מסע אחד
    "🇮🇱 שלוש שפות. מסע אחד נצחי. ✨ \"כוח החיים - הגאולה\" עכשיו זמין לכל העולם. 🌍\n🛒 לרכישה: https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%9ה/\n\n🇺🇸 Three languages. One eternal journey. ✨ \"The Power of Life - Redemption\" is now available worldwide. 🌍\n🛒 Amazon: https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n\n🇪🇸 Tres idiomas. Un viaje eterno. ✨ \"El Poder de la Vida - Redención\" ya disponible en todo el mundo. 🌍\n🛒 Amazon ES: https://www.amazon.es/dp/B0GNHN9X1T\n\n#EyalEden #NewBook #LifePower"
]

def launch_production_campaign():
    # בחירת פוסט ומדיה לפי היום בחודש
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        __typename
        ... on PostActionSuccess { post { id } }
      }
    }
    """
    
    print(f"--- משגר קמפיין משודרג: יום {datetime.now().day} ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": messages[day_idx],
                "schedulingType": "automatic",
                "mode": "shareNow",
                "assets": { "videos": [{"url": media_links[media_idx]}] }
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            
            if result.get('__typename') == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {channel_id}!")
            else:
                print(f"❌ ערוץ {channel_id} לא פורסם (סטטוס: {result.get('__typename')})")
        except Exception as e:
            print(f"⚠️ שגיאה: {e}")

if __name__ == "__main__":
    launch_production_campaign()
