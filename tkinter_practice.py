from Tkinter import *


class Example(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def add_answer_choice_method(self):
    # answer (only multiple choice)
        self.count += 1
        Label(self.frame, text="answer").grid(row=self.count)
        self.add_answer_choice = Entry(self.frame)
        self.add_answer_choice.grid(row=self.count, column=1)
        Message(self.frame,
                text="Text of the multiple choice option.").grid(row=self.count, column=2)
        Message(self.frame, text="if (condition) {//do something} else { //do something else }")\
            .grid(row=self.count, column=3)
    # position (only multiple choice)
        self.count += 1
        Label(self.frame, text="position").grid(row=self.count)
        self.add_answer_choice = Entry(self.frame)
        self.add_answer_choice.grid(row=self.count, column=1)
        Message(self.frame, text="It decides the order of the answer choices.").grid(row=self.count, column=2)
        Message(self.frame, text="1").grid(row=self.count, column=3)
    # value (only multiple choice)
        self.count += 1
        Label(self.frame, text="value").grid(row=self.count)
        self.add_answer_choice = Entry(self.frame)
        self.add_answer_choice.grid(row=self.count, column=1)
        Message(self.frame, text="This determines the integer value of the answer. Let's say there is only one "
                                 "correct answer, every wrong answer could be set to 0 and the correct one to 1. "
                                 "Some answers could be more correct than others and some could offer partial credit. "
                                 "Some could even take multiple answers and the numbers could all be equal except for "
                                 "the wrong answer in order to determine the score.").grid(row=self.count, column=2)
        Message(self.frame, text="1").grid(row=self.count, column=3)

    def remove_answer_choice_method(self):
        print "remove answer choice"
        print self.count, "before"
        temp_count = self.count - 3
        print "temp count", temp_count
        print "grid slaves",self.frame.grid_slaves()
        for label in self.frame.grid_slaves():
            print "label grid info", int(label.grid_info()["row"])
            if int(label.grid_info()["row"]) > temp_count and int(label.grid_info()["row"]) > 12:
                label.grid_forget()
                print self.count, "after"
                print "forget another one"
        if temp_count > 12:
            self.count -= 3

    def render_multiple_choice(self):
        print "multiple choice"
        #starting at row 11
        # allow multiple (only multiple choice)
        Label(self.frame, text="allow multiple").grid(row=11)
        self.allow_multiple = StringVar(self.frame)
        self.allow_multiple = OptionMenu(self.frame, self.allow_multiple, "true", "false")
        self.allow_multiple.grid(row=11, column=1)
        Message(self.frame,
                text="If set to false, the student will only be allowed to choose one answer choice. If true, "
                     "they can select one or many answers.").grid(row=11, column=2)
        Message(self.frame, text="true").grid(row=11, column=3)
        # choices (only multiple choice)
        #button to add a answer section
        self.count = 12
        self.add_answer_choices = Button(self.frame)
        self.add_answer_choices["text"] = "add a answer choice",
        self.add_answer_choices["command"] = self.add_answer_choice_method
        self.add_answer_choices.grid(row=12, column=0)
        #button to remove a answer section
        self.remove_answer_choices = Button(self.frame)
        self.remove_answer_choices["text"] = "remove the most recent answer choice",
        self.remove_answer_choices["command"] = self.remove_answer_choice_method
        self.remove_answer_choices.grid(row=12, column=1)
        # answer (only multiple choice)
        # position (only multiple choice)
        # value (only multiple choice)

    def render_coding(self):
        print "coding"
        # class name (only coding questions)
        Label(self.frame, text="class name").grid(row=11, column=0)
        self.class_name = Entry(self.frame)
        self.class_name.grid(row=11, column=1)
        Message(self.frame,
                text="These should include the names of the class and method being worked with in the code given, "
                     "assuming that both are needed.").grid(row=11, column=2)
        Message(self.frame, text="month").grid(row=11, column=3)
        # method name (only coding questions)
        # starter code (only coding questions)
        # wrapper code (only coding questions)
        # tests (only coding questions)

    def populate(self):
        # headers
        Label(self.frame, text="input name").grid(row=0, column=0, padx=25)
        Label(self.frame, text="input").grid(row=0, column=1, padx=35)
        Label(self.frame, text="description").grid(row=0, column=2, padx=130)
        Label(self.frame, text="examples").grid(row=0, column=3, padx=30)
        #external_id
        Label(self.frame, text="external ID").grid(row=1, column=0)
        self.external_id = Entry(self.frame)
        self.external_id.grid(row=1, column=1)
        Message(self.frame, text="this is a description more words go here, does it auto wrap around who knows i guess we "
                           "will find out very shortly").grid(row=1, column=2)
        Message(self.frame, text="this is an example").grid(row=1, column=3)
        # is_public
        Label(self.frame, text="is public").grid(row=2)
        self.is_public = StringVar(self.frame)
        self.is_public = OptionMenu(self.frame, self.is_public, "true", "false")
        self.is_public.grid(row=2, column=1)
        Message(self.frame,
                text="this is a description more words go here, does it auto wrap around who knows i guess we "
                     "will find out very shortly").grid(row=2, column=2)
        Message(self.frame, text="this is an example").grid(row=2, column=3)
        # experience
        Label(self.frame, text="experience").grid(row=3, column=0)
        experience = Entry(self.frame)
        experience.grid(row=3, column=1)
        Message(self.frame,
                text="Each student on CodeWorkout can gain experience points for doing exercises and workouts "
                     "through CodeWorkout generally to show how often they have practiced and give them a way to "
                     "track progress. This field takes an integer for the amount of experience points the student "
                     "will gain from completing this exercise.").grid(row=3, column=2)
        Message(self.frame, text="50").grid(row=3, column=3)

        # language list
        Label(self.frame, text="language list").grid(row=4)
        language_list_starting_value = StringVar(self.frame)
        language_list_starting_value.set("java")
        language_list = OptionMenu(self.frame, language_list_starting_value, "java")
        language_list.grid(row=4, column=1)
        Message(self.frame,
                text="This field is for a list of programming languages associated with the exercise, although "
                     "this would generally be just one. This is used for sorting and grouping exercises.") \
            .grid(row=4, column=2)
        Message(self.frame, text="java").grid(row=4, column=3)

        # style list
        Label(self.frame, text="style list").grid(row=5)
        style_list = Listbox(self.frame, selectmode=MULTIPLE)
        for item in ["factorial", "function", "multiplication", "java", "code writing", "random", "forced choice",
                     "conditional", "multiple choice", "single answer"]:
            style_list.insert(END, item)
        style_list.grid(row=5, column=1)
        Message(self.frame, text="This is the type of question used in the exercise. For example, this field could be "
                                 "multiple choice, single answer, code writing, etc. This is also used for grouping "
                                 "exercises.") \
            .grid(row=5, column=2)
        Message(self.frame, text="factorial, function, multiplication").grid(row=5, column=3)

        # tag list
        Label(self.frame, text="tag list").grid(row=6)
        tag_list = Listbox(self.frame, selectmode=MULTIPLE)
        for item in ["methods", "classes", "for-loops", "recursion", "arithmetic"]:
            tag_list.insert(END, item)
        tag_list.grid(row=6, column=1)
        Message(self.frame,
                text="This is a list of other tags that should indicate the subject matter of the exercise. "
                     "This could include things such as methods, classes, for-loops, recursion, arithmetic, etc. "
                     "This is used for grouping exercises by tags.") \
            .grid(row=6, column=2)
        Message(self.frame, text="classes, recursion").grid(row=6, column=3)

        # version
        Label(self.frame, text="version").grid(row=7, column=0)
        self.version = Entry(self.frame)
        self.version.grid(row=7, column=1)
        Message(self.frame,
                text="This is a simple integer stating the current version of the exercise. This works with the "
                     "external_id (seen above) to indicate if this is a new exercise or a new version of one. "
                     "Each version of an exercise is stored in the database so that an older version can be"
                     " accessed at any point. This is important in a situation that a student would want to "
                     "review feedback from an exercise they had previously received, but the exercise had since "
                     "been altered in the database. The student would be able to access the information to the "
                     "version of the exercise they completed.").grid(row=7, column=2)
        Message(self.frame, text="1.0").grid(row=7, column=3)
        # creator
        Label(self.frame, text="creator").grid(row=8, column=0)
        self.creator = Entry(self.frame)
        self.creator.grid(row=8, column=1)
        Message(self.frame,
                text="This should include the email of the person submitting the exercise or the update to the "
                     "exercise.").grid(row=8, column=2)
        Message(self.frame, text="john.doe@email.com").grid(row=8, column=3)
        # question
        Label(self.frame, text="question").grid(row=9, column=0)
        self.question = Entry(self.frame)
        self.question.grid(row=9, column=1)
        Message(self.frame,
                text="This should include the text for the actual question in the particular prompt.")\
            .grid(row=9, column=2)
        Message(self.frame, text="john.doe@email.com").grid(row=9, column=3)
        # position
        # multiple choice or coding question
        self.multiple_choice = Button(self.frame)
        self.multiple_choice["text"] = "Multiple choice",
        self.multiple_choice["command"] = self.render_multiple_choice
        self.multiple_choice.grid(row=10, column=0)
        self.coding = Button(self.frame)
        self.coding["text"] = "Coding",
        self.coding["command"] = self.render_coding
        self.coding.grid(row=10, column=1)


        # class name (only coding questions)
        # method name (only coding questions)
        # starter code (only coding questions)
        # wrapper code (only coding questions)
        # tests (only coding questions)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root=Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()