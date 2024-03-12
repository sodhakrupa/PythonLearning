print("Enter student heights space separated\n")
student_heights = input().split()
sum = 0
for height in student_heights:
    sum += float(height)
print(f"Sum of heights is {sum}")
average = round(sum/len(student_heights),2)
print(f"Average height is {average}")