import datetime

import docx


class Filler:

    def __init__(self):
        self.gradeBorders = [95, 82, 70, 66, 63, 60, 56, 53, 50, 45, 40]

    def infoToReplace(self, template_name, name, program_name, academic_year, ID, UEL_ID, ASU_course_code,
                      UEL_module_code,
                      ASU_course_name, UEL_module_name, semester):

        doc = docx.Document(template_name)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        paragraph.text = paragraph.text.replace("<name>", name)
                        paragraph.text = paragraph.text.replace("<program_name>", program_name)
                        paragraph.text = paragraph.text.replace("<academic_year>", str(academic_year))
                        paragraph.text = paragraph.text.replace("<ID>", str(ID))
                        paragraph.text = paragraph.text.replace("<UEL_ID>", str(UEL_ID))
                        paragraph.text = paragraph.text.replace("<ASU_course_code>", str(ASU_course_code))
                        paragraph.text = paragraph.text.replace("<UEL_module_code>", str(UEL_module_code))
                        paragraph.text = paragraph.text.replace("<ASU_course_name>", ASU_course_name)
                        paragraph.text = paragraph.text.replace("<UEL_module_name>", UEL_module_name)
                        paragraph.text = paragraph.text.replace("<semester>", str(semester))
                        if template_name == 'Header Template.docx':
                            paragraph.text = paragraph.text.replace("<date_here>",
                                                                    datetime.datetime.now().strftime('%m/%d/%Y'))
                        else:
                            # paragraph.text = paragraph.text.replace("<date_here>", ***get date from lms***
                            return 0

        doc.save(template_name)

    def gradesToReplace(self, template_name, grade, total, instructor_signature, assistant_signature):
        doc = docx.Document(template_name)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        paragraph.text = paragraph.text.replace("<grade>", grade)
                        paragraph.text = paragraph.text.replace("<instructor_signature>", instructor_signature)
                        paragraph.text = paragraph.text.replace("<assistant_signature>", assistant_signature)
                        for i in self.gradeBorders:
                            if grade / total >= self.gradeBorders[i] / 100:
                                paragraph.text = paragraph.text.replace("<_" + self.gradeBorders[i] + ">", "*")
                            else:
                                paragraph.text = paragraph.text.replace("<_0>", "*")

        doc.save(template_name)

