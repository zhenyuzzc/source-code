import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'e:/zzc/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'e:/zzc/nusername.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    qr = input(f"请确认用户名 {username} 是否正确 y/n ")
    if qr == 'y':    
        print(f"Welcome back, {username}!")
    elif qr == 'n':
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        print("输入错误")

greet_user()