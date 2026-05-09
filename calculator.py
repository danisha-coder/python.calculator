import math
import statistics
import numpy as np

while True:
    print("\n===== ALL IN ONE CALCULATOR =====")
    print("1. Quadratic Equation Solver")
    print("2. Factorial Calculator")
    print("3. Matrix Operations")
    print("4. Determinant Calculator")
    print("5. Square Root Calculator")
    print("6. Power Calculator")
    print("7. Linear Equation Solver")
    print("8. Inverse Matrix Calculator")
    print("9. Temperature Converter")
    print("10. Length Converter")
    print("11. Area of Shapes")
    print("12. Volume of Shapes")
    print("13. Weight Converter")
    print("14. Time Converter")
    print("15. Speed Converter")
    print("16. Number System Converter")
    print("17. Logarithm Calculator")
    print("18. Exponential Calculator")
    print("19. Percentage Calculator")
    print("20. Mean Median Mode")
    print("21. Trigonometric Functions")
    print("22. Degree to Radian")
    print("0. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = b**2 - 4*a*c
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Roots =", x1, x2)

    elif choice == 2:
        n = int(input("Enter Number: "))
        print("Factorial =", math.factorial(n))

    elif choice == 3:
        A = np.array([[1,2],[3,4]])
        B = np.array([[5,6],[7,8]])
        print("Addition:\n", A+B)
        print("Subtraction:\n", A-B)
        print("Multiplication:\n", A.dot(B))

    elif choice == 4:
        A = np.array([[1,2],[3,4]])
        print("Determinant =", np.linalg.det(A))

    elif choice == 5:
        n = float(input("Enter Number: "))
        print("Square Root =", math.sqrt(n))

    elif choice == 6:
        a = float(input("Base: "))
        b = float(input("Power: "))
        print("Result =", a**b)

    elif choice == 7:
        a = float(input("a: "))
        b = float(input("b: "))
        print("x =", -b/a)

    elif choice == 8:
        A = np.array([[1,2],[3,4]])
        print("Inverse Matrix:\n", np.linalg.inv(A))

    elif choice == 9:
        c = float(input("Enter Celsius: "))
        f = (c*9/5)+32
        print("Fahrenheit =", f)

    elif choice == 10:
        m = float(input("Meters: "))
        print("Feet =", m*3.28084)

    elif choice == 11:
        r = float(input("Circle Radius: "))
        print("Area =", math.pi*r*r)
        print("Perimeter =", 2*math.pi*r)

    elif choice == 12:
        r = float(input("Sphere Radius: "))
        print("Volume =", (4/3)*math.pi*r**3)

    elif choice == 13:
        kg = float(input("Kilograms: "))
        print("Pounds =", kg*2.20462)

    elif choice == 14:
        sec = float(input("Seconds: "))
        print("Minutes =", sec/60)

    elif choice == 15:
        ms = float(input("m/s: "))
        print("km/h =", ms*3.6)

    elif choice == 16:
        n = int(input("Decimal Number: "))
        print("Binary =", bin(n))
        print("Octal =", oct(n))
        print("Hexadecimal =", hex(n))

    elif choice == 17:
        n = float(input("Enter Number: "))
        print("Natural Log =", math.log(n))
        print("Log Base10 =", math.log10(n))

    elif choice == 18:
        n = float(input("Enter Number: "))
        print("e^x =", math.exp(n))

    elif choice == 19:
        total = float(input("Total: "))
        part = float(input("Part: "))
        print("Percentage =", (part/total)*100)

    elif choice == 20:
        nums = list(map(int, input("Enter Numbers: ").split()))
        print("Mean =", statistics.mean(nums))
        print("Median =", statistics.median(nums))
        print("Mode =", statistics.mode(nums))

    elif choice == 21:
        deg = float(input("Enter Degree: "))
        rad = math.radians(deg)
        print("Sin =", math.sin(rad))
        print("Cos =", math.cos(rad))
        print("Tan =", math.tan(rad))

    elif choice == 22:
        deg = float(input("Degree: "))
        print("Radian =", math.radians(deg))

    elif choice == 0:
        print("Thank You")
        break

    else:
        print("Invalid Choice")