total_days=int(input("Enter the total number of working days:"))
absent_days=int(input("Enter the total number of absent days:"))
attended_days = total_days - absent_days
attendence_percentage = (attended_days / total_days) * 100
if attendence_percentage < 75:
    print("The student will not be able to sit in the exam.")
else:
    print("The student is eligible to sit in the exam.")