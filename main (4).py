class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Function to display a list of students
def display_students(student_list):
    for student in student_list:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

# Test the function with different input lists of students
students_list1 = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.6),
    Student("Charlie", "C003", 3.9),
]

students_list2 = [
    Student("David", "D004", 3.5),
    Student("Eva", "E005", 3.7),
    Student("Frank", "F006", 3.4),
]

# Sort and display the students in descending order of CGPA
sorted_students1 = sort_students(students_list1)
sorted_students2 = sort_students(students_list2)

print("Sorted Students List 1:")
display_students(sorted_students1)

print("\nSorted Students List 2:")
display_students(sorted_students2)