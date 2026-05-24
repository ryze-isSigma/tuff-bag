print("gurvaljin 3 tal oruul")

a = float(input("1 r tal "))
b = float(input("2 r tal "))
c = float(input("3 r tal "))

if a + b <= c or a + c <= b or b + c <= a:
    print("gurvanjin bish")
else:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            print("tegsh ontsogt gurvalkin")
        elif a*a + b*b > c*c and a*a + c*c > b*b and b*b + c*c > a*a:
            print("hurts ontsgot gurvaljin")
        else:
            print("mohoi ontsogt gurvaljin")