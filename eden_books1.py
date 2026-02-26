import requests
from datetime import datetime

TOKEN = 'jujSx245sEU_sJJl3w8rDpsNBqTBae9Ajr58GKSMa4X'
PROFILE_IDS = ['69a00b534be271803d6c88c4', '69a00b894be271803d6c8938', '69a00cd24be271803d6c9595']

# רשימת המדיה שלך (קישורים ישירים)
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
    "https://drive.google.com/uc?export=download&id=1z-7viMXR-HT_Y413gA1Zk_Z6QKzSsqXQ"
]

# בנק הודעות ל-30 יום
messages = [
    messages = [
    # יום 1: השיבה הביתה
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה, אל מקור הנשמה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Are you ready for the journey back home, to the source of the soul? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Estás listo para el viaje de regreso a casa, al origen del alma? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",

    # יום 2: פורטל לאינסוף
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לעולם שכולו אור. גלו את הפורטל לאינסוף. ✨ [קישור]\n🇺🇸 Beyond time and space, there is a gate to a world of light. Discover the portal to infinity. 🌌 [Link]\n🇪🇸 Más allá del tiempo y el espacio, hay una puerta a un mundo de luz. Descubre el portal al infinito. ❤️ [Link]",

    # יום 3: פרח החיים
    "🇮🇱 הגיאומטריה המקודשת של הטבע היא המפה של הלב. חקרו את פרח החיים. 🌸 [קישור]\n🇺🇸 The sacred geometry of nature is the map of the heart. Explore the Flower of Life. 🌸 [Link]\n🇪🇸 La geometría sagrada de la naturaleza es el mapa del corazón. Explora la Flor de la Vida. ❤️ [Link]",

    # יום 4: הזמן כצמיחה רגשית
    "🇮🇱 הזמן אינו אויב, הוא הכלי שלנו לגדילה רגשית עמוקה. ⏳ [קישור]\n🇺🇸 Time is not an enemy; it is our tool for deep emotional growth. ⏳ [Link]\n🇪🇸 El tiempo no es un enemigo; es nuestra herramienta para el crecimiento emocional profundo. ❤️ [Link]",

    # יום 5: חיים מעבר לשמש
    "🇮🇱 האור שאתם רואים בשמים הוא רק קצה הקרחון של המציאות. יש חיים מעבר לשמש. ☀️ [קישור]\n🇺🇸 The light you see in the sky is just the tip of the iceberg. There is life beyond the sun. 🌌 [Link]\n🇪🇸 La luz que ves en el cielo es solo la punta del iceberg. Hay vida más allá del sol. ❤️ [Link]",

    # יום 6: הכלי המקודש
    "🇮🇱 שלוש הכוחות של הכלי המקודש מחכים להתגלות בתוככם. 💎 [קישור]\n🇺🇸 The three powers of the Sacred Vessel are waiting to be revealed within you. 💎 [Link]\n🇪🇸 Los tres poderes de la Vasija Sagrada están esperando ser revelados dentro de ti. ❤️ [Link]",

    # יום 7: נהר הנשמות
    "🇮🇱 הנשמה זורמת בנהר נצחי של אהבה ובריאה. 🌊 [קישור]\n🇺🇸 The soul flows in an eternal river of love and creation. 🌊 [Link]\n🇪🇸 El alma fluye en un río eterno de amor y creación. ❤️ [Link]",

    # יום 8: איחוד המלך והמלכה
    "🇮🇱 סיפור האהבה העתיק ביותר ביקום – איחוד המלך והמלכה בירושלים. 👑 [קישור]\n🇺🇸 The oldest love story in the universe – the union of the King and Queen in Jerusalem. 👑 [Link]\n🇪🇸 La historia de amor más antigua del universo: la unión del Rey y la Reina en Jerusalén. ❤️ [Link]",

    # יום 9: יהלום הנשמה
    "🇮🇱 כל נשמה היא יהלום נדיר בכתרו של הבורא. הגיע הזמן להבריק. 💎 [קישור]\n🇺🇸 Every soul is a rare diamond in the Creator's crown. It's time to shine. 💎 [Link]\n🇪🇸 Cada alma es un diamante raro en la corona del Creador. Es hora de brillar. ❤️ [Link]",

    # יום 10: סוד הגאולה
    "🇮🇱 גאולה אישית מתחילה במעשה אחד קטן של חסד. 🕊️ [קישור]\n🇺🇸 Personal redemption begins with one small act of kindness. 🕊️ [Link]\n🇪🇸 La redención personal comienza con un pequeño acto de bondad. ❤️ [Link]",

    # יום 11: האדם כאלמנט חמישי
    "🇮🇱 אש, אדמה, אוויר ומים – ואתם, האלמנט החמישי המחבר ביניהם. 🔥 [קישור]\n🇺🇸 Fire, Earth, Air, and Water – and you, the fifth element connecting them all. 🔥 [Link]\n🇪🇸 Fuego, Tierra, Aire y Agua – y tú, el quinto elemento que los conecta a todos. ❤️ [Link]",

    # יום 12: מסע הלוחם הרוחני
    "🇮🇱 הלוחם האמיתי הוא זה שכובש את פחדיו ובוחר באהבה. ⚔️ [קישור]\n🇺🇸 The true warrior is the one who conquers fear and chooses love. ⚔️ [Link]\n🇪🇸 El verdadero guerrero es aquel que conquista el miedo y elige el amor. ❤️ [Link]",

    # יום 13: זכרון הנשמה
    "🇮🇱 הנשמה שלכם זוכרת את המקום ממנו באה. הקשיבו לה. 👂 [קישור]\n🇺🇸 Your soul remembers where it came from. Listen to it. 🌌 [Link]\n🇪🇸 Tu alma recuerda de dónde vino. Escúchala. ❤️ [Link]",

    # יום 14: כוחה של תפילה
    "🇮🇱 תפילה היא גשר בין הלב האנושי לממלכות העליונות. 🙏 [קישור]\n🇺🇸 Prayer is a bridge between the human heart and the higher realms. 🙏 [Link]\n🇪🇸 La oración es un puente entre el corazón humano y los reinos superiores. ❤️ [Link]",

    # יום 15: הבריאה מתוך אהבה
    "🇮🇱 העולם לא נוצר במקרה, הוא נוצר מתוך אהבה אינסופית אליכם. ❤️ [קישור]\n🇺🇸 The world was not created by chance; it was created out of infinite love for you. ❤️ [Link]\n🇪🇸 El mundo no fue creado por casualidad; fue creado por un amor infinito hacia ti. ❤️ [Link]",

    # פוסטים 16-30 ימשיכו לגוון בין המסרים על האות א', סודות המלכות, והתקשור הרוחני של אייל עדן עם הבורא.
    # ... (המשך הרשימה יכיל וריאציות על המסרים הללו)
]

def post_daily():
    day = (datetime.now().day - 1) % len(messages)
    m_index = (datetime.now().day - 1) % len(media_links)
    
    data = {
        'access_token': TOKEN,
        'profile_ids[]': PROFILE_IDS,
        'text': messages[day],
        'media[video]': media_links[m_index],
        'shorten': 'false'
    }
    r = requests.post("https://api.bufferapp.com/1/updates/create.json", data=data)
    print(r.json())

if __name__ == "__main__":

    post_daily()
