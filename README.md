# crypto-chatbot
# 🚀 CryptoBuddy Chatbot

CryptoBuddy is a rule-based Python chatbot that helps users analyze cryptocurrency trends and receive investment suggestions based on:

✅ **Profitability** → price trends & market cap  
✅ **Sustainability** → energy efficiency & sustainability score

The chatbot is built with **Flask** to run in a web browser, featuring a modern UI.

---

## 🎯 Features

- Ask which crypto is trending
- Discover the most sustainable coin
- Get recommendations for long-term growth
- Query details about specific coins
- Web-based user interface (Flask)
- Simple logic—perfect for beginners!

---

## 💻 Technologies Used

- Python 3.x
- Flask
- HTML/CSS (modern UI styling)

---

## 🪙 Sample Crypto Database

CryptoBuddy uses a predefined dictionary of crypto data:

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-chatbot.git
cd crypto-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- Windows PowerShell:
  ```powershell
  .venv\Scripts\Activate
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install flask
```

*(Optional for future upgrades:)*

```bash
pip install Flask-SQLAlchemy Flask-Login
```

---

## 🚀 Run the App

```bash
python app.py
```

Visit in your browser:

```
http://127.0.0.1:5000/
```

Type your crypto questions in the web UI!

---

## 💬 Example Questions

- `Which crypto is trending?`
- `What is the most sustainable coin?`
- `Tell me about Bitcoin`
- `Which crypto is good for long-term growth?`

---

## ⚠️ Disclaimer

> **CryptoBuddy does not provide financial advice. Crypto investments carry significant risk. Always do your own research before investing. 🚀**

---

## 📝 License

MIT License

---

## 📷 Screenshots

*(Add screenshots)*

---


## ✅ How to use it:

Create a new file:

Copy
Edit
README.md
Paste the markdown above.

Save and commit:

bash
Copy
Edit
git add README.md
git commit -m "Add README for CryptoBuddy"
git push
**Happy crypto exploring with CryptoBuddy! 🚀**
