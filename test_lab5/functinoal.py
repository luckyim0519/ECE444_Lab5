import unittest
import requests

class TestNewsAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/predict"  # Replace with your Flask app URL
        
    def test_fake_news(self):
        test_data = {"text": "This is a fake news article"}
        response = requests.post(self.url, json=test_data)
        self.assertEqual(response.json()['prediction'], 'fake')

    def test_real_news(self):
        test_data = {"text": "This is a real news article"}
        response = requests.post(self.url, json=test_data)
        self.assertEqual(response.json()['prediction'], 'real')

if __name__ == '__main__':
    unittest.main()
