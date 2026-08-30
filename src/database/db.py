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
    
# Function to check password in login process
def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())
    
# function for user login
def login_user(username, password):
    try:
        response = supabase.table("users").select("*").eq("username", username).execute()
        if response.data:
            user = response.data[0]
            if check_pass(password, user["password"]):
                return user
    except Exception as e:
            return False, "Wrong username or password!"