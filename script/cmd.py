import os
print("This is on pr")

SECRET_PWDs = ""
SECRET_PWDs = os.environ.get("SECRET_PWD")
if SECRET_PWDs: 
    print("env", os.environ.get("SECRET_PWD"))
else:
    print("env is None")

print("please check the env")
