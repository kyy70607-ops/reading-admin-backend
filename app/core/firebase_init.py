# app/core/firebase_init.py
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

def get_firestore_client():
    if firebase_admin._apps:
        return firestore.client()

    cred_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not cred_json:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS_JSON is not set")

    cred_dict = json.loads(cred_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

    return firestore.client()
