Exercise 6
Aim
To create a student management system using classes and objects that allows users to enter student details, calculate average scores, and determine results.
Algorithm
Step 1
:
Start the Program.

Step 2
:
Get user input for the number of students.

Step 3
:
Create an empty list to store student objects.

Step 4
:
Get the name, age, and marks for each student using loops.

Step 5
:
Create a student object and add it to the list.

Step 6
:
Compute the average score and result using different functions.

Step 7
:
Display results for each student.

Step 8
:
Stop the Program.


Program:
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_average_score(self):
        if len(self.marks) > 0:
            return sum(self.marks) / len(self.marks)
        else:
            return 0

    def calculate_result(self):
        average_score = self.calculate_average_score()
        if average_score < 50:
            return "Fail"
        elif average_score < 60:
            return "Second Class"
        elif average_score < 90:
            return "First Class"
        else:
            return "Distinction"

# Create an empty list to store student objects
students = []

# Collect information for multiple students in a loop
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    age = int(input(f"Enter the age of student {i + 1}: "))
    

    marks = []
    for j in range(2):
        subject_mark = float(input(f"Enter the mark for subject {j + 1} for student {i + 1}: "))
        marks.append(subject_mark)

    # Create a Student object and add it to the list
    student = Student(name, age, marks)
    students.append(student)

# Analyze and display student information, including results
print("\nResult(s):")
for i, student in enumerate(students):
    print(f"Student {i + 1}:")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Average Score: {student.calculate_average_score()}")
    result = student.calculate_result()
    print(f"Result: {result}")



Exercise 7

Aim
To develop a student management system using inheritance to manage student details, marks, and grades.
Algorithm
Step 1
:
Start the Program.

Step 2
:
Define the Base Class.

Step 3
:
Define Derived Classes.

Step 4
:
Create Student Instances.

Step 5
:
Input Marks for Undergraduate Student.

Step 6
:
Input Marks for Graduate Student.

Step 7
:
Display Student Academic Information.

Step 8
:
Stop the Program.


Program:
# Class to store and handle personal details of a student
class StudentDetails:
    def __init__(self, name, student_id, programme):
        self.name = name
        self.student_id = student_id
        self.programme = programme  # Store the programme info

    def student_info(self):
        return f"Student ID: {self.student_id}\nName: {self.name}\nProgramme: {self.programme}"


# Class to handle academic details like marks and grades
class Student:
    def __init__(self, student_details):
        self.student_details = student_details  # Composition: Student has a StudentDetails object
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        # Removed the print statement here

    def calculate_grade(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)

        if num_subjects == 0:
            return "No marks available"
        
        percentage = total_marks / num_subjects
        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def student_info(self):
        # Get student's personal details from the StudentDetails object
        personal_info = self.student_details.student_info()
        # Add academic details like marks and grade
        return f"{personal_info}\nMarks: {self.marks}\nGrade: {self.calculate_grade()}"


# Main function to gather input and create student instances
def main():
    # Collect Student Details
    print("Enter Student Details:")
    name = input("Enter Name: ")
    student_id = input("Enter Student ID: ")
    programme = input("Enter Programme (UG/PG): ")  # Ask user for programme (UG or PG)
    
    student_details = StudentDetails(name, student_id, programme)
    
    # Create Student instance for academic details
    student = Student(student_details)
    
    # Get marks for the student
    num_courses = int(input("How many courses' marks should be entered?: "))
    for i in range(1, num_courses + 1):
        marks = float(input(f"Enter the course {i} mark: "))  # Prompt for each course mark
        subject = f"Course {i}"  # Automatically name the subject as "Course X"
        student.add_marks(subject, marks)
    
    # Display student information
    print("\nStudent Academic Information")
    print("----------------------------")
    print(student.student_info())  # Display complete student info


if __name__ == "__main__":
    main()

Output
