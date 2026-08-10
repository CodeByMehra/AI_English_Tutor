from src.database.config import supabase

import bcrypt 

def signup_user(email, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(hashed)