from src.database.config import supabase

import bcrypt 

def signup_user(name, username, email, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        supabase.table("users").insert({
            "name": name,
            "username": username,
            "email": email,
            "password": hashed.decode('utf-8')
        }).execute()
        return True, "Signup successful"
    except Exception as e:
        return False, "Username or email already exists"