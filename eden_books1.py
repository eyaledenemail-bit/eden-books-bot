import requests

# הדבק כאן את המפתח החדש שיצרת בין הגרשיים
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def get_new_ids():
    headers = {'Authorization': f'Bearer {TOKEN}'}
    url = "https://api.bufferapp.com/1/profiles.json"
    
    print("--- בודק את המפתח החדש ומחלץ IDs ---")
    try:
        response = requests.get(url, headers=headers)
        print(f"סטטוס שרת: {response.status_code}")
        
        if response.status_code == 200:
            profiles = response.json()
            print("הצלחה! המפתח החדש עובד. הנה ה-IDs המעודכנים שלך:")
            for p in profiles:
                print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
        else:
            print(f"שגיאה {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"תקלה טכנית: {e}")

if __name__ == "__main__":
    get_new_ids()
