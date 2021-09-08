import datetime

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm


class Filler:

    def __init__(self, *args):

        self.gradeBorders = [95, 82, 70, 66, 63, 60, 56, 53, 50, 45, 40, 0]
        self.gradeBorders2 = [100, 96, 93,	90,	89,	84,	79,	75,	74,	69,	64,	60,	59,	40,	20, 0]
        self.gradeBordersHandler = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                                    "eleven", "twelve"]
        self.gradeBordersHandler2 = ["m", "m1", "m2", "m3", "a", "a1", "a2", "a3", "ad", "ad1", "ad2", "ad3", "i", "i1",
                                     "i2", "i3"]
        self.marker1 = self.processMarker1(args[0], args[1])
        self.marker2 = self.processMarker2(args[0], args[1])

    def processMarker1(self, grade, total):

        for i in range(len(self.gradeBorders)):
            if grade / total >= (self.gradeBorders[i] / 100):
                return self.gradeBordersHandler[i]
            else:
                continue

    def processMarker2(self, grade, total):

        for i in range(len(self.gradeBorders2)):
            if grade / total >= (self.gradeBorders2[i] / 100):
                return self.gradeBordersHandler2[i]
            else:
                continue

    def infoToReplace(self, template_name, name, image_name, program_name, academic_year, ID, UEL_ID, ASU_course_code,
                      UEL_module_code,
                      ASU_course_name, UEL_module_name, semester, grade, instructor_signature,
                      assistant_signature):

        doc = DocxTemplate(template_name)

        picture = InlineImage(doc, image_name, Cm(5))
        context = {"name": name,
                   "picture": picture,
                   "program_name": program_name,
                   "ID": ID,
                   "UEL_ID": UEL_ID,
                   "semester": semester,
                   "academic_year": str(academic_year),
                   "ASU_course_code": str(ASU_course_code),
                   "UEL_module_code": str(UEL_module_code),
                   "ASU_course_name": ASU_course_name,
                   "UEL_module_name": UEL_module_name,
                   "date": datetime.datetime.now().strftime('%m/%d/%Y'),
                   "grade": grade,
                   "instructor_signature": instructor_signature,
                   "assistant_signature": assistant_signature,
                   self.marker1: "*",
                   self.marker2: "*"}

        doc.render(context)
        doc.save("new " + template_name)
