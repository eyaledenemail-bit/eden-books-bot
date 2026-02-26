import requests
from datetime import datetime

# --- הגדרות מערכת ---
# הדבק את המפתח שלך (זה שנגמר ב-kaTu) בין הגרשיים בשורה למטה
TOKEN = 'UF3XfWBgBQ6p28kcw91dKGNBJ_rPP_NSyVK2sPzkaTu' 

ORG_ID = '699ffcd6c130d9cd2ddc81cd' # המזהה של הארגון שלך
CHANNEL_IDS = [
    '69a00b534be271803d6c88c4', # Facebook
    '69a00b894be271803d6c8938', # Instagram
    '69a00cd24be271803d6c9595'  # Threads (זה שכבר עובד!)
]

# --- בנק מדיה (13 קבצים) ---
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

# --- בנק הודעות (30 יום) ---
messages = [
    "🇮🇱 האם אתם מוכנים למסע חזרה הביתה? ✨ https://nivbook.co.il/product/%D7%9B%D7%95%D7%97-%D7%9ה%D7%97%D7%99%D7%99%D7%9D-%D7%9ה%D7%92%D7%90%D7%95%D7%9C%D7%94/\n🇺🇸 Ready for the journey home? 🌌 https://www.amazon.com/Power-Life-Redemption-Eyal-Eden/dp/B0FQMB2W4M\n🇪🇸 ¿Listo para el viaje a casa? ❤️ https://www.amazon.es/dp/B0GNHN9X1T",
    "🇮🇱 מעבר לזמן ולמרחב, קיים שער לאור. ✨ [Link]",
    "🇮🇱 הגיאומטריה המקודשת של הטבע היא המפה של הלב. 🌸 [Link]",
    "🇮🇱 הזמן אינו אויב, הוא הכלי לגדילה רגשית. ⏳ [Link]",
    "🇮🇱 האור בשמים הוא רק קצה הקרחון של המציאות. ☀️ [Link]",
    "🇮🇱 שלוש הכוחות של הכלי המקודש מחכים לכם. 💎 [Link]",
    "🇮🇱 הנשמה זורמת בנהר נצחי של אהבה. 🌊 [Link]",
    "🇮🇱 סיפור האהבה העתיק ביותר - איחוד המלך והמלכה. 👑 [Link]",
    "🇮🇱 כל נשמה היא יהלום נדיר בכתרו של הבורא. 💎 [Link]",
    "🇮🇱 גאולה אישית מתחילה במעשה קטן של חסד. 🕊️ [Link]",
    "🇮🇱 אש, אדמה, אוויר ומים - ואתם האלמנט החמישי. 🔥 [Link]",
    "🇮🇱 הלוחם האמיתי כובש את פחדיו ובוחר באהבה. ⚔️ [Link]",
