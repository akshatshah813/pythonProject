try:
    a = int(input("Enyer number a =>"))
    b = int(input("Enyer number b =>"))
    print("Division of a and b =", (a / b))

except ZeroDivisionError:
    print(" Bro why u entered 0")
except ValueError:
    print("Why you entered characters")
except:
    print("Other Error")