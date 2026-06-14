# Spell Checker App using Python

#importing the necessary library

from flask import Flask, render_template, request
from spellchecker import SpellChecker

app = Flask(__name__)

spell = SpellChecker()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():

    text = request.form['text']

    words = text.split()

    corrected_words = []

    for word in words:

        corrected_word = spell.correction(word)

        if corrected_word is None:
            corrected_word = word

        corrected_words.append(corrected_word)

    corrected_text = " ".join(corrected_words)

    return render_template(
        'index.html',
        original=text,
        corrected=corrected_text
    )
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)