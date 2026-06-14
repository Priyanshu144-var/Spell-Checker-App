# Spell-Checker-App

AI Spell Checker Web Application

A modern and user-friendly Spell Checker Web Application built using Python, Flask, and PySpellChecker. This application helps users detect and automatically correct spelling mistakes in English text through a clean and responsive web interface.

Features

- Spell checking and auto-correction
- Modern Glassmorphism UI design
- Fast and lightweight
- User-friendly interface
- Responsive design
- Built with Flask and Python

Technologies Used

- Python
- Flask
- HTML5
- CSS3
- PySpellChecker

Project Structure

spell-checker-web-app/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

Installation

Clone the Repository

git clone https://github.com/your-username/spell-checker-web-app.git
cd spell-checker-web-app

Create Virtual Environment (Optional)

python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Run the Application

python app.py

Open your browser and visit:

http://127.0.0.1:5000

How It Works

1. User enters text in the input area.
2. Flask receives the text from the form.
3. PySpellChecker analyzes each word.
4. Misspelled words are corrected automatically.
5. Corrected text is displayed on the webpage.

Example

Input

helllo worlld

Output

hello world

Future Enhancements

- Dark/Light Mode
- Voice Input
- Multiple Language Support
- Download Corrected Text
- Grammar Checking
- AI-Based Suggestions

Author

Priyanshu Varshney

License

This project is open source and available under the MIT License.
