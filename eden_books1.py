import requests

# וודא שאתה מעתיק לכאן את ה-Access Token (זה שמתחיל ב-1/)
RAW_TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def final_test():
    # ניקוי רווחים מיותרים שעלולים להיכנס בהעתקה
    token = RAW_TOKEN.strip()
    
    # שימוש בכתובת המשתמש - הבדיקה הכי בסיסית שיש
    url = f"https://api.bufferapp.com/1/user.json?access_token={token}"
    
    print(f"--- בודק חיבור נקי למשתמש ---")
    try:
        # הוספת כותרת User-Agent כדי שהשרת יחשוב שאנחנו דפדפן
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        
        print(f"סטטוס שרת: {response.status_code}")
        
        if response.status_code == 200:
            user_data = response.json()
            print(f"הצלחה! המערכת מזהה את: {user_data.get('name')}")
            print("עכשיו נסה להריץ שוב את הפקודה של הפרופילים.")
        else:
            print(f"השרת עדיין מחזיר שגיאה. תוכן: {response.text}")
            
    except Exception as e:
        print(f"שגיאה טכנית: {e}")

if __name__ == "__main__":
    final_test()
