import requests

# הדבק כאן את המפתח החדש שקיבלת בין הגרשיים
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def get_profile_ids():
    # שליחת המפתח כפרמטר בכתובת (הדרך הכי יציבה למנוע שגיאה 500)
    url = f"https://api.bufferapp.com/1/profiles.json?access_token={TOKEN}"
    
    print("--- בודק חיבור עם המפתח החדש ---")
    try:
        response = requests.get(url)
        print(f"סטטוס שרת: {response.status_code}")
        
        if response.status_code == 200:
            profiles = response.json()
            print("מעולה! המפתח עובד. הנה ה-IDs שלך (תעתיק אותם):")
            for p in profiles:
                # מדפיס את סוג הרשת ואת ה-ID כדי שנדע מה שייך למה
                print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
        else:
            print(f"שגיאה {response.status_code}: השרת של Buffer החזיר תשובה לא תקינה.")
            print(f"תוכן התשובה: {response.text}")
            
    except Exception as e:
        print(f"תקלה בחיבור האינטרנט: {e}")

if __name__ == "__main__":
    get_profile_ids()
