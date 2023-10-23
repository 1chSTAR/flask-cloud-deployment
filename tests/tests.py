# tests/test_app.py

import unittest
from flask_web_app.app import app  # adjust the import based on where your app is defined

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_get(self):
        """Test the home page with a GET request."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Since we're not sure about the specific content in a GET request, 
        # we just check for a successful response.
        # If there's a consistent string on every GET request, you can assert for its presence.

    def test_home_page_post(self):
        """Test the home page with a POST request and a name."""
        response = self.app.post('/', data={'name': 'aws'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, aws!', response.data)

    def test_home_page_post_without_name(self):
        """Test the home page with a POST request without a name."""
        response = self.app.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Hello,', response.data)  # Ensure no greeting when no name is provided

if __name__ == '__main__':
    unittest.main()
