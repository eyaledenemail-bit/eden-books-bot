import requests

# העתק את המפתח החדש שמופיע תחת eyaleden בצילום המסך שלך והדבק כאן
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def get_ids_v2():
    # הכתובת המדויקת למערכת ה-Beta החדשה
    url = 'https://api.buffer.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # שאילתה לקבלת המזהים של הערוצים שלך
    query = """
    query {
      profiles {
        id
        service
        service_username
      }
    }
    """
    
    print("--- בודק חיבור למערכת ה-GraphQL (api.buffer.com) ---")
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        print(f"סטטוס שרת: {response.status_code}")
        
        data = response.json()
        if 'data' in data and data['data']['profiles']:
            print("הצלחה! הנה ה-IDs המעודכנים שלך:")
            for p in data['data']['profiles']:
                print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
        else:
            print("שגיאה בתשובה:", data)
            
    except Exception as e:
        print(f"תקלה טכנית: {e}")

if __name__ == "__main__":
    get_ids_v2()
