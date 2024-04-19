email="mehtaab@gmail.com"
pwd=12345
otp=123456
uemail=str(input("enter email"))
upwd=int(input("enter passwod"))
uotp=int(input("enter otp"))
if(email == uemail):
    if(pwd==upwd):
        print("login sucess")
        if(otp==uotp):
            print("tranction successful")
        else:
            print("tranction denied")
    else:
        print("login failed due to incorrect pwd")
else:
    print("login failed due to incorrect email")