import datetime as dt

class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.ID = kwargs.get("ID")
        self.UEL_ID = kwargs.get("UEL_ID")
        self.now = dt.datetime.now()
        self.year = self.now.year
        if self.now.month < 9:
            self.academic_year = f"{self.year-1}/{self.year}"
        else:
            self.academic_year = f"{self.year}/{self.year+1}"
        self.picture_name = kwargs.get("picture_name")
        self.program_name = kwargs.get("program_name")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")




class Subject:

    def __init__(self, **kwargs):
        self.ASU_course_code = kwargs.get("ASU_course_code")
        self.ASU_course_name = kwargs.get("ASU_course_name")
        self.UEL_module_code = kwargs.get("UEL_module_code")
        self.UEL_module_name = kwargs.get("UEL_module_name")
        self.semester = kwargs.get("semester")
        self.instructor_signature = kwargs.get("instructor_signature")
        self.assistant_signature = kwargs.get("assistant_signature")
        self.midterms: Midterm
        self.project: Project
        self.assignments: Assignment
        self.labs: Lab
        self.quizzes = []


class Midterm:

    def __init__(self, **kwargs):
        self.grade = kwargs.get("grade")
        self.total = kwargs.get("total")
        self.num = 1
        self.file_path = None


class Project:

    def __init__(self, **kwargs):
        self.grade = kwargs.get("grade")
        self.total = kwargs.get("total")
        self.num = 1
        self.file_paths = []


class Quiz:

    def __init__(self, **kwargs):
        self.grade = kwargs.get("grade")
        self.total = kwargs.get("total")
        self.num = kwargs.get("num")
        self.file_path = None


class Assignment:

    def __init__(self, **kwargs):
        self.grade = kwargs.get("grade")
        self.total = kwargs.get("total")
        self.num = kwargs.get("num")
        self.file_paths = []


class Lab:

    def __init__(self, **kwargs):
        self.grade = kwargs.get("grade")
        self.total = kwargs.get("total")
        self.num = kwargs.get("num")
        self.file_paths = []


class Header:

    def __init__(self):
        self.grade = 0
        self.total = 1
        self.num = 0
