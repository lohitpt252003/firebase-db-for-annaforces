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

1. **Set the `FIREBASE_CREDENTIALS` environment variable:**

   This environment variable should contain the *entire JSON content* of your Firebase service account key. It is crucial that the value is a single, unquoted JSON string.

   **Example of setting directly in your shell (replace with your actual JSON):**

   **For Windows (using Command Prompt):**
   ```cmd
   set FIREBASE_CREDENTIALS={"type": "service_account", "project_id": "your-project-id", ...}
   ```

   **For Linux and macOS (using Bash/Zsh):**
   ```bash
   export FIREBASE_CREDENTIALS='{"type": "service_account", "project_id": "your-project-id", ...}'
   ```

   **Using a `.env` file:**
   You can also place this variable in a `.env` file in the project root. Ensure the JSON content is on a single line and not enclosed in extra quotes (unless your shell requires it for `export` commands, as shown above).
   ```
   FIREBASE_CREDENTIALS={"type": "service_account", "project_id": "your-project-id", ...}
   ```

## Usage

The `firebase_db.py` module provides the following functions:

- `add_user(user_id, password)`: Adds a new user to the Firestore database with a hashed password.
- `verify_user(user_id, password)`: Verifies the password of an existing user. Returns `(True, None)` on success, `(False, None)` if password verification fails, or `(None, error_message)` if there's a database error or the user is not found.

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

**Note:** The `test.py` script will attempt to read the `FIREBASE_CREDENTIALS` from a `.env` file in the project root if the environment variable is not already set in your shell.

## Credits

This project was created by [Your Name].

## Contributors

- [LOHIT P TALAVAR (Owner)](https://github.com/lohitpt252003)
- [PRIYANSHI MEENA](https://github.com/MeenaPriyanshi)

## Thanks (CREDITS)

Special thanks to the developers of the following libraries:

- [Firebase Admin SDK for Python](https://firebase.google.com/docs/admin/setup)
- [argon2-cffi](https://argon2-cffi.readthedocs.io/en/stable/)