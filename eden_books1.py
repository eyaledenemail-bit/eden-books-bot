import requests
from datetime import datetime

# --- הגדרות מערכת ---
# הדבק כאן את המפתח שלך (זה שנגמר ב-kaTu)
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' 

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (כבר עובד!)
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
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%9ה/\n🇺🇸 Ready for the journey home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Listo para el viaje a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨",
    "🇮🇱 הגיאומטריה המקודשת של הטבע. 🌸",
    "🇮🇱 הזמן אינו אויב, הוא הכלי לגדילה. ⏳",
    "🇮🇱 האור בשמים הוא רק קצה הקרחון. ☀️",
    "🇮🇱 שלוש הכוחות של הכלי המקודש. 💎",
    "🇮🇱 הנשמה זורמת בנהר של אהבה. 🌊",
    "🇮🇱 איחוד המלך והמלכה. 👑",
    "🇮🇱 כל נשמה היא יהלום נדיר. 💎",
    "🇮🇱 גאולה מתחילה בחסד. 🕊️",
    "🇮🇱 אתם האלמנט החמישי. 🔥",
    "🇮🇱 הלוחם בוחר באהבה. ⚔️",
    "🇮🇱 הנשמה זוכרת את מקורה. 🌌",
    "🇮🇱 תפילה היא גשר למלכות. 🙏",
    "🇮🇱 העולם נוצר מאהבה אליכם. ❤️",
    "🇮🇱 האות א' - תחילת הכל. 🌀",
    "🇮🇱 ממלכת המלכים שמעבר לשמש. ✨",
    "🇮🇱 האלמנט החמישי בתוככם. 🔥",
    "🇮🇱 פעולה היא זרע בבריאה. 🌱",
    "🇮🇱 הנשמה מחפשת את דרכה. 🌊",
    "🇮🇱 האור הגנוז בפנים. 🕯️",
    "🇮🇱 ירושלים - שער העולמות. 🏰",
    "🇮🇱 אהבה הקימה את העולם. ❤️",
    "🇮🇱 הקשיבו לשקט. 🤫",
    "🇮🇱 תפקידכם בתיקון העולם. ✨",
    "🇮🇱 עולם חסד ייבנה. 🤝",
    "🇮🇱 האור שלכם נצחי. 🌟",
    "🇮🇱 השכינה שוכנת באהבה. 🕊️",
    "🇮🇱 המוות הוא דלת למסע. 🚪",
    "🇮🇱 הגאולה רק מתחילה. ✨"
]

def launch_campaign():
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
          post { id }
        }
      }
    }
    """
    
    print(f"--- משגר קמפיין יומי: יום {datetime.now().day} ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": messages[day_idx],
                "schedulingType": "automatic",
                "mode": "shareNow",
                "assets": {
                    "videos": [{"url": media_links[media_idx]}]
                }
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            typename = result.get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה! פוסט {result['post']['id']} שוגר לערוץ {channel_id}")
            else:
                print(f"❓ ערוץ {channel_id} החזיר סטטוס: {typename}")
                if typename == 'UnexpectedError':
                    print("   טיפ: פייסבוק/אינסטגרם לעיתים דורשות העלאת וידאו ידנית או פורמט אחר.")
        except Exception as e:
            print(f"⚠️ תקלה טכנית בערוץ {channel_id}: {e}")

if __name__ == "__main__":
    launch_campaign()
