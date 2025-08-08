# CryptAsk

Crypto-Chatbot
This is a chatbot which provides you with all the information you require regarding crypto currency whether it be prices or information about various terms related to crypto currencies.

CryptAsk: Cryptocurrency Chatbot
CryptAsk is an interactive web application designed to simplify cryptocurrency information for users. It provides live cryptocurrency prices, answers frequently asked questions, and offers basic financial tips. Built using Flask for the backend and HTML/CSS for the frontend, CryptAsk ensures a seamless user experience.

Features
Live Cryptocurrency Prices: Get real-time prices of popular cryptocurrencies like Bitcoin, Ethereum, and more.
FAQs: Access predefined answers to common cryptocurrency-related questions.
Financial Tips: Receive helpful tips on savings, investments, and debt management.
Interactive UI: A responsive and visually appealing user interface.
Technologies Used
Backend: Flask, Python
Frontend: HTML, CSS, JavaScript
Database: MongoDB for managing FAQs
API Integration: CoinGecko API for real-time cryptocurrency prices
Styling: CSS for a dynamic and responsive layout
Installation
Prerequisites
Ensure you have the following installed on your system:

Python 3.7+
MongoDB instance (Cloud or Local)
Steps
Clone the Repository

git clone https://github.com/your-repo/cryptask.git
cd cryptask
Set up the Environment Install required dependencies using pip:

pip install -r requirements.txt
Configure MongoDB Update the MongoDB connection string in app.py to your instance:

client = MongoClient("your-mongodb-connection-string")
Run the Application Start the Flask server:

python app.py
Access the Application Open your browser and navigate to:

http://localhost:5000
File Structure
.
├── app.py                # Backend logic and API integrations
├── templates
│   └── index.html       # Frontend structure
├── static
│   ├── css              # Custom styles
│   ├── js               # Client-side scripts
│   └── images           # Static assets
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
Usage
Start typing your query or click predefined options in the chatbot.
For live prices, type queries like:
"crypto price for bitcoin"
"crypto price for ethereum"
Explore FAQs by selecting predefined buttons.
Screenshots
Chatbot Interface

Future Enhancements
Add multilingual support.
Include user authentication for personalized experiences.
Expand financial tips and cryptocurrency details.
Add charts for price trends.
Future Enhancements Add multilingual support. Include user authentication for personalized experiences. Expand financial tips and cryptocurrency details. Add charts for price trends.
