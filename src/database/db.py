from src.database.config import supabase

import bcrypt 

def signup_user(name, username, email, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(hashed)
    supabase.table("users").insert({
    "email": email,
    "password": hashed.decode('utf-8')
    }).execute()