import secrets

password_length = int(input("Enter password length: "))
print(secrets.token_urlsafe(password_length))
