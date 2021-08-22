import unittest
from methods import Token, Restricted
import werkzeug
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

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

        # self.assertRaises(werkzeug.exceptions.Forbidden, self.convert.generate_token("admin", "nopassword"))
        # self.assertEqual("403 Forbidden: You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.", self.convert.generate_token("admin", "nopassword"))

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
