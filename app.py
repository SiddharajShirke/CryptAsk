from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb+srv://abhayshinde16325:fVDu9Xpzl9YWIUmA@cluster0.9humt.mongodb.net/")
db = client.crypto_chatbot
faqs_collection = db.FAQS

def get_crypto_price(crypto_symbol, fiat_symbol="usd"):
    """Get cryptocurrency price using CoinGecko API"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={fiat_symbol}"
    response = requests.get(url)
    data = response.json()
    
    if crypto_symbol not in data:
        return f"Error: Unable to find data for cryptocurrency symbol '{crypto_symbol}'."
    
    try:
        rate = data[crypto_symbol][fiat_symbol]
        return f"The current price of {crypto_symbol.upper()} in {fiat_symbol.upper()} is ${rate}."
    except KeyError as e:
        return f"Error processing data: {str(e)}."

def process_user_query(user_input):
    """Combined logic to handle both FAQ and live crypto price queries"""
    user_input = user_input.lower()
    
    # Handle predefined button queries
    if user_input == "trending cryptocurrencies":
        return "Here are today's trending cryptocurrencies: Bitcoin (BTC), Ethereum (ETH), and Solana (SOL). Would you like to know the current price of any of these?"
    
    elif user_input == "crypto basics":
        return "Cryptocurrency is a digital or virtual form of currency that uses cryptography for security. The most popular cryptocurrency is Bitcoin, followed by Ethereum. Would you like to learn more about a specific aspect of cryptocurrencies?"
    
    elif user_input == "what is bitcoin":
        return "Bitcoin is the first and most well-known cryptocurrency, created in 2009 by an unknown person using the pseudonym Satoshi Nakamoto. It's a decentralized digital currency that can be sent from user to user without the need for intermediaries. Would you like to know the current Bitcoin price?"
    
    # Check for crypto price query
    if "crypto price" in user_input:
        symbol = user_input.split("crypto price for")[-1].strip().lower()
        return get_crypto_price(symbol)
    
    # Check MongoDB for FAQ match
    faq = faqs_collection.find_one({"question": {"$regex": user_input, "$options": "i"}})
    if faq:
        return faq['answer']
    
    # Handle other financial queries
    if "savings tip" in user_input:
        return "Start by saving at least 20% of your income each month."
    elif "investment tip" in user_input:
        return "Diversify your investments to minimize risk."
    elif "debt management" in user_input:
        return "Focus on paying off high-interest debts first."
    
    return "I can help you with cryptocurrency prices and general financial questions. Try asking about 'crypto price for bitcoin' or check our FAQs!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({"response": "Please provide a message."})
    
    response = process_user_query(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True) 