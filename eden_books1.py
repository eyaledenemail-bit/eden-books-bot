import requests
from datetime import datetime

# --- הגדרות מערכת (סופי) ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu
ORG_ID = '699ffcd6c130d9cd2ddc81cd' # מזהה הארגון שלך
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

# --- בנק הודעות (30 יום) ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Ready for the journey home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Listo para el viaje a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨ [קישור]\n🇺🇸 Beyond time and space. 🌌 [Link]\n🇪🇸 Más allá del tiempo. ❤️ [Link]",
    "🇮🇱 הגיאומטריה המקודשת של הטבע. 🌸 [קישור]\n🇺🇸 Sacred geometry. 🌸 [Link]\n🇪🇸 La geometría sagrada. ❤️ [Link]",
    "🇮🇱 הזמן אינו אויב, הוא הכלי לגדילה. ⏳ [קישור]\n🇺🇸 Time is a tool for growth. ⏳ [Link]\n🇪🇸 El tiempo es crecimiento. ❤️ [Link]",
    "🇮🇱 האור בשמים הוא רק קצה הקרחון. ☀️ [קישור]\n🇺🇸 Light is the tip of the iceberg. 🌌 [Link]\n🇪🇸 La luz es la punta del iceberg. ❤️ [Link]",
    "🇮🇱 שלוש הכוחות של הכלי המקודש. 💎 [קישור]\n🇺🇸 Three powers of the Sacred Vessel. 💎 [Link]\n🇪🇸 Los tres poderes de la Vasija. ❤️ [Link]",
    "🇮🇱 הנשמה זורמת בנהר של אהבה. 🌊 [קישור]\n🇺🇸 The soul flows in love. 🌊 [Link]\n🇪🇸 El alma fluye en amor. ❤️ [Link]",
    "🇮🇱 איחוד המלך והמלכה. 👑 [קישור]\n🇺🇸 Union of King and Queen. 👑 [Link]\n🇪🇸 Unión del Rey y la Reina. ❤️ [Link]",
    "🇮🇱 כל נשמה היא יהלום נדיר. 💎 [קישור]\n🇺🇸 Every soul is a diamond. 💎 [Link]\n🇪🇸 Cada alma es un diamante. ❤️ [Link]",
    "🇮🇱 גאולה מתחילה בחסד. 🕊️ [קישור]\n🇺🇸 Redemption starts with kindness. 🕊️ [Link]\n🇪🇸 La redención nace de la bondad. ❤️ [Link]",
    "🇮🇱 אתם האלמנט החמישי. 🔥 [קישור]\n🇺🇸 You are the fifth element. 🔥 [Link]\n🇪🇸 Eres el quinto elemento. ❤️ [Link]",
    "🇮🇱 הלוחם בוחר באהבה. ⚔️ [קישור]\n🇺🇸 The warrior chooses love. ⚔️ [Link]\n🇪🇸 El guerrero elige el amor. ❤️ [Link]",
    "🇮🇱 הנשמה זוכרת את מקורה. 🌌 [קישור]\n🇺🇸 The soul remembers its home. 🌌 [Link]\n🇪🇸 El alma recuerda su origen. ❤️ [Link]",
    "🇮🇱 תפילה היא גשר למלכות. 🙏 [קישור]\n🇺🇸 Prayer is a bridge. 🙏 [Link]\n🇪🇸 La oración es un puente. ❤️ [Link]",
    "🇮🇱 העולם נוצר מאהבה אליכם. ❤️ [קישור]\n🇺🇸 The world was made for you. ❤️ [Link]\n🇪🇸 El mundo se creó por amor. ❤️ [Link]",
    "🇮🇱 האות א' - תחילת הכל. 🌀 [קישור]\n🇺🇸 Aleph - the beginning. 🌀 [Link]\n🇪🇸 Alef - el principio. ❤️ [Link]",
    "🇮🇱 ממלכת המלכים שמעבר לשמש. ✨ [קישור]\n🇺🇸 Kingdom beyond the sun. ✨ [Link]\n🇪🇸 El Reino más allá del sol. ❤️ [Link]",
    "🇮🇱 האלמנט החמישי בתוככם. 🔥 [קישור]\n🇺🇸 Fifth element is within. 🔥 [Link]\n🇪🇸 El quinto elemento está en ti. ❤️ [Link]",
    "🇮🇱 פעולה היא זרע בבריאה. 🌱 [קישור]\n🇺🇸 Action is a seed. 🌱 [Link]\n🇪🇸 La acción es una semilla. ❤️ [Link]",
    "🇮🇱 הנשמה מחפשת את דרכה. 🌊 [קישור]\n🇺🇸 Soul seeks its way. 🌊 [Link]\n🇪🇸 El alma busca su camino. ❤️ [Link]",
    "🇮🇱 האור הגנוז בפנים. 🕯️ [קישור]\n🇺🇸 Hidden light within. 🕯️ [Link]\n🇪🇸 La luz oculta interior. ❤️ [Link]",
    "🇮🇱 ירושלים - שער העולמות. 🏰 [קישור]\n🇺🇸 Jerusalem - gate of worlds. 🏰 [Link]\n🇪🇸 Jerusalén - puerta de mundos. ❤️ [Link]",
    "🇮🇱 אהבה הקימה את העולם. ❤️ [קישור]\n🇺🇸 Love built the world. ❤️ [Link]\n🇪🇸 El amor construyó el mundo. ❤️ [Link]",
    "🇮🇱 הקשיבו לשקט. 🤫 [קישור]\n🇺🇸 Listen to the silence. 🤫 [Link]\n🇪🇸 Escucha el silencio. ❤️ [Link]",
    "🇮🇱 תפקידכם בתיקון העולם. ✨ [קישור]\n🇺🇸 Your role in repair. ✨ [Link]\n🇪🇸 Tu papel en la reparación. ❤️ [Link]",
    "🇮🇱 עולם חסד ייבנה. 🤝 [קישור]\n🇺🇸 A world of kindness. 🤝 [Link]\n🇪🇸 Un mundo de bondad. ❤️ [Link]",
    "🇮🇱 האור שלכם נצחי. 🌟 [קישור]\n🇺🇸 Your light is eternal. 🌟 [Link]\n🇪🇸 Tu luz es eterna. ❤️ [Link]",
    "🇮🇱 השכינה שוכנת באהבה. 🕊️ [קישור]\n🇺🇸 Divine Presence is in love. 🕊️ [Link]\n🇪🇸 La Presencia Divina es amor. ❤️ [Link]",
    "🇮🇱 המוות הוא דלת למסע. 🚪 [קישור]\n🇺🇸 Death is a door. 🚪 [Link]\n🇪🇸 La muerte es una puerta. ❤️ [Link]",
    "🇮🇱 הגאולה רק מתחילה. ✨ [קישור]\n🇺🇸 Redemption is beginning. ✨ [Link]\n🇪🇸 La redención comienza. ❤️ [Link]"
]

def launch_final():
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    # תיקון המוטציה: מבקשים 'post { id }' במקום 'success'
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        post {
          id
        }
      }
    }
    """
    
    print(f"--- משגר פוסט ליום {datetime.now().day} ---")
    
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
            # בודקים אם חזר ID של פוסט
            if 'data' in res_data and res_data['data']['createPost'].get('post'):
                post_id = res_data['data']['createPost']['post']['id']
                print(f"✅ הצלחה! פוסט {post_id} עלה לערוץ {channel_id}")
            else:
                print(f"❌ שגיאה בערוץ {channel_id}: {res_data}")
        except Exception as e:
            print(f"⚠️ תקלה טכנית: {e}")

if __name__ == "__main__":
    launch_final()
