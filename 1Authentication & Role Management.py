# ============================================================
# MODULE 1
# Authentication & Role Management
# ============================================================

users = {
    "student": {
        "password": "student123",
        "role": "User / Student"
    },

    "admin": {
        "password": "admin123",
        "role": "Traffic Authority"
    }
}


def authenticate(username, password, role):

    if username in users:

        if users[username]["password"] == password:

            if users[username]["role"] == role:
                return True

    return False


def get_user_role(username):

    if username in users:
        return users[username]["role"]

    return "Unknown"


# ------------------------------------------------------------
# Run Module 1 separately
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("MODULE 1")
    print("Authentication & Role Management")
    print("======================================")

    username = input("Enter username: ")
    password = input("Enter password: ")

    print("\n1. User / Student")
    print("2. Traffic Authority")

    choice = input("Enter role choice: ")

    if choice == "1":
        role = "User / Student"
    else:
        role = "Traffic Authority"

    if authenticate(username, password, role):

        print("\nAuthentication Successful")
        print("Username:", username)
        print("Role:", role)

    else:

        print("\nAuthentication Failed")