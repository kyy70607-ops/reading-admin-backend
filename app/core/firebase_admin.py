import os
import json
import firebase_admin
from firebase_admin import credentials, auth, firestore

def init_firebase():
    if not firebase_admin._apps:
        cred_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
        if not cred_json:
            raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS_JSON is not set")

        cred = credentials.Certificate(json.loads(cred_json))
        firebase_admin.initialize_app(cred)

def get_firestore():
    init_firebase()
    return firestore.client()

def verify_token(id_token: str):
    init_firebase()
    return auth.verify_id_token(id_token)
