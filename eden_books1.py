import requests

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'

def final_debug():
    # הוספת כותרות שמדמות דפדפן כדי למנוע חסימות של Buffer
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print("--- ניסיון חיבור סופי למערכת Buffer ---")
    
    # ניסיון לבדוק את הפרופילים ישירות
    url = "https://api.bufferapp.com/1/profiles.json"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"סטטוס שרת: {response.status_code}")
        
        if response.status_code == 200:
            profiles = response.json()
            print("הצלחה! המכונה מחוברת. אלו הפרופילים שלך:")
            for p in profiles:
                print(f"- רשת: {p['service']} | שם משתמש: {p['service_username']} | ID: {p['id']}")
        elif response.status_code == 401:
            print("שגיאה 401: המפתח (Token) לא תקין או פג תוקף. צור מפתח חדש ב-Buffer.")
        else:
            print(f"שגיאה {response.status_code}: השרת החזיר תשובה לא צפויה.")
            print("תוכן השגיאה:", response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"שגיאת תקשורת: {e}")

if __name__ == "__main__":
    final_debug()
