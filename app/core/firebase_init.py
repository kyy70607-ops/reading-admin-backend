import os
import json
from google.cloud import firestore
from google.oauth2 import service_account

def get_firestore_client():
    raw = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not raw:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS_JSON is not set")

    credentials_info = json.loads(raw)

    credentials = service_account.Credentials.from_service_account_info(
        credentials_info
    )

    return firestore.Client(
        credentials=credentials,
        project=credentials.project_id
    )
