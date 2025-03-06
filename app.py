from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Sample data
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs"
]

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', 
                           title='Welcome to My Dynamic App', 
                           current_time=current_time)

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        except ValueError:
            result = "Error: Invalid input"
    
    return render_template('calculator.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
