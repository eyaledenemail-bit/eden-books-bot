import requests
from datetime import datetime

# --- הגדרות מערכת ---
# הדבק את המפתח שלך (זה שנגמר ב-kaTu) בין הגרשיים למטה
TOKEN = 'כאן_מדביקים_את_המפתח' 

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (עובד!)
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
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨ [Link]",
    "🇮🇱 הגיאומטריה המקודשת של הטבע היא המפה של הלב. 🌸 [Link]",
    # ... כאן יבואו שאר הפוסטים (כבר שמורים אצלי, נוסיף אותם בסוף)
]

def launch_and_detect():
    day_idx = (datetime.now().day - 1) % len(messages)
    media_idx = (datetime.now().day - 1) % len(media_links)
    
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    # שאילתה חכמה: מבקשת __typename כדי לדעת מה קורה במקרה של שגיאה
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
    
    print(f"--- משגר פוסט ליום {datetime.now().day} ---")
    
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
            
            # שליפת הנתונים מהתשובה
            result = res_data.get('data', {}).get('createPost', {})
            typename = result.get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה! פוסט {result['post']['id']} שוגר לערוץ {channel_id}")
            else:
                print(f"❓ ערוץ {channel_id} החזיר סטטוס: {typename}")
                print(f"פרטי התשובה: {res_data}")
                
        except Exception as e:
            print(f"⚠️ תקלה טכנית בערוץ {channel_id}: {e}")

if __name__ == "__main__":
    launch_and_detect()
