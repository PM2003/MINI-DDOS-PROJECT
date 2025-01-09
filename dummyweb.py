from flask import Flask, request
# Create a Flask application
app = Flask(__name__)
# Define a route for the home page
@app.route('/')
def home():
return "Welcome to the dummy website!"
# Define a route to echo back the request data
@app.route('/echo', methods=['GET', 'POST'])
def echo():
data = request.get_data(as_text=True)
return f"Echo: {data}"
# Define a route to simulate a heavy workload
@app.route('/slow')
def slow():
import time
# Simulate a slow response time
time.sleep(5)
return "This is a slow response!"
# Run the Flask application
if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)