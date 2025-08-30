import firebase_admin
import os
from firebase_admin import credentials, firestore
from argon2 import PasswordHasher
from dotenv import load_dotenv

load_dotenv()

# Load the path to the service account key from the environment variable
cred_path = os.environ.get("FIREBASE_DB_JSON_PATH")

if not cred_path:
    db = None
    ph = None
else:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    ph = PasswordHasher()

def get_user(user_id):
    if not db:
        return None, "Database not initialized. FIREBASE_DB_JSON_PATH not set."
    doc_ref = db.collection(u'users').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict(), None
    else:
        return None, None

def add_user(user_id, password):
    if not db:
        return None, "Database not initialized. FIREBASE_DB_JSON_PATH not set."
    hashed_password = ph.hash(password)
    doc_ref = db.collection(u'users').document(user_id)
    doc_ref.set({
        u'password': hashed_password
    })
    return True, None

def verify_user(user_id, password):
    if not db:
        return None, "Database not initialized. FIREBASE_DB_JSON_PATH not set."
    user_data, error = get_user(user_id)
    if error:
        return None, error
    if user_data:
        try:
            ph.verify(user_data['password'], password)
            return True, None
        except Exception:
            return False, None
    else:
        return False, None