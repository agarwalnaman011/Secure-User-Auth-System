import hashlib
import mysql.connector

# Setup connection to your local MySQL instance
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Replace with your MySQL username
        password="agarwaln",  # Replace with your MySQL password
        database="SecureAuthDB"
    )

# 1. SHA-256 Hashing Mechanism
def hash_password(password):
    # Encodes string to bytes, runs SHA-256, and returns 64-character hexadecimal string
    return hashlib.sha256(password.encode()).hexdigest()

# 2. Secure Registration Function
def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Generate the secure hash instead of saving the plain text
    secure_hash = hash_password(password)
    
    # Parameterized query to safely prevent SQL Injection vulnerabilities
    query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    
    try:
        cursor.execute(query, (username, secure_hash))
        conn.commit()
        print(f"✔️ User '{username}' successfully registered!")
    except mysql.connector.Error as err:
        print(f"❌ Error: Username might already exist or database issue. ({err})")
    finally:
        cursor.close()
        conn.close()

# 3. Secure Login/Authentication Function
def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hash the input password to see if it matches what is stored
    input_hash = hash_password(password)
    
    # Parameterized verification query
    query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
    
    cursor.execute(query, (username, input_hash))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result:
        print("🔓 Access Granted: Successful Secure Authentication!")
        return True
    else:
        print("🔒 Access Denied: Invalid credentials.")
        return False

# --- Quick Local Testing Environment ---
if __name__ == "__main__":
    print("--- Registering a New User Securely ---")
    register_user("naman_cyber", "MySuperSecretPassword123")
    
    print("\n--- Trying to Login with Correct Password ---")
    login_user("naman_cyber", "MySuperSecretPassword123")
    
    print("\n--- Trying to Login with Wrong Password ---")
    login_user("naman_cyber", "WrongPassword125")