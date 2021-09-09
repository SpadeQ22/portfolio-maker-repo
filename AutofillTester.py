from InfoContainers import Subject, Midterm, Project, Quiz, Lab, Assignment, Student
from Autofill.filler import createSubjectSliceFiller

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


createSubjectSliceFiller(student=student1, subject=subject1, subjectSlice=ass1)
