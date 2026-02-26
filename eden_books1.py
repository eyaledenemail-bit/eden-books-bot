import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads
]

# נשתמש בתמונה אחת פשוטה לבדיקה (JPG) כדי לראות אם פייסבוק מאשרת
TEST_IMAGE = "https://raw.githubusercontent.com/eyaledenemail-bit/eden-books-bot/main/cover.jpg" 

messages = [
    "🇮🇱 בדיקת מערכת: כוח החיים - הגאולה. ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%9ה/",
]

def launch_image_test():
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
    
    print(f"--- מריץ בדיקת תמונות (Image Test) ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": messages[0],
                "schedulingType": "automatic",
                "mode": "shareNow",
                "assets": {
                    "images": [{"url": TEST_IMAGE}] # שימוש ב-images במקום videos
                }
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            typename = result.get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {channel_id}!")
            else:
                print(f"❌ ערוץ {channel_id} עדיין מסרב. סטטוס: {typename}")
        except Exception as e:
            print(f"⚠️ תקלה: {e}")

if __name__ == "__main__":
    launch_image_test()
