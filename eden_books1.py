import requests

# הדבק כאן את המפתח שמופיע תחת eyaleden בצילום המסך שלך
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def get_buffer_channels():
    url = 'https://api.buffer.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    # שאילתה מעודכנת שמתאימה למערכת ה-Beta החדשה
    query = """
    query {
      account {
        organizations {
          id
          name
          channels {
            id
            service
            name
          }
        }
      }
    }
    """

    print("--- מנסה למשוך ערוצים ממערכת ה-Beta (GraphQL) ---")
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        print(f"סטטוס שרת: {response.status_code}")
        data = response.json()

        if 'errors' in data:
            print("שגיאת GraphQL:", data['errors'])
        else:
            orgs = data.get('data', {}).get('account', {}).get('organizations', [])
            if not orgs:
                print("לא נמצאו ארגונים בחשבון זה.")
            for org in orgs:
                print(f"\nארגון: {org['name']} (ID: {org['id']})")
                print("ערוצים מחוברים:")
                for channel in org.get('channels', []):
                    print(f"  - רשת: {channel['service']} | שם: {channel['name']} | ID: {channel['id']}")
    except Exception as e:
        print(f"שגיאה טכנית: {e}")

if __name__ == "__main__":
    get_buffer_channels()

