def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('logged_in', False):
            return "Access Denied!"
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    return f"Profile: {user['name']}"

user1 = {'name': "ali", "logged_in": True}
user2 = {'name': "guest", "logged_in": False}
print(view_profile(user1))
print(view_profile(user2))