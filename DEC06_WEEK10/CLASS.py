student1_name = "ZILONG"
student1_grade = "1.75"
student1_subject = "FIGHTER"

student2_name = "JOY"
student2_grade = "2.5"
student2_subject = "ASSASSIN"

student3_name = "WANWAN"
student3_grade = "5"
student3_subject = "MARKSMAN"

def print_student_info_function(name, grade, subject):
    print(f"Student {name} - grade is {grade} - subject is {subject}")

if __name__ == "__main__":
    print_student_info_function(student1_name, student1_grade, student1_name)
    print_student_info_function(student2_name, student2_grade, student2_name)
    print_student_info_function(student3_name, student3_grade, student3_name)

#CLASS
class Student:
    default_subject = "Mobile Legends"
    year_and_section = "1-2"

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"Name {self.name} - grade is {self.grade} - subject is {self.subject}")

    @classmethod
    def print_student_info_class_method(cls, name, grade):
        print(f"Student {name} - grade is {grade} - subject is {cls.default_subject}")
        return cls(name, grade, cls.default_subject)

    @classmethod
    def update_year_and_section(cls, year_section_update):
        cls.year_and_section = year_section_update

    @staticmethod
    def is_passing_grade(grade):
        if grade <= 3:
            print("passed, congrats")
        else:
            print("did not passed, nice try")


#--------------------------------------------------------------------------------------------------------------------------
print("#-------------------------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    student1 = Student("ZILONG", 1.75, "FIGHTER")
    student2 = Student("JOY", 2.5, "ASSASSIN")
    student3 = Student("WANWAN", 5, "MARKSMAN")
    student4 = Student.print_student_info_class_method("FLORYN", "1.75")

    student1.print_student_info_method()
    student2.print_student_info_method()
    student3.print_student_info_method()

    Student.is_passing_grade(4.75)
    Student.is_passing_grade(student1.grade)
    Student.is_passing_grade(student2.grade)
    Student.is_passing_grade(student3.grade)

    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)
    Student.update_year_and_section("2-4")
    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)