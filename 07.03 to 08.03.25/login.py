import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# Login (Make sure you have logged in before to create a session)
username = "seetha_manogaran"
password = "Yashnevathy"

try:
    L.load_session_from_file(username)  # Load saved session
except FileNotFoundError:
    L.login(username, password)  # Login if no session found
    L.save_session_to_file()  # Save session for next time
