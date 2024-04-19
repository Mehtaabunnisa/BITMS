def mehtaab():#using without parameters
    return " This is my bank balance"
test_dict={"fname":mehtaab,"age":19,"address":"ballari"}
print("the original dict is:"+str(test_dict))
res=test_dict["fname"]()#calling function using brackets
print("the required call result:"+str(res))