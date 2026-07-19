import hashlib
import json
import os

# Path to store the user credentials
DB_FILE = "users_db.json"

def load_database():
    """Load users from the JSON database file."""
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: Database file is corrupted. Starting with an empty database.")
        return {}

def save_database(database):
    """Save users to the JSON database file."""
    with open(DB_FILE, "w") as f:
        json.dump(database, f, indent=4)

def hash_password(password, salt=None):
    """Hash password using SHA-256 with a salt."""
    if salt is None:
        # Generate a random 16-character salt
        salt = os.urandom(16).hex()
    
    # Hash the password combined with the salt
    hashed = hashlib.sha256((password + salt).encode("utf-8")).hexdigest()
    return hashed, salt

def register_user(database):
    """Register a new user."""
    print("\n--- User Registration ---")
    username = input("Enter a username: ").strip()
    
    if not username:
        print("Username cannot be empty.")
        return
    
    if username in database:
        print("Username already exists. Please choose a different one.")
        return

    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Registration failed.")
        return

    # Hash the password and save
    hashed, salt = hash_password(password)
    database[username] = {
        "hashed_password": hashed,
        "salt": salt
    }
    save_database(database)
    print(f"User '{username}' registered successfully!")

def login_user(database):
    """Log in an existing user."""
    print("\n--- User Login ---")
    username = input("Username: ").strip()
    password = input("Password: ")

    if username not in database:
        print("Invalid username or password.")
        return

    user_data = database[username]
    stored_hash = user_data["hashed_password"]
    salt = user_data["salt"]

    # Verify password
    hashed, _ = hash_password(password, salt)
    if hashed == stored_hash:
        print(f"\nWelcome back, {username}! Login successful.")
    else:
        print("Invalid username or password.")

def main():
    database = load_database()
    
    while True:
        print("\n=========================")
        print("   CONSOLE LOGIN SYSTEM  ")
        print("=========================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            login_user(database)
        elif choice == "2":
            register_user(database)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
