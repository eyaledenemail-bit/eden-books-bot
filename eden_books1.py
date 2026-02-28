import requests
from datetime import datetime

# --- הגדרות מערכת ---
# הדבק כאן את המפתח שלך (זה שנגמר ב-kaTu)
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' 

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads
]

# --- בנק תמונות (JPG) ---
# כרגע נשתמש בתמונת העטיפה מה-GitHub שלך כגיבוי
image_links = [
    "https://raw.githubusercontent.com/eyaledenemail-bit/eden-books-bot/main/cover.jpg"
]

# --- בנק הודעות ל-30 יום (עברית, אנגלית, ספרדית) ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://tinyurl.com/233mcy6n/\n🇺🇸 Ready for the journey home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Listo para el viaje a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨\n🇺🇸 Beyond time and space, there is a gate to light. 🌌\n🇪🇸 Más allá del tiempo y el espacio, hay una puerta a la luz. ❤️",
    "🇮🇱 הגיאומטריה המקודשת היא המפה של הלב. 🌸\n🇺🇸 Sacred geometry is the map of the heart. 🌸\n🇪🇸 La geometría sagrada es el mapa del corazón. ❤️"
]
# השלמה ל-30 יום במידה וחסר
while len(messages) < 30:
    messages.append(messages[0])

def launch_image_campaign():
    day = datetime.now().day
    msg_idx = (day - 1) % len(messages)
    img_idx = (day - 1) % len(image_links)
    
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
    
    print(f"--- משגר קמפיין תמונות ליום {day} ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": messages[msg_idx],
                "schedulingType": "automatic",
                "mode": "shareNow",
                "assets": {
                    "images": [{"url": image_links[img_idx]}]
                }
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            
            if result.get('__typename') == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {channel_id}!")
            else:
                print(f"❌ ערוץ {channel_id} נכשל. סטטוס: {result.get('__typename')}")
                print(f"פרטים: {res_data}")
        except Exception as e:
            print(f"⚠️ שגיאה טכנית בערוץ {channel_id}: {e}")

if __name__ == "__main__":
    launch_image_campaign()
