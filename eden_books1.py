import requests

# המפתח שלך מהצילום (זה שנגמר ב-kaTu)
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def discover_mutations():
    url = 'https://api.buffer.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # שאילתת "אינטרוספקציה" - שואלת את השרת אילו מוטציות (פקודות) קיימות
    query = """
    query {
      __schema {
        mutationType {
          fields {
            name
            description
          }
        }
      }
    }
    """
    
    print("--- בודק אילו פקודות קיימות ב-API החדש של Buffer ---")
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        print(f"סטטוס שרת: {response.status_code}")
        data = response.json()
        
        if 'data' in data and data['data']['__schema']['mutationType']:
            mutations = data['data']['__schema']['mutationType']['fields']
            print("\nהנה רשימת הפקודות שהשרת מכיר:")
            for m in mutations:
                print(f"- {m['name']}: {m['description']}")
        else:
            print("השרת לא החזיר רשימת פקודות. תשובה גולמית:")
            print(data)
            
    except Exception as e:
        print(f"שגיאה טכנית: {e}")

if __name__ == "__main__":
    discover_mutations()
