name = input("Enter your name: ")
section = input("Enter you section: ")

prelim = float(input("Enter your Prelim Grade: "))
if prelim < 40 or prelim > 100:
    print("Invalid Grades, please try again.")
else:
    midterm = float(input("Enter your Midterm Grade: "))
    if midterm < 40 or midterm > 100:
        print("Invalid Grades, please try again.")
    else:
        finals = float(input("Enter your Final Grade: "))
        if finals < 40 or finals > 100:
            print("Invalid Grades, please try again.")
        else:
            final_grade = round(prelim * 0.3333 + midterm * 0.3333 + finals * 0.3333)
            if final_grade <= 100 and final_grade >= 99 :
                gpa = 1.00
                desc = "Excellent"
            elif final_grade <= 98 and final_grade >= 96:
                    gpa = 1.25
                    desc = "Outstanding"
            elif final_grade <= 95 and final_grade >= 93:
                    gpa = 1.50
                    desc = "Superior"
            elif final_grade <= 92 and final_grade >= 90:
                    gpa = 1.75
                    desc = "Very Good"
            elif final_grade <= 89 and final_grade >= 87:
                    gpa = 2.00
                    desc = "Good"
            elif final_grade <= 86 and final_grade >= 84:
                    gpa = 2.25
                    desc = "Satisfactory"
            elif final_grade <= 83 and final_grade >= 81:
                    gpa = 2.50
                    desc = "Fairly Satisfactory"
            elif final_grade <= 80 and final_grade >= 78:
                    gpa = 2.75
                    desc = "Fair"
            elif final_grade <= 77 and final_grade >= 75:
                    gpa = 3.00
                    desc = "Passed"
            else:
                final_grade > 75
                gpa = 5.00
                desc = "Failed"

print(f"Final Grade: {final_grade}%")
print(f"GPA: {gpa}")
print(f"Congrats! you did a {desc} job")
