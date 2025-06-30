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


def chatbot():
    print("👋 Hey there! I’m CryptoBuddy. Let’s hunt for green and growing cryptos together!")
    print("Type 'exit' to leave the chat.\n")
    
    while True:
        user_query = input("You: ").lower()
        
        if user_query == "exit":
            print("CryptoBuddy: Goodbye! Remember, crypto is risky—always do your own research. 🚀")
            break
        
        # Sustainability question
        if "sustainable" in user_query or "eco" in user_query:
            recommend = max(
                crypto_db,
                key=lambda x: crypto_db[x]["sustainability_score"]
            )
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
        
        # Trending or profitability question
        elif "trending" in user_query or "rising" in user_query or "profitable" in user_query:
            trending_coins = []
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising":
                    trending_coins.append(coin)
            
            if trending_coins:
                print(f"CryptoBuddy: These coins are trending up: {', '.join(trending_coins)} 🚀")
            else:
                print("CryptoBuddy: Hmm, nothing is trending up at the moment.")
        
        # Long-term growth
        elif "long-term" in user_query or "growth" in user_query:
            suitable_coins = []
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                    suitable_coins.append(coin)
            
            if suitable_coins:
                print(f"CryptoBuddy: For long-term growth, I’d recommend {', '.join(suitable_coins)}. 🚀 They’re rising and sustainable!")
            else:
                print("CryptoBuddy: Hmm, no coins perfectly match long-term growth criteria right now.")
        
        # Specific coin information
        else:
            found = False
            for coin in crypto_db:
                if coin.lower() in user_query:
                    details = crypto_db[coin]
                    message = (
                        f"CryptoBuddy: Here’s what I know about {coin}:\n"
                        f"- Price Trend: {details['price_trend']}\n"
                        f"- Market Cap: {details['market_cap']}\n"
                        f"- Energy Use: {details['energy_use']}\n"
                        f"- Sustainability Score: {details['sustainability_score']*10}/10"
                    )
                    print(message)
                    found = True
                    break
            if not found:
                print("CryptoBuddy: Hmm, I’m not sure how to answer that. Try asking me about sustainability, profitability, or a specific coin.")

chatbot()
