from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

from job_search import JobSearch
from indeed_scraper import Indeed_Scraper

class MainWindow:
    def __init__(self):
        self.working_dir = os.path.abspath(os.curdir)
        self.job_search = JobSearch()
        self.scraper = Indeed_Scraper()
        self.window_width = 800
        self.window_height = 600

        # Generate Window Boilerplate
        self.root = Tk()
        self.root.title("Job Jackal - Indeed Aggregator")
        self.root.geometry(self.Determine_Window_Dimensions())
        self.root.minsize(self.window_width, self.window_height)
        self.root.iconbitmap('.\\assets\\short_jackal.ico')

        # Generate Default Window Contents
        self.cb_exclude_nopay = ttk.Checkbutton(self.root,
                                   text="Exclude listings with no listed wage",
                                   command=self.job_search.Tick_ExcludeNoPayRate)

        self.cb_exclude_nopay = ttk.Checkbutton(self.root,
                                                text="Exclude listings with no listed wage",
                                                command=self.job_search.Tick_ExcludeNoPayRate)


        self.frame_header = LabelFrame(self.root)
        self.frame_header.pack(padx=10, pady=10)

        self.frame_basic_search = LabelFrame(self.root, padx=10, pady=10, text="Basic Job Search")
        self.frame_basic_search.pack(padx=10, pady=10)

        self.frame_salary_options = LabelFrame(self.root, padx=10, pady=10, text="Salary Options")
        self.frame_salary_options.pack(padx=10, pady=10)

        self.frame_adv_search = LabelFrame(self.root)
        self.frame_adv_search.pack(padx=10, pady=10)


        self.image_banner = ImageTk.PhotoImage(Image.open('./Assets/Job_Jackal_Banner.png'))
        self.label_banner = Label(self.frame_header, image=self.image_banner)
        self.label_banner.pack()

        self.label_job_title = ttk.Label(self.frame_basic_search, text="Job Title: ")
        self.label_job_title.grid(row=1, column=0)
        self.field_job_title = ttk.Entry(self.frame_basic_search, width=10)
        self.field_job_title.grid(row=1, column=1)


        self.label_location = ttk.Label(self.frame_basic_search, text="\tLocation: ")
        self.label_location.grid(row=1, column=2)
        self.field_location = ttk.Entry(self.frame_basic_search, width=10)
        self.field_location.grid(row=1, column=3)

        self.label_radius = ttk.Label(self.frame_basic_search, text="\tRadius: ")
        self.label_radius.grid(row=1, column=4)
        self.field_radius = ttk.Entry(self.frame_basic_search, width=3)
        self.field_radius.grid(row=1, column=5)

        self.label_min_salary = ttk.Label(self.frame_salary_options, text="Minimum Salary: ")
        self.label_min_salary.grid(row=2, column=0)
        self.field_min_salary = ttk.Entry(self.frame_salary_options, width=5)
        self.field_min_salary.grid(row=2, column=1)

        self.label_min_hourly = ttk.Label(self.frame_salary_options, text="Minimum Salary: ")
        self.label_min_hourly.grid(row=2, column=2)
        self.field_min_hourly = ttk.Entry(self.frame_salary_options, width=5)
        self.field_min_hourly.grid(row=2, column=3)



        # self.label_job_title.grid(row=1, column=0,)
        # self.field_job_title.grid(row=1, column=1)
        # self.label_location.grid(row=1, column=0)
        # self.field_location.grid(row=1, column=1)
        # self.label_radius.grid(row=2, column=0)
        # self.field_radius.grid(row=2, column=1)
        # self.cb_exclude_nopay.grid(row=1, column=0)

    def Determine_Window_Dimensions(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)
        return f'{self.window_width}x{self.window_height}+{center_x}+{center_y}'

    def Disable_Resizable_Window(self, hint="wh"):
        width = False
        height = False
        if len(hint) <= 2:
            if "h" not in hint:
                height = True
            if "w" not in hint:
                width = True

            self.root.resizable(width, height)

    def Set_Window_Opacity(self, opacity):
        self.root.attributes('-alpha',opacity)

    def Main_Loop(self):
        self.root.mainloop()

if __name__ == "__main__":
    my_gui = MainWindow()
    my_gui.Main_Loop()