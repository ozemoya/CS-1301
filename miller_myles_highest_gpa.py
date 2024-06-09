class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty")
        return max(self.roster, key=lambda student: student.get_gpa())

def main():
    course = Course()
    while True:
        first_name = input("Enter student's first name (or 'stop' to end): ")
        if first_name.lower() == 'stop':
            break
        last_name = input("Enter student's last name: ")
        try:
            gpa = float(input("Enter student's GPA: "))
            course.add_student(Student(first_name, last_name, gpa))
        except ValueError:
            print("Invalid GPA. Please enter a numeric value.")

    print(f"Number of students in the course: {course.course_size()}")
    try:
        top_student = course.find_student_highest_gpa()
        print(f"Top student: {top_student.get_first()} {top_student.get_last()}, GPA: {top_student.get_gpa()}")
    except EmptyRosterError as e:
        print(e)

if __name__ == "__main__":
    main()
