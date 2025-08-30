import unittest
from firebase_db import add_user, verify_user
import os

class TestUserAuthentication(unittest.TestCase):

    def setUp(self):
        if not os.environ.get("FIREBASE_DB_JSON_PATH"):
            self.skipTest("FIREBASE_DB_JSON_PATH environment variable is not set.")

    def test_add_and_verify_user_u1(self):
        # Test adding and verifying a simple user
        user_id = "U1"
        password = "1234"
        success, error = add_user(user_id, password)
        self.assertTrue(success)
        self.assertIsNone(error)

        verified, error = verify_user(user_id, password)
        self.assertTrue(verified)
        self.assertIsNone(error)

    def test_add_and_verify_user_u2(self):
        # Test adding and verifying a user with a complex password
        user_id = "U2"
        password = "abcd124!@3"
        success, error = add_user(user_id, password)
        self.assertTrue(success)
        self.assertIsNone(error)

        verified, error = verify_user(user_id, password)
        self.assertTrue(verified)
        self.assertIsNone(error)

    def test_verify_wrong_password_u1(self):
        # Test verifying a user with a wrong password
        user_id = "U1"
        password = "wrong_password"
        verified, error = verify_user(user_id, password)
        self.assertFalse(verified)
        self.assertIsNone(error)

    def test_verify_wrong_password_u2(self):
        # Test verifying a user with a wrong password
        user_id = "U2"
        password = "wrong_password"
        verified, error = verify_user(user_id, password)
        self.assertFalse(verified)
        self.assertIsNone(error)

    def test_verify_nonexistent_user(self):
        # Test verifying a non-existent user
        user_id = "nonexistent_user"
        password = "some_password"
        verified, error = verify_user(user_id, password)
        self.assertFalse(verified)
        self.assertIsNone(error)

if __name__ == '__main__':
    unittest.main()
