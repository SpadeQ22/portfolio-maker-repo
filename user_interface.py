import os
import sys
import threading
import tkinter as tk
import tkinter.messagebox
from os import listdir
from os.path import isfile, join
from tkinter import ttk

import requests.exceptions

import Autofill

import InfoContainers
import UI.Screen2
import converter
import merge
from Autofill.filler import createSubjectFiller
from UI.Screen1 import Screen1
from UI.Screen2 import Screen2
from UI.Screen3 import Screen3
from UI.Screen4 import Screen4
# from UI.test import Screen4
from Downloader.Downloader import Downloader


class Application(tk.Tk):

    def __init__(self, *args):
        super().__init__()
        self.subjects = []
        self.student = None
        self.current_subject = None
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        self.currentScreen = None
        self.change_to_screen(Screen1)
        self.overrideredirect(False)
        # super().bind("<Button-1>", self.clickwin)
        # super().bind("<B1-Motion>", self.dragwin)
        self.resizable(False, False)
        self.mainloop()

    def change_to_screen(self, Screen):
        screen = Screen(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def change_to_screen2(self):
        screen = Screen2(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def change_to_screen3(self):
        screen = Screen3(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
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
            root.after(2500, step)

        def start_download():
            try:
                downloader = Downloader(self.student.email, self.student.password)
                subject_codes = [subject.ASU_course_code for subject in self.subjects]
                downloader.get_files(subject_codes)
                downloader.get_quizzes(subject_codes)
                self.current_subject = self.subjects[0]
                for subject in self.subjects:
                    createSubjectFiller(self.student, subject)
                self.classify()
                self.change_to_screen(Screen4)
            except requests.exceptions.ConnectionError:
                root.destroy()
                ans = tk.messagebox.askretrycancel("Error 400", "Connection Error: Couldn't Connect to Server, Try Again!")
                if ans:
                    self.download_splash()
                else:
                    sys.exit(0)

        root = tk.Tk()
        threading.Thread(target=start_download).start()
        root.geometry("400x100")
        root.configure(bg="#83568a")
        root.resizable(False, False)
        root.title("Portfolio Maker")
        my_label = tk.Label(root, text="accessing site and getting cookies...", anchor="w",
                            font=("RobotoCondensed-normal", 10, "normal"), bg="#83568a")
        my_label.pack(fill=tk.BOTH, padx=50, pady=10)
        my_progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        my_progress.pack(pady=1)
        root.eval('tk::PlaceWindow . center')
        step()
        root.mainloop()

    def classify(self):
        for subject in self.subjects:
            if os.path.exists(f"Subjects/{subject.ASU_course_code}"):
                if os.path.exists(f"Subjects/{subject.ASU_course_code}/ass"):
                    mypath = f"Subjects/{subject.ASU_course_code}/ass"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    onlyfiles.append(f"Subjects/{subject.ASU_course_code}/My Header.docx")
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.assignments.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/lab"):
                    mypath = f"Subjects/{subject.ASU_course_code}/lab"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    print(onlyfiles)
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.labs.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/project"):
                    mypath = f"Subjects/{subject.ASU_course_code}/project"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.project.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/quizzes"):
                    mypath = f"Subjects/{subject.ASU_course_code}/quizzes"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.quizzes.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/midterm"):
                    mypath = f"Subjects/{subject.ASU_course_code}/midterm"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.midterms.file_paths = onlyfiles

    def merger_interface(self):
        pdfs_to_merge = []
        for subject in self.subjects:
            pdfs_to_merge.append(f"Subjects/{subject.ASU_course_code}/My Header.pdf")
            pdfs_to_merge.append(subject.assignments.file_paths)
            pdfs_to_merge.append(subject.quizzes.file_paths)
            pdfs_to_merge.append(subject.midterm.file_paths)
            pdfs_to_merge.append(subject.labs.file_paths)
            pdfs_to_merge.append(subject.project.file_paths)
            merge.merge_pdfs(pdfs_to_merge, f"Subjects/{subject.ASU_course_code}")
            pdfs_to_merge = []
        tkinter.messagebox.showinfo("Success", "Portfolios Generated Successfully")
