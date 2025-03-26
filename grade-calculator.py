ngrade=int(input("Enter a numeric grade:"))
match ngrade:
    case ngrade if 90 <=ngrade<= 100:
        print("A")
    case ngrade if 80 <=ngrade<= 89:
        print("B")
    case ngrade if 70 <=ngrade<= 79:
        print("C")
    case ngrade if 60 <=ngrade<= 69:
        print("D")
    case ngrade if 0<=ngrade<60:
        print("F")
    case _:
        print("Invalid numeric grade")




