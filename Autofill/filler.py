import datetime

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm


class Filler:

    def __init__(self, **kwargs):
        """
        1) passes the parameters to processMarker1() and processMarker2() to return a string to be replaced based on the
        grade
        2) this process is done by using grade borders lists as shown, and grade border handlers
        (replaceable strings in templates)

        this is done to ease the process of .render() as this method can only be
        used once, so all info must be processed first after passing it

        :param kwargs: takes grade, total marks, and number of slice (eg. lab 2, lab 1)
        """
        self.gradeBorders = [95, 82, 70, 66, 63, 60, 56, 53, 50, 45, 40, 0]
        self.gradeBorders2 = [100, 96, 93, 90, 89, 84, 79, 75, 74, 69, 64, 60, 59, 40, 20, 0]
        self.gradeBordersHandler = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                                    "eleven", "twelve"]
        self.gradeBordersHandler2 = ["m", "m1", "m2", "m3", "a", "a1", "a2", "a3", "ad", "ad1", "ad2", "ad3", "i", "i1",
                                     "i2", "i3"]
        self.marker1 = self.processMarker1(kwargs["grade"], kwargs["total"])
        self.marker2 = self.processMarker2(kwargs["grade"], kwargs["total"])

    def processMarker1(self, grade, total):
        """
        this function passes the first marker (in the template) which specifies the student performance
        to the function called infoToReplace

        :param grade: takes grade of a subject object eg. lab, quiz...
        :param total: takes total mark of the same subject object
        :return: returns the string to be replaced in the template
        """
        for i in range(len(self.gradeBorders)):
            if grade / total >= (self.gradeBorders[i] / 100):
                return self.gradeBordersHandler[i]
            else:
                continue

    def processMarker2(self, grade, total):
        """
        this function passes the second marker (in the template) which specifies the student performance
        to the function called infoToReplace

        :param grade: takes grade of a subject object eg. lab, quiz...
        :param total: takes total mark of the same subject object
        :return: returns the string to be replaced in the template
        """

        for i in range(len(self.gradeBorders2)):
            if grade / total >= (self.gradeBorders2[i] / 100):
                return self.gradeBordersHandler2[i]
            else:
                continue

    def infoToReplace(self, **kwargs):

        """
        takes all info to be replaced in a given template

        :param kwargs: takes all info including student, sunject and subject info to be replaced in the template and
        attempts this action using render() method
        :return: new generated documents of the student in a file --> Autofill/AutofillResults
        """

        doc = DocxTemplate(kwargs["template_name"])

        picture = InlineImage(doc, "Autofill/Templates and pictures/" + kwargs["picture"], Cm(5))
        context = {"name": kwargs["name"],
                   "picture": kwargs["picture"],
                   "program_name": kwargs["program_name"],
                   "ID": kwargs["ID"],
                   "UEL_ID": kwargs["UEL_ID"],
                   "semester": kwargs["semester"],
                   "academic_year": str(kwargs["academic_year"]),
                   "ASU_course_code": str(kwargs["ASU_course_code"]),
                   "UEL_module_code": str(kwargs["UEL_module_code"]),
                   "ASU_course_name": kwargs["ASU_course_name"],
                   "UEL_module_name": kwargs["UEL_module_name"],
                   "date": datetime.datetime.now().strftime('%m/%d/%Y'),
                   "no": kwargs["no"],
                   "grade": kwargs["grade"],
                   "instructor_signature": kwargs["instructor_signature"],
                   "assistant_signature": kwargs["assistant_signature"],
                   self.marker1: "*",
                   self.marker2: "*"}

        doc.render(context)
        doc.save("Autofill/AutofillResults/My " +
                 (kwargs["template_name"].replace("Template.docx", "")).replace("Autofill/Templates and pictures/", "")
                 + str(kwargs["no"]) + ".docx")


def createSubjectSliceFiller(student, subject, subjectSlice):
    """
    Creates a filler object to process grade markers and to replace all info passed in a given template

    :param student: takes student object to pass its parameter to infoToReplace method
    :param subject: takes subject object to pass its parameter to infoToReplace method
    :param subjectSlice: takes a slice (eg. lab, midterm...) of a subject
    :return: the results of infoToReplace
    """
    # takes quiz, assignment...objects and creates a filler for their templates
    templates = ['Autofill/Templates and pictures/Header Template.docx',
                 'Autofill/Templates and pictures/Assignment Template.docx',
                 'Autofill/Templates and pictures/Quiz Template.docx',
                 'Autofill/Templates and pictures/Lab Template.docx',
                 'Autofill/Templates and pictures/Project Template.docx']

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
