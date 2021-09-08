import random

from Autofill.filler import Filler
from Autofill.InfoToReplace import Subject, Midterm, Project, Quiz, Lab, Assignment, Student


templates = ['Header Template.docx', 'Assignments Template.docx', 'Quizzes Template.docx', 'Lab Template.docx',
             'Project Template.docx']

student = Student("Hussein", 'placeholder.png', 2021, 123, "CESS", 2021)
subject = Subject("cse111", "uel111",
                  "programming", "programminguel", "fall", "Ahmed", "marwa")
midterm = Midterm(20, 25)
project = Project(9, 10)
lab1 = Lab(8, 10, 1)
lab2 = Lab(9, 10, 2)
ass1 = Assignment(5, 10, 1)
ass2 = Assignment(8, 10, 2)
quiz1 = Quiz(10, 10, 1)
quiz2 = Quiz(9, 10, 2)


def createSubjectObjectFiller(subjectObject):


   # takes quiz, assignment...objects and creates a filler for their templates

    i = input("Press:\n1 for :" + templates[0] +
              "\n2 for :" + templates[1] +
              "\n3 for :" + templates[2] +
              "\n4 for :" + templates[3] +
              "\n5 for :" + templates[4])
    template_name = templates[int(i)]

    fill = Filler(subjectObject.grade, subjectObject.grade)
    fill.infoToReplace(template_name, student.name, student.picture_name, student.program_name, student.academic_year
                       , student.ID, student.UEL_ID, subject.ASU_course_code, subject.UEL_module_code,
                       subject.ASU_course_name, subject.UEL_module_name, subject.semester, subjectObject.grade,
                       subject.instructor_signature, subject.assistant_signature)


createSubjectObjectFiller(quiz1)