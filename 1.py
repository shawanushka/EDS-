for i in range(1, 6):
    marks = float(input(f"Enter marks of student {i}: "))

    if marks >= 40:
        print("Result: Passed")

        if marks > 75:
            print("Grade: Distinction")
        elif marks >= 60:
            print("Grade: First Class")
        elif marks >= 50:
            print("Grade: Second Class")
        else:
            print("Grade: Just Pass")
    else:
        print("Result: Failed")