try:
    e_n=[2,4,5,6]
    print(e_n[5])
except ZeroDivisionError:
    print("denominater cannot be zero")
except IndexError:
    print("Index out of bound")
    
    