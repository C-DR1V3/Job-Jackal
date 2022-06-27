from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

from job_search import JobSearch
from indeed_scraper import Indeed_Scraper

class MainWindow:
    def __init__(self):
        self.working_dir = os.path.abspath(os.curdir)
        self.job_search = JobSearch()
        self.scraper = Indeed_Scraper()
        self.window_width = 660
        self.window_height = 600
        self.destination_folder = "Select Directory For Output File"

        # Generate Window Boilerplate
        self.root = Tk()
        self.root.configure(bg='#222424')
        self.root.title("Job Jackal - Indeed Aggregator")
        self.root.geometry(self.Determine_Window_Dimensions())
        self.root.minsize(self.window_width, self.window_height)
        self.root.iconbitmap('.\\assets\\short_jackal.ico')

        # Generate Default Window Content

        self.frame_header = LabelFrame(self.root, borderwidth=0, bg='#222424', fg='#222424')
        self.frame_header.pack(anchor=NW, padx=10, pady=10)

        self.frame_left_group = LabelFrame(self.root, borderwidth=0, bg='#222424')
        self.frame_left_group.pack(anchor=NW, padx=5, pady=5)

        self.frame_basic_search = LabelFrame(self.frame_left_group, padx=10, pady=10, borderwidth=0, bg='#222424')
        self.frame_basic_search.pack(anchor=NW, padx=10, pady=2)

        self.frame_salary_options = LabelFrame(self.frame_left_group, padx=10, pady=10, borderwidth=0, bg='#222424')
        self.frame_salary_options.pack(anchor=NW, padx=10, pady=2)

        self.frame_adv_search = LabelFrame(self.frame_left_group, borderwidth=0, bg='#222424')
        self.frame_adv_search.pack(anchor=NW, padx=10, pady=(40, 2))


        self.image_banner = ImageTk.PhotoImage(Image.open('./Assets/Job_Jackal_Banner.png'))
        self.label_banner = Label(self.frame_header, image=self.image_banner, bg='#222424')
        self.label_banner.pack()

        self.label_job_title = Label(self.frame_basic_search, text="Job Title: ", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_job_title.pack(side=LEFT)
        self.field_job_title = Entry(self.frame_basic_search, width=20, background="#404242", foreground="#eeeeee")
        self.field_job_title.pack(padx=(0,25), side=LEFT)
        

        self.label_location = Label(self.frame_basic_search, text="Location: ", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_location.pack(side=LEFT)
        self.field_location = Entry(self.frame_basic_search, width=20, background="#404242", foreground="#eeeeee")
        self.field_location.pack(padx=(0,25), side=LEFT)

        self.label_radius = Label(self.frame_basic_search, text="Radius: ", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_radius.pack(side=LEFT)
        self.field_radius = Entry(self.frame_basic_search, width=4, background="#404242", foreground="#eeeeee")
        self.field_radius.pack(padx=(0,25), side=LEFT)

        self.label_min_salary = Label(self.frame_salary_options, text="Minimum Salary: ", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_min_salary.pack(side=LEFT)
        self.field_min_salary = Entry(self.frame_salary_options, width=5, background="#404242", foreground="#eeeeee")
        self.field_min_salary.pack(padx=(0,50), side=LEFT)

        self.label_min_hourly = Label(self.frame_salary_options, text="Minimum Salary: ", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_min_hourly.pack(side=LEFT)
        self.field_min_hourly = Entry(self.frame_salary_options, width=5, background="#404242", foreground="#eeeeee")
        self.field_min_hourly.pack(padx=(0,50), side=LEFT)

        self.cb_exclude_nopay = Checkbutton(self.frame_salary_options,
                                                text="Exclude listings with no listed wage",
                                                background="#404242", foreground="#eeeeee", selectcolor='#2c2e2e',
                                                command=self.job_search.Tick_ExcludeNoPayRate)
        self.cb_exclude_nopay.pack(side=LEFT)

        self.label_exclude = Label(self.frame_adv_search, text="Exclude words from job description", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_exclude.grid(row=0, column=0, pady=(0,5))
        self.field_exclude = Text(self.frame_adv_search, width=37, height=15, background="#404242", foreground="#eeeeee")
        self.field_exclude.grid(row=1, column=0, padx=(0,15))

        self.label_include = Label(self.frame_adv_search, text="Include words from job description", background="#2c2e2e", foreground="#eeeeee", relief=RIDGE)
        self.label_include.grid(row=0, column=2, pady=(0,5))
        self.field_include = Text(self.frame_adv_search, width=37, height=15, background="#404242", foreground="#eeeeee")
        self.field_include.grid(row=1, column=2, padx=(15,0))


        self.button_folder_dialog = Button(self.frame_left_group, text=self.destination_folder, width=42, background="#2c2e2e", foreground="#eeeeee", relief=RAISED,
                                           command=self.Get_Install_Directory)
        self.button_folder_dialog.pack(side=LEFT, anchor=S, padx=(10,14))

        self.button_initiate = Button(self.frame_left_group, text="Search", width=15, background="#2c2e2e", foreground="#eeeeee", relief=RAISED)
        self.button_initiate.pack(side=LEFT, anchor=S, pady=(10, 0), padx=(14,0))



    def Get_Install_Directory(self):
        self.destination_folder = filedialog.askdirectory(
            parent=self.frame_adv_search,
            title="Choose directory to output results",
        )
        self.button_folder_dialog['text'] = self.destination_folder


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