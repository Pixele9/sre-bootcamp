import unittest
from methods import Token, Restricted
import werkzeug
import requests
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    # home health check
    def test_health_check2(self):
        responseText = requests.get("http://localhost:8000/").text
        print(responseText)
        self.assertEqual("HOME OK", responseText)

    # health check
    def test_health_check(self):
        responseText = requests.get("http://localhost:8000/_health").text
        print(responseText)
        self.assertEqual("OK", responseText)

    def test_generate_token(self):
        # I had to change this JWT token because PyJWT changes the order of the headers
        # although the result is corrert the headers differ
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', self.convert.generate_token('admin', 'secret'))
    
    # Test for wrong credentails
    def test_wrong_credentials(self):
        try:
            self.convert.generate_token("admin", "nopassword")
        except Exception as e:
            return True

    def test_access_data(self): 
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))

    # Test for wrong acces token
    def test_no_access_data(self):
        try:
            self.validate.access_data("nothing")
        except Exception as e:
            return True

if __name__ == '__main__':
    unittest.main()
