import firebase_admin
from firebase_admin import credentials, firestore
import os
from app.core.config import FIREBASE_KEY_PATH

cred = credentials.Certificate(FIREBASE_KEY_PATH)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
