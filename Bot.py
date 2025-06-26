from flask import Flask

import requests
from datetime import datetime

TOKEN = '7824269927:AAGnd7FWPH9LVwyuRwzOXEcVocxQ4J-OoBw'
CHAT_ID = '@fathkerajer'

# 📝 قائمة المنشورات العشوائية
posts = [
    " قال رسول الله  خيركم من تعلم القرآن وعلمه",
    "الصلاة عماد الدين، حافظ عليها",
    " التفكر ساعة خير من عبادة سنة",
    " سبحان الله وبحمده، سبحان الله العظيم",
    " تبسمك في وجه أخيك صدقة",
    " اجعل هدفك الجنة ولا تنشغل عنها",
    " صل من قطعك واعفُ عمن ظلمك",
    " فضل الصيام لا يُدرك إلا بثواب عظيم",
    " الذكر حصن المسلم",
    " اقرأ وردك من القرآن اليوم"
]

now = datetime.now()
if now.hour == 1 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 1 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[3]}')
if now.hour == 2 and now.minute < 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 10 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 11 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 11 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 12 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 12 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 13 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 13 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 14 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 14 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 15 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 15 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 16 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 16 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 17 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 17 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 18 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 18 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 19 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 19 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 20 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 20 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 21 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 21 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 22 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 22 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 23 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 23 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 0 and now.minute == 0:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[0]}')
if now.hour == 0 and now.minute > 30:
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')
if now.hour == 3 and now.minute > 30 :
        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={posts[1]}')

app = Flask(__name__)

@app.route('/')
def index():
    import random
    msg = random.choice(posts)
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}')
    return f"✅ تم النشر: {msg}"

if __name__ == '__main__':
    app.run()
