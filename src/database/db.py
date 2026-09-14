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
                return True, user
        return False, "Incorrect username or password"
    except Exception as e:
        return False, "Something went wrong, please try again"
    
    
# Save sessions
def save_session(user_id, transcript, feedback):
    try:
        supabase.table("sessions").insert({
            "user_id": user_id,
            "transcript": transcript,
            "grammar_score": feedback["grammar_score"],
            "fluency_score": feedback["fluency_score"],
            "grammar_feedback": feedback["grammar_feedback"],
            "fluency_feedback": feedback["fluency_feedback"],
            "suggestion": feedback["suggestion"],
        }).execute()
        return True, "Session saved"
    except Exception as e:
        return False, "Could not save session"
    
# function to fetch user info

def get_user_sessions(user_id):
    try:
        response = supabase.table("sessions").select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        return []