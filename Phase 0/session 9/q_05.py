marks = {
    "Ali":85,
    "Ahmed":72,
    "Sara":91,
    "Ayesha":66
}
max_student = {
    "name": "None",
    "marks": marks["Ali"]
}
for k, v in marks.items():
    if v > max_student["marks"]:
        max_student["name"] = k
        max_student["marks"] = v
print(max_student)

min_student = {
    "name": "None",
    "marks": marks["Ali"]
}
for k, v in marks.items():
    if v < min_student["marks"]:
        min_student["name"] = k
        min_student["marks"] = v
print(min_student)

# average marks
avg = 0
cnt = len(marks)
avg = sum(marks.values())/cnt
print(avg)