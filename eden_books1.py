import requests

# העתק את המפתח מהצילום שלך (זה שמופיע תחת eyaleden) והדבק כאן
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def get_profiles_graphql():
    url = 'https://api.bufferapp.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}'}
    
    # שאילתה בשפת GraphQL כדי לקבל את הפרופילים
    query = """
    query {
      profiles {
        id
        service
        service_username
      }
    }
    """
    
    print("--- בודק חיבור למערכת ה-GraphQL החדשה ---")
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        print(f"סטטוס שרת: {response.status_code}")
        
        data = response.json()
        if 'data' in data and data['data']['profiles']:
            print("הצלחה! הנה ה-IDs המעודכנים שלך:")
            for p in data['data']['profiles']:
                print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
        else:
            print("שגיאה בתשובה מהשרת:", data)
            
    except Exception as e:
        print(f"תקלה טכנית: {e}")

if __name__ == "__main__":
    get_profiles_graphql()
