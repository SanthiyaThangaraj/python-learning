calculate_grade=int(input("Enter a numeric grade:"))
match calculate_grade:
    case calculate_grade if 90 <=calculate_grade<= 100:
        print("A")
    case calculate_grade if 80 <=calculate_grade<= 89:
        print("B")
    case calculate_grade if 70 <=calculate_grade<= 79:
        print("C")
    case calculate_grade if 60 <=calculate_grade<= 69:
        print("D")
    case calculate_grade if 0<=calculate_grade<60:
        print("F")
    case _:
        print("Invalid numeric grade")




