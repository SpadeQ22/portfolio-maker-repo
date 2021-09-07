from filler import toReplace


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


