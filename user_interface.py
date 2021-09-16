import os
from tkinter import *
from tkinter import ttk

import InfoContainers
from UI.Screen1 import Screen1
from UI.Screen2 import Screen2
from UI.Screen3 import Screen3
from UI.Screen4 import Screen4
from Downloader.Downloader import Downloader

class Application(Tk):

    def __init__(self, *args):
        super().__init__ ()
        self.subjects: InfoContainers.Subject
        self.student = None
        self.current_subject: InfoContainers.Subject
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        self.currentScreen = None
        self.change_to_screen(Screen3)
        self.overrideredirect(False)
        # super().bind("<Button-1>", self.clickwin)
        # super().bind("<B1-Motion>", self.dragwin)
        self.resizable(False, False)
        self.mainloop()

    # def dragwin(self, event):
    #     x = super().winfo_pointerx() - self._offsetx
    #     y = super().winfo_pointery() - self._offsety
    #     super().geometry(f"+{x}+{y}")
    #
    # def clickwin(self, event):
    #     self._offsetx = super ().winfo_pointerx () - super ().winfo_rootx ()
    #     self._offsety = super ().winfo_pointery () - super ().winfo_rooty ()

    def change_to_screen(self, Screen):
        screen = Screen(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config (
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config (
            image=colorOnLeave))

    def check_filled(self, *args) -> bool:
        cnt = 0
        for arg in list(args):
            print(arg)
            if len(arg) > 0:
                cnt += 1
        if cnt == len(args):
            return True
        else:
            return False

    def download_splash(self):
        def step():
            my_progress['value'] += 2
            if my_progress['value'] == 100:
                root.destroy()
                return
            if my_progress['value'] == 20:
                my_label['text'] = 'Downloading files...'
            if my_progress['value'] == 80:
                my_label['text'] = 'Organizing files and setting file paths...'
            root.after(1000, step)
        root = Tk()
        root.geometry("400x100")
        root.configure(bg="#83568a")
        root.resizable(False, False)
        root.title("Portfolio Maker")
        my_label = Label(root, text="accessing site and getting cookies...", anchor="w",
                         font=("RobotoCondensed-normal", 10, "normal"), bg="#83568a")
        my_label.pack(fill=BOTH, padx=50, pady=10)
        my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
        my_progress.pack(pady=1)
        root.eval('tk::PlaceWindow . center')
        step()
        root.mainloop()

    def start_download(self):
        downloader = Downloader(self.student.email, self.student.password)
        subject_codes = [subject.ASU_course_code for subject in self.subjects]
        downloader.get_files(subject_codes)
        downloader.get_quizzes(subject_codes)
        self.classify()

    def classify(self):
        for subject in self.subjects:
            if os.path(f"Subjects/{subject.ASU_course_code}").exists():
                if os.path(f"Subjects/{subject.ASU_course_code}/ass").exists():
                        for entry in os.scandir(f"Subjects/{subject.ASU_course_code}/ass"):
                            subject.assignments.file_paths.append(entry)
                if os.path(f"Subjects/{subject.ASU_course_code}/labs").exists():
                    for entry in os.scandir(f"Subjects/{subject.ASU_course_code}/labs"):
                        subject.labs.file_paths.append(entry)
                if os.path(f"Subjects/{subject.ASU_course_code}/project").exists():
                    for entry in os.scandir(f"Subjects/{subject.ASU_course_code}/project"):
                        subject.project.file_paths.append(entry)
                if os.path(f"Subjects/{subject.ASU_course_code}/quizzes").exists():
                    quiz_list = os.scandir(f"Subjects/{subject.ASU_course_code}/quizzes")
                    subject.quizzes[0].file_path = quiz_list[0]
                    subject.quizzes[1].file_path = quiz_list[1]
                    subject.quizzes[2].file_path = quiz_list[2]


app = Application()
