import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.core.firebase_init import db
from app.core.security import hash_password

email = input("メールアドレス: ")
password = input("パスワード: ")

db.collection("admins").document(email).set({
    "email": email,
    "password": hash_password(password)
})

print("管理者アカウントを作成しました。")
