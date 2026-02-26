import requests

TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' # המפתח שנגמר ב-kaTu

def final_inspection():
    url = 'https://api.buffer.com/graphql'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    
    # שאילתה לבדיקת הערכים המותרים ב-Enums ובמבנה ה-Assets
    query = """
    query {
      schedulingType: __type(name: "SchedulingType") { enumValues { name } }
      shareMode: __type(name: "ShareMode") { enumValues { name } }
      assetsInput: __type(name: "AssetsInput") { inputFields { name } }
    }
    """
    
    try:
        response = requests.post(url, json={'query': query}, headers=headers)
        data = response.json()
        
        if 'data' in data:
            d = data['data']
            print("--- ערכי SchedulingType מותרים ---")
            for e in d['schedulingType']['enumValues']: print(f"- {e['name']}")
            
            print("\n--- ערכי ShareMode מותרים ---")
            for e in d['shareMode']['enumValues']: print(f"- {e['name']}")
            
            print("\n--- שדות בתוך AssetsInput ---")
            for f in d['assetsInput']['inputFields']: print(f"- {f['name']}")
        else:
            print("שגיאה:", data)
    except Exception as e:
        print(f"תקלה: {e}")

if __name__ == "__main__":
    final_inspection()
