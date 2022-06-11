class InvalidMarks(Exception):
    pass

try:
    a = int(input("Enter marks of english =>"))
    b = int(input("Enter marks of hindi =>"))

    if a<0:
        raise InvalidMarks
    elif b<0:
        raise InvalidMarks
    else:
        print("Total marks =",(a+b))

except InvalidMarks:
    print("Please Enter valid marks")
except:
    print("Other error")