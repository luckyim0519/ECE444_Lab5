import requests
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# The URL of the API
url = 'http://serve-sentiment-env.eba-3jajeqrh.us-east-2.elasticbeanstalk.com/fake_api'

# The text to be sent as a query parameter
test_cases = [
    'This is an example news article to check if it is fake or real.',
    'Breaking news: Local man wins lottery!',
    'Unbelievable! Scientists discover a new planet made entirely of chocolate.',
    'New study shows that drinking coffee can lead to increased productivity.'
]

# Prepare a list to store the response times
response_times = []

# Iterate over each test case
for test_case in test_cases:
    for _ in range(100):  # Send 100 requests for each test case
        start_time = time.time()  # Record the start time
        
        # Sending the GET request to the API
        response = requests.get(url, params={'text': test_case})
        
        # Calculate the response time
        response_time = time.time() - start_time
        
        # Append the response time and test case to the list
        response_times.append({'test_case': test_case, 'response_time': response_time})

        # Optional: Sleep for a short duration to avoid overwhelming the server
        time.sleep(0.1)  # Sleep for 100ms

# Create a DataFrame from the response times list
df = pd.DataFrame(response_times)

# Set up the matplotlib figure
plt.figure(figsize=(12, 6))

# Create a box plot of the response times
sns.boxplot(x='test_case', y='response_time', data=df)

# Adding titles and labels
plt.title('Response Times for API Calls')
plt.xlabel('Test Case')
plt.ylabel('Response Time (seconds)')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit all elements
plt.show()
