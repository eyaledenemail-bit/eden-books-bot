import requests

# המפתח שלך מהצילום (זה שנגמר ב-kaTu)
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu'

def inspect_input_type():
    url = 'https://api.buffer.com/graphql'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # שאילתה שבודקת את מבנה הנתונים שהשרת מצפה לו ב-createPost
    query = """
    query {
      __type(name: "CreatePostInput") {
        inputFields {
          name
          type {
            name
            kind
            ofType {
              name
            }
          }
        }
      }
    }
    """
    
    print("--- בודק את המבנה המדויק של פקודת הפרסום ---")
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        data = response.json()
        
        if 'data' in data and data['data']['__type']:
            fields = data['data']['__type']['inputFields']
            print("\nהנה השדות שאתה חייב להשתמש בהם:")
            for f in fields:
                field_type = f['type']['name'] or f['type']['ofType']['name']
                print(f"- {f['name']} (סוג: {field_type})")
        else:
            print("שגיאה בקבלת המבנה:", data)
            
    except Exception as e:
        print(f"שגיאה טכנית: {e}")

if __name__ == "__main__":
    inspect_input_type()
