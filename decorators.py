def grant_access(name):
    user_name=["Ravi","Sumesh","Suresh"]

    def decorator(func):
        def wrapper():
            if name in user_name:
                func()
            else:
                print(f"Access Denied")
        return wrapper
    return decorator

@grant_access('Ravi')
def authorize():
    print(f"Access Granted")
    return authorize

authorize()