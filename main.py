def max_no(my_list: list):  # max_mark
    max_no = my_list[0]
    for i in my_list:
        if i > max_no:
            max_no = i
    print("max mark =", max_no)


def min_no(my_list: list):  # min_mark
    max_no = my_list[0]
    for i in my_list:
        if i < max_no:
            max_no = i
    print("min mark =", max_no)

studant_count = int(input("enter number of studant:"))
marks_count = int(input("enter number of marks:"))
my_studants = []
for i in range(0, studant_count):
    student = (input(f"enter name of student{i + 1}:"))
    my_studants.append(student)
    studant_marks = []
    sum = 0
    for j in range(0, marks_count):
        mark = int(input(f"enter mark{j + 1} of studant {my_studants[i]}:"))
        studant_marks.append(mark)
        sum += studant_marks[j]

    average = sum / marks_count
    max_no(studant_marks)
    min_no(studant_marks)
    print(f"avrge of marks =", average)
