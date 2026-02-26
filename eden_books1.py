import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu
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
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨ [Link]",
    "🇮🇱 הגיאומטריה המקודשת של הטבע. 🌸 [Link]",
    "🇮🇱 הזמן אינו אויב, הוא הכלי לגדילה. ⏳ [Link]",
    "🇮🇱 האור בשמים הוא רק קצה הקרחון. ☀️ [Link]",
    "🇮🇱 שלוש הכוחות של הכלי המקודש. 💎 [Link]",
    "🇮🇱 הנשמה זורמת בנהר של אהבה. 🌊 [Link]",
    "🇮🇱 איחוד המלך והמלכה. 👑 [Link]",
    "🇮🇱 כל נשמה היא יהלום נדיר. 💎 [Link]",
    "🇮🇱 גאולה מתחילה בחסד. 🕊️ [Link]",
    "🇮🇱 אתם האלמנט החמישי. 🔥 [Link]",
    "🇮🇱 הלוחם בוחר באהבה. ⚔️ [Link]",
    "🇮🇱 הנשמה זוכרת את מקורה. 🌌 [Link]",
    "🇮🇱 תפילה היא גשר למלכות. 🙏 [Link]",
    "🇮🇱 העולם נוצר מאהבה אליכם. ❤️ [Link]",
    "🇮🇱 האות א' - תחילת הכל. 🌀 [Link]",
    "🇮🇱 ממלכת המלכים שמעבר לשמש. ✨ [Link]",
    "🇮🇱 האלמנט החמישי בתוככם. 🔥 [Link]",
    "🇮🇱 פעולה היא זרע בבריאה. 🌱 [Link]",
    "🇮🇱 הנשמה מחפשת את דרכה. 🌊 [Link]",
    "🇮🇱 האור הגנוז בפנים. 🕯️ [Link]",
    "🇮🇱 ירושלים - שער העולמות. 🏰 [Link]",
    "🇮🇱 אהבה הקימה את העולם. ❤️ [Link]",
    "🇮🇱 הקשיבו לשקט. 🤫 [Link]",
    "🇮🇱 תפקידכם בתיקון העולם. ✨ [Link]",
    "🇮🇱 עולם חסד ייבנה. 🤝 [Link]",
    "🇮🇱 האור שלכם נצחי. 🌟 [Link]",
    "🇮🇱 השכינה שוכנת באהבה. 🕊️ [Link]",
    "🇮🇱 המוות הוא דלת למסע. 🚪 [Link]",
    "🇮🇱 הגאולה רק מתחילה. ✨ [Link]"
]

def launch_final_automated():
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    # המוטציה המדויקת עם השדות שחילצנו
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post { id }
        }
      }
    }
    """
    
    print(f"--- משגר קמפיין אוטומטי ליום {datetime.now().day} ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": messages[day_idx],
                "schedulingType": "now", # מתוזמן לעכשיו
                "mode": "social",        # מצב רשתות חברתיות
                "assets": {
                    "video": {"url": media_links[media_idx]} # שימוש ב-assets במקום media
                }
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            
            if 'data' in res_data and res_data['data']['createPost']:
                print(f"✅ הצלחה! פוסט שוגר לערוץ {channel_id}")
            else:
                print(f"❌ שגיאה בערוץ {channel_id}: {res_data}")
        except Exception as e:
            print(f"⚠️ תקלה טכנית: {e}")

if __name__ == "__main__":
    launch_final_automated()
