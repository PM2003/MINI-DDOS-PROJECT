from flask import Flask, request
import time
import logging
# Create a Flask application
app = Flask(__name__)
# Set up logging
logging.basicConfig(filename='ddos_monitoring.log', level=logging.INFO, format='%(asctime)s -
%(message)s')
# Define a route for the home page
@app.route('/')
def home():
start_time = time.time()
response = "Welcome to the dummy website!"
# Calculate response time
response_time = time.time() - start_time
# Log request and response time
logging.info(f"Route: /, Method: {request.method}, Response Time: {response_time:.4f}
seconds")
return response
# Define a route to echo back the request data
@app.route('/echo', methods=['GET', 'POST'])
def echo():
start_time = time.time()
data = request.get_data(as_text=True)
response = f"Echo: {data}"
# Calculate response time
response_time = time.time() - start_time
# Log request, data, and response time
logging.info(f"Route: /echo, Method: {request.method}, Data: {data}, Response Time:
{response_time:.4f} seconds")
return response
# Define a route to simulate a heavy workload
@app.route('/slow')
def slow():
start_time = time.time()
# Simulate a slow response time
time.sleep(5)
response = "This is a slow response!"
# Calculate response time
response_time = time.time() - start_time
# Log request and response time
logging.info(f"Route: /slow, Method: {request.method}, Response Time: {response_time:.4f}
seconds")
return response
# Run the Flask application
if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)s