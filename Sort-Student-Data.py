class Student:
    def __init__(self, name, roll_number, entrance_marks):
        self.name = name
        self.roll_number = roll_number
        self.entrance_marks = entrance_marks


def merge_sort(students, left, right, field):
    if left < right:
        mid = (left + right) // 2
        merge_sort(students, left, mid, field)
        merge_sort(students, mid + 1, right, field)
        merge(students, left, mid, right, field)


def merge(students, left, mid, right, field):
    n1 = mid - left + 1
    n2 = right - mid

    left_list = students[left:left + n1]
    right_list = students[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if field == "name":
            if left_list[i].name <= right_list[j].name:
                students[k] = left_list[i]
                i += 1
            else:
                students[k] = right_list[j]
                j += 1
        elif field == "rollNumber":
            if left_list[i].roll_number <= right_list[j].roll_number:
                students[k] = left_list[i]
                i += 1
            else:
                students[k] = right_list[j]
                j += 1
        elif field == "entranceMarks":
            if left_list[i].entrance_marks <= right_list[j].entrance_marks:
                students[k] = left_list[i]
                i += 1
            else:
                students[k] = right_list[j]
                j += 1
        k += 1

    while i < n1:
        students[k] = left_list[i]
        i += 1
        k += 1

    while j < n2:
        students[k] = right_list[j]
        j += 1
        k += 1


def main():
    students = [
        Student("Bhushan", 1, 95.5),
        Student("Bobby", 2, 88.0),
        Student("Chetan", 3, 92.5),
        Student("Dhiraj", 4, 87.5),
        Student("Elvish Bhai", 5, 34.5),
        Student("Sakshi", 6, 45.0),
        Student("Ghetan", 7, 98.55),
        Student("Sameer", 8, 78.25),
        Student("Dhiraj", 9, 60.78),
        Student("Dhaval", 10, 70.59)
    ]

    print("Choose the field for sorting (1 - Name, 2 - Roll Number, 3 - Entrance Marks):")
    choice = int(input())

    if choice == 1:
        merge_sort(students, 0, len(students) - 1, "name")
    elif choice == 2:
        merge_sort(students, 0, len(students) - 1, "rollNum
