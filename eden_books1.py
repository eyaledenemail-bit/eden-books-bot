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

    # יום 16: כוחה של האות א'
    "🇮🇱 האות א' - תחילת הכל, האחדות שבין הבורא לבריאה. 🌀 [קישור]\n🇺🇸 The letter Aleph - the beginning of everything, the unity between Creator and creation. 🌀 [Link]\n🇪🇸 La letra Alef: el principio de todo, la unidad entre el Creador y la creación. ❤️ [Link]",

    # יום 17: המלכות העליונה
    "🇮🇱 הצצה לממלכת המלכים שמעבר לשמש. שם הכל התחיל. ✨ [קישור]\n🇺🇸 A glimpse into the Kingdom of Kings beyond the sun. Where it all began. 🌌 [Link]\n🇪🇸 Una mirada al Reino de los Reyes más allá del sol. Donde todo comenzó. ❤️ [Link]",

    # יום 18: חמשת האלמנטים
    "🇮🇱 האם אתם מכירים את האלמנט החמישי? הוא נמצא בתוככם. 🔥💧💨🌱 [קישור]\n🇺🇸 Do you know the fifth element? It is within you. 🔥💧💨🌱 [Link]\n🇪🇸 ¿Conoces el quinto elemento? Está dentro de ti. ❤️ [Link]",

    # יום 19: זרעי הבריאה
    "🇮🇱 כל פעולה שלכם היא זרע שנשתל בגן הבריאה. בחרו באהבה. 🌱 [קישור]\n🇺🇸 Every action is a seed planted in the garden of creation. Choose love. 🌱 [Link]\n🇪🇸 Cada acción es una semilla plantada en el jardín de la creación. Elige el amor. ❤️ [Link]",

    # יום 20: סוד המים והנשמה
    "🇮🇱 כמו מים שזורמים לים, הנשמה תמיד מחפשת את דרכה חזרה למקור. 🌊 [קישור]\n🇺🇸 Like water flowing to the sea, the soul always seeks its way back to the source. 🌊 [Link]\n🇪🇸 Como el agua que fluye hacia el mar, el alma siempre busca su camino de regreso al origen. ❤️ [Link]",

    # יום 21: האור הגנוז
    "🇮🇱 האור הגנוז מחכה לאלו שמעזים להביט פנימה. 🕯️ [קישור]\n🇺🇸 The hidden light awaits those who dare to look within. 🕯️ [Link]\n🇪🇸 La luz oculta espera a quienes se atreven a mirar hacia adentro. ❤️ [Link]",

    # יום 22: ירושלים של מעלה
    "🇮🇱 ירושלים היא לא רק עיר, היא שער רוחני לאיחוד העולמות. 🏰 [קישור]\n🇺🇸 Jerusalem is not just a city; it is a spiritual gate for the union of worlds. 🏰 [Link]\n🇪🇸 Jerusalén no es solo una ciudad; es una puerta espiritual para la unión de los mundos. ❤️ [Link]",

    # יום 23: האהבה ככוח בורא
    "🇮🇱 אהבה היא האנרגיה שהקימה את העולם. הרגישו אותה. ❤️ [קישור]\n🇺🇸 Love is the energy that built the world. Feel it. ❤️ [Link]\n🇪🇸 El amor es la energía que construyó el mundo. Siéntela. ❤️ [Link]",

    # יום 24: הקול הפנימי
    "🇮🇱 הבורא מדבר אליכם דרך השקט. האם אתם מקשיבים? 🤫 [קישור]\n🇺🇸 The Creator speaks to you through the silence. Are you listening? 🌌 [Link]\n🇪🇸 El Creador te habla a través del silencio. ¿Estás escuchando? ❤️ [Link]",

    # יום 25: המטרה האישית
    "🇮🇱 לכל נשמה יש תפקיד ייחודי בתיקון העולם. מצאו את שלכם. ✨ [קישור]\n🇺🇸 Every soul has a unique role in repairing the world. Find yours. ✨ [Link]\n🇪🇸 Cada alma tiene un papel único en la reparación del mundo. Encuentra el tuyo. ❤️ [Link]",

    # יום 26: חסד ורחמים
    "🇮🇱 עולם חסד ייבנה. כל מעשה טוב מקרב את הגאולה. 🤝 [קישור]\n🇺🇸 A world of kindness will be built. Every good deed brings redemption closer. 🤝 [Link]\n🇪🇸 Un mundo de bondad será construido. Cada buena acción acerca la redención. ❤️ [Link]",

    # יום 27: הנצחיות שלכם
    "🇮🇱 הגוף זמני, אבל האור שלכם נצחי. אל תפחדו לזרוח. 🌟 [קישור]\n🇺🇸 The body is temporary, but your light is eternal. Don't be afraid to shine. 🌟 [Link]\n🇪🇸 El cuerpo es temporal, pero tu luz es eterna. No tengas miedo de brillar. ❤️ [Link]",

    # יום 28: השכינה בינינו
    "🇮🇱 השכינה שוכנת בכל מקום שבו יש אהבה ואמת. 🕊️ [קישור]\n🇺🇸 The Divine Presence dwells wherever there is love and truth. 🕊️ [Link]\n🇪🇸 La Presencia Divina mora dondequiera que haya amor y verdad. ❤️ [Link]",

    # יום 29: המסע נמשך
    "🇮🇱 המוות הוא רק דלת לממלכה הבאה. המסע לעולם לא נגמר. 🚪 [קישור]\n🇺🇸 Death is only a door to the next kingdom. The journey never ends. 🌌 [Link]\n🇪🇸 La muerte es solo una puerta al siguiente reino. El viaje nunca termina. ❤️ [Link]",

    # יום 30: סיכום והתחלה חדשה
    "🇮🇱 סיימנו חודש של גילויים, אבל הגאולה רק מתחילה. הצטרפו אלינו. ✨ [קישור]\n🇺🇸 We finished a month of discoveries, but redemption is just beginning. Join us. ✨ [Link]\n🇪🇸 Terminamos un mes de descubrimientos, pero la redención solo está comenzando. Únete a nosotros. ❤️ [Link]"
    
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

