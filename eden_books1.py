import requests
from datetime import datetime

# --- הגדרות מערכת ---
TOKEN = 'כאן_מדביקים_את_המפתח' # המפתח שנגמר ב-kaTu

CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads
]

# נשתמש בתמונה חיצונית סופר-יציבה לבדיקה
STABLE_IMAGE = "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=800&q=80"

def post_diagnostic(channel_id, text, image_url=None):
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
    
    variables = {
        "input": {
            "channelId": channel_id,
            "text": text,
            "schedulingType": "automatic",
            "mode": "shareNow"
        }
    }
    
    if image_url:
        variables["input"]["assets"] = {"images": [{"url": image_url}]}
        
    response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
    return response.json()

def run_diagnostic():
    print(f"--- בדיקת מערכת סופית: יום {datetime.now().day} ---")
    
    for cid in CHANNEL_IDS:
        print(f"\nבדיקת ערוץ {cid}:")
        
        # שלב א': בדיקת טקסט נקי
        print(f" 1. מנסה טקסט בלבד...")
        res_text = post_diagnostic(cid, "בדיקת טקסט - כוח החיים הגאולה ✨")
        if res_text.get('data', {}).get('createPost', {}).get('__typename') == 'PostActionSuccess':
            print(f" ✅ הצלחה בטקסט!")
        else:
            print(f" ❌ כישלון בטקסט: {res_text}")

        # שלב ב': בדיקת תמונה יציבה
        print(f" 2. מנסה תמונה יציבה...")
        res_img = post_diagnostic(cid, "בדיקת תמונה - כוח החיים הגאולה 📖", STABLE_IMAGE)
        if res_img.get('data', {}).get('createPost', {}).get('__typename') == 'PostActionSuccess':
            print(f" ✅ הצלחה בתמונה!")
        else:
            print(f" ❌ כישלון בתמונה: {res_img}")

if __name__ == "__main__":
    run_diagnostic()
