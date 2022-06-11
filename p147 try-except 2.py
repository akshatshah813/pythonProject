try:
    a = int(input("Enter marks of english =>"))
    b = int(input("Enter marks of hindi =>"))

    if a<0:
        print("Enter valid marks in English")
    elif b<0:
        print("Enter valid marks in hindi")
    else:
        print("Total marks =",(a+b))
except:
    print("Other error")