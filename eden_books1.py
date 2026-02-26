import requests

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'

def debug_buffer():
    # הגדרת הכותרות עם המפתח שלך
    headers = {'Authorization': f'Bearer {TOKEN}'}
    
    print("--- שלב 1: בדיקת תקינות המפתח (User Info) ---")
    user_url = "https://api.bufferapp.com/1/user.json"
    user_res = requests.get(user_url, headers=headers)
    print(f"סטטוס משתמש: {user_res.status_code}")
    
    if user_res.status_code == 200:
        print("המפתח תקין! ברוך הבא, " + user_res.json().get('name', 'משתמש'))
        
        print("\n--- שלב 2: משיכת מזהי הפרופילים (Profile IDs) ---")
        profiles_url = "https://api.bufferapp.com/1/profiles.json"
        prof_res = requests.get(profiles_url, headers=headers)
        
        if prof_res.status_code == 200:
            profiles = prof_res.json()
            for p in profiles:
                print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
        else:
            print(f"שגיאה במשיכת פרופילים: {prof_res.status_code}")
            print(prof_res.text)
    else:
        print("נראה שיש בעיה במפתח הגישה (Token).")
        print(f"תגובת השרת: {user_res.text}")

if __name__ == "__main__":
    debug_buffer()
