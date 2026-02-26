import requests
from datetime import datetime

# --- הגדרות מערכת (מעודכן למערכת ה-Beta) ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu
ORG_ID = '699ffcd6c130d9cd2ddc81cd'
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

# --- בנק הודעות ל-30 יום ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה, אל מקור הנשמה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Are you ready for the journey back home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Estás listo para el viaje de regreso a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לעולם שכולו אור. ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Beyond time and space. 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 Más allá del tiempo y el espacio. ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 הגיאומטריה המקודשת של הטבע היא המפה של הלב. 🌸 https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Sacred geometry is the map of the heart. 🌸 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 La geometría sagrada es el mapa del corazón. ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 הזמן אינו אויב, הוא הכלי שלנו לגדילה רגשית עמוקה. ⏳ [Link]\n🇺🇸 Time is our tool for deep emotional growth. ⏳ [Link]\n🇪🇸 El tiempo es nuestra herramienta de crecimiento. ❤️ [Link]",
    "🇮🇱 האור שאתם רואים בשמים הוא רק קצה הקרחון של המציאות. ☀️ [Link]\n🇺🇸 The light you see is just the tip of the iceberg. 🌌 [Link]\n🇪🇸 La luz que ves es solo la punta del iceberg. ❤️ [Link]",
    "🇮🇱 שלוש הכוחות של הכלי המקודש מחכים להתגלות בתוככם. 💎 [Link]\n🇺🇸 The three powers of the Sacred Vessel. 💎 [Link]\n🇪🇸 Los tres poderes de la Vasija Sagrada. ❤️ [Link]",
    "🇮🇱 הנשמה זורמת בנהר נצחי של אהבה ובריאה. 🌊 [Link]\n🇺🇸 The soul flows in an eternal river of love. 🌊 [Link]\n🇪🇸 El alma fluye en un río eterno de amor. ❤️ [Link]",
    "🇮🇱 סיפור האהבה העתיק ביותר ביקום – איחוד המלך והמלכה. 👑 [Link]\n🇺🇸 The oldest love story – the King and Queen. 👑 [Link]\n🇪🇸 La historia de amor más antigua. ❤️ [Link]",
    "🇮🇱 כל נשמה היא יהלום נדיר בכתרו של הבורא. 💎 [Link]\n🇺🇸 Every soul is a rare diamond. 💎 [Link]\n🇪🇸 Cada alma es un diamante raro. ❤️ [Link]",
    "🇮🇱 גאולה אישית מתחילה במעשה אחד קטן של חסד. 🕊️ [Link]\n🇺🇸 Personal redemption begins with kindness. 🕊️ [Link]\n🇪🇸 La redención comienza con la bondad. ❤️ [Link]",
    "🇮🇱 אש, אדמה, אוויר ומים – ואתם, האלמנט החמישי. 🔥 [Link]\n🇺🇸 Fire, Earth, Air, and Water – you are the fifth. 🔥 [Link]\n🇪🇸 Fuego, Tierra, Aire y Agua – eres el quinto. ❤️ [Link]",
    "🇮🇱 הלוחם האמיתי הוא זה שכובש את פחדיו ובוחר באהבה. ⚔️ [Link]\n🇺🇸 The true warrior conquers fear and chooses love. ⚔️ [Link]\n🇪🇸 El verdadero guerrero elige el amor. ❤️ [Link]",
    "🇮🇱 הנשמה שלכם זוכרת את המקום ממנו באה. 🌌 [Link]\n🇺🇸 Your soul remembers where it came from. 🌌 [Link]\n🇪🇸 Tu alma recuerda de dónde vino. ❤️ [Link]",
    "🇮🇱 תפילה היא גשר בין הלב האנושי לממלכות העליונות. 🙏 [Link]\n🇺🇸 Prayer is a bridge to the higher realms. 🙏 [Link]\n🇪🇸 La oración es un puente a los reinos superiores. ❤️ [Link]",
    "🇮🇱 העולם נוצר מתוך אהבה אינסופית אליכם. ❤️ [Link]\n🇺🇸 The world was created out of infinite love for you. ❤️ [Link]\n🇪🇸 El mundo fue creado por amor a ti. ❤️ [Link]",
    "🇮🇱 האות א' - תחילת הכל, האחדות שבין הבורא לבריאה. 🌀 [Link]\n🇺🇸 Aleph - the beginning of everything. 🌀 [Link]\n🇪🇸 Alef - el principio de todo. ❤️ [Link]",
    "🇮🇱 הצצה לממלכת המלכים שמעבר לשמש. שם הכל התחיל. ✨ [Link]\n🇺🇸 A glimpse into the Kingdom beyond the sun. ✨ [Link]\n🇪🇸 Una mirada al Reino más allá del sol. ❤️ [Link]",
    "🇮🇱 האם אתם מכירים את האלמנט החמישי? הוא נמצא בתוככם. 🔥 [Link]\n🇺🇸 Do you know the fifth element? It's within you. 🔥 [Link]\n🇪🇸 ¿Conoces el quinto elemento? Está en ti. ❤️ [Link]",
    "🇮🇱 כל פעולה שלכם היא זרע שנשתל בגן הבריאה. 🌱 [Link]\n🇺🇸 Every action is a seed in the garden of creation. 🌱 [Link]\n🇪🇸 Cada acción es una semilla de creación. ❤️ [Link]",
    "🇮🇱 כמו מים שזורמים לים, הנשמה תמיד מחפשת את דרכה. 🌊 [Link]\n🇺🇸 Like water to the sea, the soul seeks its way. 🌊 [Link]\n🇪🇸 Como el agua al mar, el alma busca su camino. ❤️ [Link]",
    "🇮🇱 האור הגנוז מחכה לאלו שמעזים להביט פנימה. 🕯️ [Link]\n🇺🇸 The hidden light awaits those who look within. 🕯️ [Link]\n🇪🇸 La luz oculta espera a quienes miran adentro. ❤️ [Link]",
    "🇮🇱 ירושלים היא שער רוחני לאיחוד העולמות. 🏰 [Link]\n🇺🇸 Jerusalem is a spiritual gate. 🏰 [Link]\n🇪🇸 Jerusalén es una puerta espiritual. ❤️ [Link]",
    "🇮🇱 אהבה היא האנרגיה שהקימה את העולם. ❤️ [Link]\n🇺🇸 Love is the energy that built the world. ❤️ [Link]\n🇪🇸 El amor es la energía que construyó el mundo. ❤️ [Link]",
    "🇮🇱 הבורא מדבר אליכם דרך השקט. האם אתם מקשיבים? 🤫 [Link]\n🇺🇸 The Creator speaks through the silence. 🤫 [Link]\n🇪🇸 El Creadור te habla en el silencio. ❤️ [Link]",
    "🇮🇱 לכל נשמה יש תפקיד ייחודי בתיקון העולם. ✨ [Link]\n🇺🇸 Every soul has a role in repairing the world. ✨ [Link]\n🇪🇸 Cada alma tiene un papel en la reparación. ❤️ [Link]",
    "🇮🇱 עולם חסד ייבנה. כל מעשה טוב מקרב את הגאולה. 🤝 [Link]\n🇺🇸 A world of kindness brings redemption closer. 🤝 [Link]\n🇪🇸 Un mundo de bondad acerca la redención. ❤️ [Link]",
    "🇮🇱 הגוף זמני, אבל האור שלכם נצחי. 🌟 [Link]\n🇺🇸 The body is temporary, but your light is eternal. 🌟 [Link]\n🇪🇸 El cuerpo es temporal, tu luz es eterna. ❤️ [Link]",
    "🇮🇱 השכינה שוכנת בכל מקום שבו יש אהבה ואמת. 🕊️ [Link]\n🇺🇸 The Divine Presence dwells where there is love. 🕊️ [Link]\n🇪🇸 La Presencia Divina mora en el amor. ❤️ [Link]",
    "🇮🇱 המוות הוא רק דלת לממלכה הבאה. המסע נמשך. 🚪 [Link]\n🇺🇸 Death is only a door. The journey continues. 🚪 [Link]\n🇪🇸 La muerte es solo una puerta al siguiente reino. ❤️ [Link]",
    "🇮🇱 סיימנו חודש של גילויים, אבל הגאולה רק מתחילה. ✨ [Link]\n🇺🇸 A month of discovery. Redemption begins. ✨ [Link]\n🇪🇸 Un mes de descubrimientos. Comienza la redención. ❤️ [Link]"
]

def launch_full_campaign():
    # בחירת פוסט ומדיה לפי היום בחודש (1-31)
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        success
      }
    }
    """
    
    print(f"--- משגר קמפיין יומי: יום {datetime.now().day} ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "organizationId": ORG_ID,
                "channelId": channel_id,
                "text": messages[day_idx],
                "media": {"video": media_links[media_idx]}
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            if res_data.get('data', {}).get('createPost', {}).get('success'):
                print(f"✅ הצלחה: הפוסט עלה לערוץ {channel_id}")
            else:
                print(f"❌ שגיאה בערוץ {channel_id}: {res_data}")
        except Exception as e:
            print(f"⚠️ תקלה טכנית: {e}")

if __name__ == "__main__":
    launch_full_campaign()
