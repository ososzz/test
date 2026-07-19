# A simple in-memory user database (username: password)
USERS = {
    "admin": "admin123",
    "user": "password123"
}

def login():
    print("--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in USERS and USERS[username] == password:
        print("Login successful! Welcome.")
    else:
        print("Login failed. Incorrect username or password.")

if __name__ == "__main__":
    login()
