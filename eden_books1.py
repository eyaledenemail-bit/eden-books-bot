import requests

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'

def list_profiles():
    url = f"https://api.bufferapp.com/1/profiles.json?access_token={TOKEN}"
    response = requests.get(url)
    
    if response.status_code == 200:
        profiles = response.json()
        print("--- רשימת הפרופילים שלך ---")
        for p in profiles:
            print(f"רשת: {p['service']} | שם: {p['service_username']} | ID: {p['id']}")
    else:
        print(f"שגיאה בחיבור: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    list_profiles()
