from Tkinter import *
class Application(Frame):

    def say_hi(self):
        print "hi there, everyone!"
        print variable.get()
        print entry.get()
    def generate_entry_box(self, title, description, example, row):
        print "generating entry box"
        Label(self, text=title).grid(row=row, column=0)
        aexternal_id = Entry(self)
        aexternal_id.grid(row=row, column=1)
        Message(self, text=description).grid(row=row, column=2)
        Message(self, text=example).grid(row=row, column=3)
    def generate_dropdown_box(self):
        print "generating dropdown box"
    def generate_label(self, text, row, column):
        Label(self, text=text).grid(row=row, column=column)

    def createWidgets(self):
        global external_id #need to worry about this because you could possibly overwrite old exercises
        global is_public
        global experience
        global language_list
        global style_list
        global tag_list
        global version
        global creator
        global prompts
        global position
        global question
        global allow_multiple
        global choices
        global answer
        global position
        global value
        #coding stuff
        global class_name
        global method_name
        global start_code
        global wrapper_code
        global tests



        #create the canvas
        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")
        # create all the main containers
        headers_frame = Frame(self, bg='cyan', width=450, height=50, pady=3)
        body_frame = Frame(self.canvas, bg='white', width=450, height=50, pady=3)
        #create the scroll bar and set it
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=5)
        self.canvas.grid(row=1, stick="nsew")
        self.canvas.create_window((4, 4), window=body_frame, anchor="nw",
                                  tags="body_frame")

        body_frame.bind("<Configure>", self.onFrameConfigure)

        # containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        headers_frame.grid(row=0, sticky="ew")
        #body_frame.grid(row=1, sticky="nsew")

        #headers
        Label(headers_frame, text="input name").grid(row=0, column=0, padx=25)
        Label(headers_frame, text="input").grid(row=0, column=1, padx=35)
        Label(headers_frame, text="description").grid(row=0, column=2, padx=130)
        Label(headers_frame, text="examples").grid(row=0, column=3, padx=30)

        #external_id
        Label(body_frame, text="external ID").grid(row=1, column=0)
        external_id = Entry(body_frame)
        external_id.grid(row=1, column=1)
        Message(body_frame, text="this is a description more words go here, does it auto wrap around who knows i guess we "
                           "will find out very shortly").grid(row=1, column=2)
        Message(body_frame, text="this is an example").grid(row=1, column=3)

        #is_public
        Label(body_frame, text="is public").grid(row=2)
        is_public = StringVar(body_frame)
        is_public = OptionMenu(body_frame, is_public, "true", "false")
        is_public.grid(row=2, column=1)
        Message(body_frame, text="this is a description more words go here, does it auto wrap around who knows i guess we "
                           "will find out very shortly").grid(row=2, column=2)
        Message(body_frame, text="this is an example").grid(row=2, column=3)
        #experience
        Label(body_frame, text="experience").grid(row=3, column=0)
        experience = Entry(body_frame)
        experience.grid(row=3, column=1)
        Message(body_frame, text="Each student on CodeWorkout can gain experience points for doing exercises and workouts "
                           "through CodeWorkout generally to show how often they have practiced and give them a way to "
                           "track progress. This field takes an integer for the amount of experience points the student "
                           "will gain from completing this exercise.").grid(row=3, column=2)
        Message(body_frame, text="50").grid(row=3, column=3)

        #language list
        Label(body_frame, text="language list").grid(row=4)
        language_list_starting_value = StringVar(body_frame)
        language_list_starting_value.set("java")
        language_list = OptionMenu(body_frame, language_list_starting_value, "java")
        language_list.grid(row=4, column=1)
        Message(body_frame, text="This field is for a list of programming languages associated with the exercise, although "
                           "this would generally be just one. This is used for sorting and grouping exercises.")\
            .grid(row=4, column=2)
        Message(body_frame, text="java").grid(row=4, column=3)

        #style list
        Label(body_frame, text="style list").grid(row=5)
        style_list = Listbox(body_frame, selectmode=MULTIPLE)
        for item in ["factorial", "function", "multiplication", "java", "code writing", "random", "forced choice",
                     "conditional", "multiple choice", "single answer"]:
            style_list.insert(END, item)
        style_list.grid(row=5, column=1)
        Message(body_frame, text="This is the type of question used in the exercise. For example, this field could be "
                           "multiple choice, single answer, code writing, etc. This is also used for grouping "
                           "exercises.") \
            .grid(row=5, column=2)
        Message(body_frame, text="factorial, function, multiplication").grid(row=5, column=3)

        #tag list
        Label(body_frame, text="tag list").grid(row=6)
        tag_list = Listbox(body_frame, selectmode=MULTIPLE)
        for item in ["methods", "classes", "for-loops", "recursion", "arithmetic"]:
            tag_list.insert(END, item)
        tag_list.grid(row=6, column=1)
        Message(body_frame, text="This is a list of other tags that should indicate the subject matter of the exercise. "
                           "This could include things such as methods, classes, for-loops, recursion, arithmetic, etc. "
                           "This is used for grouping exercises by tags.") \
            .grid(row=6, column=2)
        Message(body_frame, text="classes, recursion").grid(row=6, column=3)

        #version
        Label(body_frame, text="version").grid(row=7, column=0)
        version = Entry(body_frame)
        version.grid(row=7, column=1)
        Message(body_frame, text="This is a simple integer stating the current version of the exercise. This works with the "
                           "external_id (seen above) to indicate if this is a new exercise or a new version of one. "
                           "Each version of an exercise is stored in the database so that an older version can be"
                           " accessed at any point. This is important in a situation that a student would want to "
                           "review feedback from an exercise they had previously received, but the exercise had since "
                           "been altered in the database. The student would be able to access the information to the "
                           "version of the exercise they completed.").grid(row=7, column=2)
        Message(body_frame, text="1.0").grid(row=7, column=3)
        #creator

        #prompts
        #position
        #question
        #allow multiple (only multiple choice)
        #choices (only multiple choice)
        #answer (only multiple choice)
        #position (only multiple choice)
        #value (only multiple choice)
        #class name (only coding questions)
        #method name (only coding questions)
        #starter code (only coding questions)
        #wrapper code (only coding questions)
        #tests (only coding questions)

        #drop down menu options
        #global variable
        #variable = StringVar(self)
        #variable.set("one")  # default value
        #Label(self, text="external ID").grid(row=3)
        ##w = OptionMenu(self, variable, "one", "two", "three")
        #w.grid(row=3, column=1)
        #Message(self, text="this is a description more words go here, does it auto wrap around who knows i guess we "
        #                   "will find out very shortly").grid(row=3, column=2)
        #Message(self, text="this is an example").grid(row=3, column=3)
        #end drop down menu options
        #start fill in your own option
        #global entry
        #Label(self, text="external ID").grid(row=4)
        #entry = Entry(self)
        #entry.grid(row=4, column=1)
        #Message(self, text="this is a description more words go here, does it auto wrap around who knows i guess we "
        #                   "will find out very shortly").grid(row=4, column=2)
        #Message(self, text="this is an example").grid(row=4, column=3)
        #end fill in your own option

        Label(self, text="external ID")
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] = self.quit


        #self.QUIT.pack()

        #self.hi_there = Button(self)
        #self.hi_there["text"] = "Hello",
        #self.hi_there["command"] = self.say_hi
        #self.hi_there.grid(row=4, column=1)

   #     self.hi_there.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()