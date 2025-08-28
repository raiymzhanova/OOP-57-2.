#1
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def say_hello():
    return "hello, world"

print(say_hello())



#2
def require_admin(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        if user == "admin":
            return func(*args, **kwargs)
        else:
            print("Access denied")
    return wrapper

@require_admin
def delete_database(user):
    print("Database deleted!")

#Проверка
delete_database("admin")
delete_database("user1")