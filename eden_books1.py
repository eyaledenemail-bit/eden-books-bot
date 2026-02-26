import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads
]

# פוסט פשוט מאוד ללא קישורים או תמונות
test_message = "בדיקת מערכת: כוח החיים - הגאולה. יום נפלא לכולם! ✨"

def launch_clean_test():
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
    
    print(f"--- מריץ בדיקת טקסט נקי (Text-Only Test) ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": test_message,
                "schedulingType": "automatic",
                "mode": "shareNow"
                # הסרנו לגמרי את ה-assets (המדיה)
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            typename = result.get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {channel_id}! הפוסט באוויר.")
            else:
                print(f"❌ ערוץ {channel_id} עדיין מסרב. סטטוס: {typename}")
                print(f"   פירוט מהשרת: {res_data}")
        except Exception as e:
            print(f"⚠️ תקלה טכנית: {e}")

if __name__ == "__main__":
    launch_clean_test()
