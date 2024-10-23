import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# API Endpoint
url = "http://your-flask-app-url/predict"

# Test cases
test_cases = [
    {"text": "This is a fake news article"},  # Fake news 1
    {"text": "This is another fake news article"},  # Fake news 2
    {"text": "This is a real news article"},  # Real news 1
    {"text": "This is another real news article"}  # Real news 2
]

# Perform 100 API calls per test case and record timestamps
results = []

for i, case in enumerate(test_cases):
    case_label = f"Test Case {i+1}"
    for _ in range(100):
        start_time = time.time()
        response = requests.post(url, json=case)
        end_time = time.time()
        latency = end_time - start_time
        results.append([case_label, latency])

# Write results to a CSV file
with open('api_latency_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Test Case", "Latency"])
    writer.writerows(results)

# Read the CSV for analysis
df = pd.read_csv('api_latency_results.csv')

# Boxplot visualization
plt.figure(figsize=(10, 6))
df.boxplot(by='Test Case', column=['Latency'], grid=False)
plt.title('API Latency Boxplot per Test Case')
plt.suptitle('')  # Suppress the default title
plt.xlabel('Test Case')
plt.ylabel('Latency (seconds)')
plt.show()

# Calculate the average latency for each test case
average_latency = df.groupby('Test Case')['Latency'].mean()
print(average_latency)
