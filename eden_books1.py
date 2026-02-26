import requests

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'
PROFILE_IDS = ['69a00b534be271803d6c88c4', '69a00b894be271803d6c8938', '69a00cd24be271803d6c9595']

def test_connection():
    url = "https://api.bufferapp.com/1/updates/create.json"
    
    for profile_id in PROFILE_IDS:
        print(f"בודק חיבור לפרופיל: {profile_id}")
        payload = {
            'access_token': TOKEN,
            'profile_ids[]': [profile_id],
            'text': "בדיקת מערכת אוטומטית - כוח החיים הגאולה ✨",
            'shorten': 'false'
        }
        
        response = requests.post(url, data=payload)
        print(f"סטטוס: {response.status_code}")
        print(f"תגובה: {response.text}")

if __name__ == "__main__":
    test_connection()
