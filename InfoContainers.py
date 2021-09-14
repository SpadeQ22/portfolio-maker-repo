class Student:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.ID = kwargs["ID"]
        self.UEL_ID = kwargs["UEL_ID"]
        self.academic_year = kwargs["academic_year"]
        self.picture_name = kwargs["picture_name"]
        self.program_name = kwargs["program_name"]




class Subject:

    def __init__(self, **kwargs):
        self.ASU_course_code = kwargs["ASU_course_code"]
        self.ASU_course_name = kwargs["ASU_course_name"]
        self.UEL_module_code = kwargs["UEL_module_code"]
        self.UEL_module_name = kwargs["UEL_module_name"]
        self.semester = kwargs["semester"]
        self.instructor_signature = kwargs["instructor_signature"]
        self.assistant_signature = kwargs["assistant_signature"]


class Midterm:

    def __init__(self, **kwargs):
        self.grade = kwargs["grade"]
        self.total = kwargs["total"]
        self.num = 1


class Project:

    def __init__(self, **kwargs):
        self.grade = kwargs["grade"]
        self.total = kwargs["total"]
        self.num = 1


class Quiz:

    def __init__(self, **kwargs):
        self.grade = kwargs["grade"]
        self.total = kwargs["total"]
        self.num = kwargs["num"]


class Assignment:

    def __init__(self, **kwargs):
        self.grade = kwargs["grade"]
        self.total = kwargs["total"]
        self.num = kwargs["num"]


class Lab:

    def __init__(self, **kwargs):
        self.grade = kwargs["grade"]
        self.total = kwargs["total"]
        self.num = kwargs["num"]


class Header:

    def __init__(self):
        self.grade = 0
        self.total = 1
        self.num = 0
