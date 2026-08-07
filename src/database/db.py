from src.database.config import supabase

import bcrypt 

def signup_user(email, password):
    print("signup called with", email, password)