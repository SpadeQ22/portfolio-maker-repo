

class Student:
    def __init__(self, name, picture_name, ID, UEL_ID, program_name, academic_year):
        self.name = name
        self.ID = ID
        self.UEL_ID = UEL_ID
        self.program_name = program_name
        self.academic_year = academic_year
        self.picture_name = picture_name


class Subject:

    def __init__(self, ASU_course_code, UEL_module_code,
                 ASU_course_name, UEL_module_name, semester, instructor_signature, assistant_signature):
        self.ASU_course_code = ASU_course_code
        self.ASU_course_name = ASU_course_name
        self.UEL_module_code = UEL_module_code
        self.UEL_module_name = UEL_module_name
        self.semester = semester
        self.instructor_signature = instructor_signature
        self.assistant_signature = assistant_signature


class Midterm:

    def __init__(self, grade, total):
        self.grade = grade
        self.total = total


class Project:

    def __init__(self, grade, total):
        self.grade = grade
        self.total = total


class Quiz:

    def __init__(self, grade, total, no):
        self.grade = grade
        self.total = total
        self.no = no


class Assignment:

    def __init__(self, grade, total, no):
        self.grade = grade
        self.total = total
        self.no = no


class Lab:

    def __init__(self, grade, total, no):
        self.grade = grade
        self.total = total
        self.no = no
