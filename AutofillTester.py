from Autofill.filler import Filler
from Autofill.InfoToReplace import Subject, Midterm, Project, Quiz, Lab, Assignment, Student

templates = ['Autofill/Templates and pictures/Header Template.docx',
             'Autofill/Templates and pictures/Assignment Template.docx',
             'Autofill/Templates and pictures/Quiz Template.docx', 'Autofill/Templates and pictures/Lab Template.docx',
             'Autofill/Templates and pictures/Project Template.docx']

student1 = Student("Hussein", 'placeholder.png', 2021, 123, "CESS", 2021)
subject1 = Subject("cse111", "uel111",
                   "programming", "programminguel", "fall", "Ahmed", "marwa")
midterm = Midterm(20, 25)
project = Project(9, 10)
lab1 = Lab(8, 10, 1)
lab2 = Lab(9, 10, 2)
ass1 = Assignment(5, 10, 1)
ass2 = Assignment(8, 10, 2)
quiz1 = Quiz(10, 10, 1)
quiz2 = Quiz(9, 10, 2)


def createSubjectSliceFiller(student, subject, subjectSlice):
    """
    Creates a filler object to process grade markers and to replace all info passed in a given template

    :param student: takes student object to pass its parameter to infoToReplace method
    :param subject: takes subject object to pass its parameter to infoToReplace method
    :param subjectSlice: takes a slice (eg. lab, midterm...) of a subject
    :return: the results of infoToReplace
    """
    # takes quiz, assignment...objects and creates a filler for their templates

    i = input("Press:\n0 for :" + templates[0] +
              "\n1 for: " + templates[1] +
              "\n2 for: " + templates[2] +
              "\n3 for: " + templates[3] +
              "\n4 for: " + templates[4])
    template_name = templates[int(i)]

    fill = Filler(grade=subjectSlice.grade, total=subjectSlice.total, no=subjectSlice.no)
    fill.infoToReplace(template_name=template_name, name=student.name, picture=student.picture_name,
                       program_name=student.program_name, academic_year=student.academic_year,
                       ID=student.ID, UEL_ID=student.UEL_ID, ASU_course_code=subject.ASU_course_code,
                       UEL_module_code=subject.UEL_module_code, ASU_course_name=subject.ASU_course_name,
                       UEL_module_name=subject.UEL_module_name, semester=subject.semester, grade=subjectSlice.grade,
                       instructor_signature=subject.instructor_signature,
                       assistant_signature=subject.assistant_signature, no=subjectSlice.no)


createSubjectSliceFiller(student=student1, subject=subject1, subjectSlice=ass1)

