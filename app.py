from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/prayertime')
def get_prayer_time():
    city = request.args.get('city', 'Riyadh')
    country = request.args.get('country', 'Saudi Arabia')

    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=4"

    response = requests.get(url)
    data = response.json()
    timings = data['data']['timings']

    prayer_times = (
        f"🕌 أوقات الصلاة لـ {city}: "
        f"الفجر: {timings['Fajr']} 🌅 | "
        f"الظهر: {timings['Dhuhr']} ☀️ | "
        f"العصر: {timings['Asr']} 🌤️ | "
        f"المغرب: {timings['Maghrib']} 🌇 | "
        f"العشاء: {timings['Isha']} 🌌"
    )

    return prayer_times
