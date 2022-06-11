try:

    a = int(input("Enyer number a =>"))
    b = int(input("Enyer number b =>"))
    print("Division of a and b =", (a / b))

except ZeroDivisionError:
    print("Oye only >0")
except:
    print("Errr")

finally:
    print("Last line")