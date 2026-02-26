import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (עובד!)
]

# פוסט לבדיקה - שים לב שהוספנו saveToDraft
test_message = "בדיקת מערכת: כוח החיים - הגאולה. האור יוצא לדרך! ✨"

def launch_draft_test():
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
    
    print(f"--- מריץ בדיקת טיוטה (Save to Draft) ---")
    
    for channel_id in CHANNEL_IDS:
        variables = {
            "input": {
                "channelId": channel_id,
                "text": test_message,
                "schedulingType": "automatic",
                "mode": "addToQueue", # שינוי ל"הוספה לתור" במקום פרסום מיידי
                "saveToDraft": True,   # פקודה לשמור כטיוטה
                "source": "api"        # ציון המקור
            }
        }
        
        try:
            response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
            res_data = response.json()
            result = res_data.get('data', {}).get('createPost', {})
            typename = result.get('__typename')
            
            if typename == 'PostActionSuccess':
                print(f"✅ הצלחה בערוץ {channel_id}! הפוסט נשמר כטיוטה.")
            else:
                print(f"❌ ערוץ {channel_id} עדיין מסרב. סטטוס: {typename}")
                print(f"   תשובת השרת: {res_data}")
        except Exception as e:
            print(f"⚠️ תקלה טכנית: {e}")

if __name__ == "__main__":
    launch_draft_test()
