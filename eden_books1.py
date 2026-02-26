import requests
from datetime import datetime

# פרטי הגישה שלך
TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'
PROFILE_IDS = ['69a00b534be271803d6c88c4', '69a00b894be271803d6c8938', '69a00cd24be271803d6c9595']

media_links = [
    "https://drive.google.com/uc?export=download&id=1yUzXKQIFDePnNuTNhaVj6c68sdnlK8SN",
    "https://drive.google.com/uc?export=download&id=1apuf0UzMEQxZxudid0k0D4jLq1CnN_ap",
    "https://drive.google.com/uc?export=download&id=1H4IDzt683V8MBaWgEIpbAmO4JPTJFi7W",
    "https://drive.google.com/uc?export=download&id=1SqJI7NsEjba54C4EWO5gZlvnvNucwJgr",
    "https://drive.google.com/uc?export=download&id=1qr9PrYh5j057vGD9MY7HX1UwXlRe2o_W",
    "https://drive.google.com/uc?export=download&id=1YDtgOF5AN9FDrueujH_s0mZilA-TSizq",
    "https://drive.google.com/uc?export=download&id=1ZUCC3UPJCf0MiwG9PY_vSr8c_24Ki2aG",
    "https://drive.google.com/uc?export=download&id=1AeaQ_pEqqzuxwSQD9qPyWKZiCUqVAaHg",
    "https://drive.google.com/uc?export=download&id=1D2G65cEAVfSlNAiLK1sksK6w_u0yugwg",
    "https://drive.google.com/uc?export=download&id=1z-7viMXR-HT_Y413gA1Zk_Z6QKzSsqXQ",
    "https://drive.google.com/uc?export=download&id=17FO7xqyctMsEdGBu3HH5QU92Nr5tJenZ",
    "https://drive.google.com/uc?export=download&id=1bdM-Cb3x2afG3YIMLsqEPWJk6seWHJLK",
    "https://drive.google.com/uc?export=download&id=16r8LEv57QBquxddCd6o89bpkhV0MSdAD"
]

messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Return home to your soul. 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 Regreso al origen del alma. ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%94%D7%97%D7%99%D7%99%D7%9D-%D7%94%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Beyond time and space. 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 Más allá del tiempo y el espacio. ❤️ https://www.amazon.es/dp/B0GNHN9X1T"
] # הוסף כאן את שאר ה-30 שנתתי לך קודם

def post_daily():
    day_index = (datetime.now().day - 1) % len(messages)
    media_index = (datetime.now().day - 1) % len(media_links)
    
    url = "https://api.bufferapp.com/1/updates/create.json"
    
    # שליחה לכל פרופיל בנפרד כדי למנוע קריסה כללית
    for profile_id in PROFILE_IDS:
        data = {
            'access_token': TOKEN,
            'profile_ids[]': [profile_id],
            'text': messages[day_index],
            'media[video]': media_links[media_index],
            'shorten': 'false'
        }
        
        print(f"נסה לפרסם לפרופיל: {profile_id}")
        response = requests.post(url, data=data)
        
        print(f"סטטוס שרת: {response.status_code}")
        try:
            print("תשובת Buffer:", response.json())
        except:
            print("שגיאה: השרת לא החזיר JSON. תוכן התשובה:")
            print(response.text)

if __name__ == "__main__":
    post_daily()
