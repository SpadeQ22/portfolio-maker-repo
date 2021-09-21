from InfoContainers import Subject, Midterm, Project, Quiz, Lab, Assignment, Student, Header
from Autofill.filler import createSubjectFiller


midterm = Midterm(grade=20, total=25)
project = Project(grade=9, total=10)
lab1 = Lab(grade=8, total=10)
lab2 = Lab(grade=9, total=10)
ass1 = Assignment(grade=5, total=10)
ass2 = Assignment(grade=8, total=10)
quiz1 = Quiz(grade=10, total=10)
quiz2 = Quiz(grade=7, total=10)

student1 = Student(name="Hussein", picture_name='mario.png', UEL_ID=2021, ID=123,
                   program_name="CESS", academic_year=2021)
subject1 = Subject(ASU_course_code="cse111", UEL_module_code="uel111",
                   ASU_course_name="programming", UEL_module_name="programminguel", semester="fall",
                   instructor_signature="Ahmed", assistant_signature="maria", midterm=midterm, assignments=[ass1, ass2],
                   labs=[lab1, lab2], project=project, quizzes=[quiz1, quiz2])

createSubjectFiller(student=student1, subject=subject1)