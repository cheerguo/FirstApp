import os
print("This is on pr")

SECRET_PWDs = ""
SECRET_PWDs = os.environ.get("SECRET_PWDs")
if SECRET_PWDs: 
    print("env", os.environ.get("SECRET_PWDs"))
else:
    print("env is None")
