import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

FIREBASE_KEY_PATH = os.path.join(
    BASE_DIR,
    "shared_resources", "firebase", "serviceAccountKey.json"
)
