import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (עובד!)
]

# --- בנק הודעות ל-30 יום (3 שפות + לינקים) ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://tinyurl.com/233mcy6n/\n🇺🇸 Ready for the journey home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Listo para el viaje a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨\n🇺🇸 Beyond time and space, there is a gate to light. 🌌\n🇪🇸 Más allá del tiempo y el espacio, hay una puerta a la luz. ❤️",
    "🇮🇱 הגיאומטריה המקודשת היא המפה של הלב. 🌸\n🇺🇸 Sacred geometry is the map of the heart. 🌸\n🇪🇸 La geometría sagrada es el mapa del corazón. ❤️",
    # (הקוד ימשיך להריץ את אלו בסבב של 30 יום)
]
while len(messages) < 30: messages.append(messages[0])

def launch():
    day = datetime.now().day
    msg = messages[(day-1) % len(messages)]
    # שימוש בתמונה יציבה שהוכחנו שעובדת ב-Threads
    img_url = "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=800&q=80"

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
    
    print(f"--- משגר קמפיין יום {day} ---")
    
    for cid in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": cid,
                "text": msg,
                "schedulingType": "automatic",
                "mode": "shareNow",
                "assets": {"images": [{"url": img_url}]}
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            typename = res_data.get('data', {}).get('createPost', {}).get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {cid}!")
            else:
                print(f"❌ ערוץ {cid} ממתין להגדרות ב-Buffer (סטטוס: {typename})")
        except Exception as e:
            print(f"⚠️ שגיאה: {e}")

if __name__ == "__main__":
    launch()
