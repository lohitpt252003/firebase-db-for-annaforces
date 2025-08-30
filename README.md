
# Firebase Authentication with Argon2 Hashing

This project provides a simple Python module for user authentication using Firebase Firestore and Argon2 for password hashing.

## Features

- User creation with hashed passwords
- User password verification
- Secure password hashing using Argon2
- Integration with Firebase Firestore

## Prerequisites

- Python 3
- A Google Firebase project
- A Firebase service account key (in JSON format)

## Installation

1. Clone the repository:
   ```bash
   git clone https://your-repo-url.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set the `FIREBASE_DB_JSON_PATH` environment variable:**

   This environment variable should point to the absolute path of your Firebase service account key JSON file.

   **For Windows:**
   ```bash
   set FIREBASE_DB_JSON_PATH="path\to\your\serviceAccountKey.json"
   ```

   **For Linux and macOS:**
   ```bash
   export FIREBASE_DB_JSON_PATH="/path/to/your/serviceAccountKey.json"
   ```

## Usage

The `firebase_db.py` module provides the following functions:

- `add_user(user_id, password)`: Adds a new user to the Firestore database with a hashed password.
- `verify_user(user_id, password)`: Verifies the password of an existing user.

### Example

```python
from firebase_db import add_user, verify_user

# Add a new user
add_user("new_user", "password123")

# Verify the user
if verify_user("new_user", "password123"):
    print("User verified successfully!")
else:
    print("User verification failed.")
```

## Testing

To run the tests, execute the following command:

```bash
python test.py
```

**Note:** Make sure you have set the `FIREBASE_DB_JSON_PATH` environment variable before running the tests.

## Credits

This project was created by [Your Name].

## Contributors

- [LOHIT P TALAVAR (Owner)](https://github.com/lohitpt252003)
- [PRIYANSHI MEENA](https://github.com/MeenaPriyanshi)

## Thanks (CREDITS)

Special thanks to the developers of the following libraries:

- [Firebase Admin SDK for Python](https://firebase.google.com/docs/admin/setup)
- [argon2-cffi](https://argon2-cffi.readthedocs.io/en/stable/)