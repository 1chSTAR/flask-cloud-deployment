# tests/test_app.py

import unittest
from app import app  # adjust the import based on where your app is defined

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)  # Check if "Hello" is in the response

if __name__ == '__main__':
    unittest.main()
