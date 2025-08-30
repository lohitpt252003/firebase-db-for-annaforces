from firebase_db import add_user, verify_user
import os

def run_tests():
    if not os.environ.get("FIREBASE_DB_JSON_PATH"):
        print("Please set the FIREBASE_DB_JSON_PATH environment variable to run the tests.")
        return

    # Test 1: Add and verify a simple user
    print("Running Test 1: Add and verify user U1")
    user_id_1 = "U1"
    password_1 = "1234"
    success, error = add_user(user_id_1, password_1)
    assert success and not error, "Test 1 Failed: Could not add user U1"
    verified, error = verify_user(user_id_1, password_1)
    assert verified and not error, "Test 1 Failed: Could not verify user U1"
    print("Test 1 Passed!")

    # Test 2: Add and verify a user with a complex password
    print("\nRunning Test 2: Add and verify user U2")
    user_id_2 = "U2"
    password_2 = "abcd124!@3"
    success, error = add_user(user_id_2, password_2)
    assert success and not error, "Test 2 Failed: Could not add user U2"
    verified, error = verify_user(user_id_2, password_2)
    assert verified and not error, "Test 2 Failed: Could not verify user U2"
    print("Test 2 Passed!")

    # Test 3: Verify user U1 with a wrong password
    print("\nRunning Test 3: Verify user U1 with wrong password")
    wrong_password_1 = "wrong_password"
    verified, error = verify_user(user_id_1, wrong_password_1)
    assert not verified and not error, "Test 3 Failed: Verified user U1 with wrong password"
    print("Test 3 Passed!")

    # Test 4: Verify user U2 with a wrong password
    print("\nRunning Test 4: Verify user U2 with wrong password")
    wrong_password_2 = "wrong_password"
    verified, error = verify_user(user_id_2, wrong_password_2)
    assert not verified and not error, "Test 4 Failed: Verified user U2 with wrong password"
    print("Test 4 Passed!")

    # Test 5: Verify a non-existent user
    print("\nRunning Test 5: Verify non-existent user")
    non_existent_user = "nonexistent_user"
    password_5 = "some_password"
    verified, error = verify_user(non_existent_user, password_5)
    assert not verified and not error, "Test 5 Failed: Verified a non-existent user"
    print("Test 5 Passed!")

if __name__ == '__main__':
    run_tests()