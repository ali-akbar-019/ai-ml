name = input("Name: ")
roll_number = input("Roll Number: ")

marks = []
for i in range(5):
    mark = int(input(str(i + 1) + "Subject Marks: "))
    marks.append(mark)

total_marks_of_student = 0
for i in range(5):
    total_marks_of_student += marks[i]

total_marks = 100 * 5
average = total_marks_of_student / 5
print("Total Marks: ", total_marks)
print("Total Marks of Student: ", total_marks_of_student)
print("Average Marks: ", average)
print("Percentage: ", (total_marks_of_student / total_marks) * 100)