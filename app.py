from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# MODELS
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    chats = db.relationship('Chat', backref='user', lazy=True)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# LOGIN MANAGER
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# CRYPTO DB
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3 / 10},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6 / 10},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8 / 10}
}

# CHATBOT LOGIC
def chatbot_response(user_query):
    user_query = user_query.lower()

    if user_query == "exit":
        return "👋 Goodbye! Remember, crypto is risky — always do your own research. 🚀"

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Try {recommend} — it's one of the most eco-friendly cryptos available!"

    elif "trending" in user_query or "rising" in user_query or "profitable" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 Trending coins: {', '.join(trending_coins)} 🚀" if trending_coins else "🔍 No coins are trending up at the moment."

    elif "long-term" in user_query or "growth" in user_query:
        suitable = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7]
        return f"🕒 Long-term picks: {', '.join(suitable)} — rising and sustainable!" if suitable else "🤔 No ideal long-term picks right now."

    else:
        for coin in crypto_db:
            if coin.lower() in user_query:
                details = crypto_db[coin]
                return (
                    f"📊 *{coin} Overview*:\n"
                    f"- Price Trend: {details['price_trend']}\n"
                    f"- Market Cap: {details['market_cap']}\n"
                    f"- Energy Use: {details['energy_use']}\n"
                    f"- Sustainability Score: {int(details['sustainability_score'] * 10)}/10"
                )
        return "🤖 Ask me about specific coins, trends, sustainability or growth."

# ROUTES
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    response = ""
    if request.method == "POST":
        question = request.form["message"]
        response = chatbot_response(question)

        # Save to DB
        chat = Chat(question=question, answer=response, user_id=current_user.id)
        db.session.add(chat)
        db.session.commit()

    # Load full chat history for current user
    chat_history = Chat.query.filter_by(user_id=current_user.id).order_by(Chat.timestamp.desc()).all()
    return render_template("index.html", response=response, chat_history=chat_history)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("signup"))

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful. Please log in.")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/history")
@login_required
def history():
    chats = Chat.query.filter_by(user_id=current_user.id).order_by(Chat.timestamp.desc()).all()
    return render_template("history.html", chats=chats)

# DB INIT
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
