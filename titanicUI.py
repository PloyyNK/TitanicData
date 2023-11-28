import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
from titanic_class import Titanic
from graph import Graph

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class TitanicUI(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.t = Titanic()
        self.bg = tk.PhotoImage(file="titanic1.gif")
        self.ct = self.t.ComboboxTopic
        self.graph = Graph()

        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        """element for program"""
        # add background image
        back = tk.Label(self, image=self.bg)
        back.place(x=0, y=0)

        # summary area
        self.summary = ttk.LabelFrame(self, text="Description")
        self.summary.grid(row=1, column=0, sticky="NEWS")

        # creating a row with combobox widgets for filters
        self.label_frame = ttk.LabelFrame(self, text="Select Information")
        self.label_frame.grid(row=2, column=0, sticky="NEWS")

        # combobox for gender selection
        label1 = ttk.Label(self.label_frame, text="Gender")
        label1.grid(row=0, column=0)
        self.gender_select = tk.StringVar()
        self.GenderSelect = ttk.Combobox(self.label_frame, state="readonly", textvariable=self.gender_select)
        self.GenderSelect.bind('<<ComboboxSelected>>')  # , self.update_filters
        self.GenderSelect.grid(row=1, column=0, padx=10, pady=10)
        self.GenderSelect.config(values=sorted(self.ct))

        # combobox for info selection
        label2 = ttk.Label(self.label_frame, text="x-axis")
        label2.grid(row=0, column=1)
        self.info_select = tk.StringVar()
        self.InfoSelect = ttk.Combobox(self.label_frame, state="readonly", textvariable=self.info_select)
        self.InfoSelect.bind('<<ComboboxSelected>>')
        self.InfoSelect.grid(row=1, column=1, padx=10, pady=10)
        self.InfoSelect.config(values=["Age", "Pclass"])

        # combobox for graph type
        label3 = ttk.Label(self.label_frame, text="Graph type")
        label3.grid(row=0, column=2)
        self.graph_type = tk.StringVar()
        self.GraphTypeSelect = ttk.Combobox(self.label_frame, state="readonly", textvariable=self.graph_type)
        self.GraphTypeSelect.bind("<<ComboboxSelected>>")
        self.GraphTypeSelect.grid(row=1, column=2, padx=10, pady=10)
        self.GraphTypeSelect.config(values=["scatter", "bar"])

        self.QuitButton = ttk.Button(self.label_frame, text="Quit", command=self.quit)
        self.QuitButton.grid(row=3, column=0, pady=10, padx=10)

        self.PlotButton = ttk.Button(self.label_frame, text="Plot", command=self.check_input)
        self.PlotButton.grid(row=3, column=2, pady=10, padx=10)

        # plot graph area
        self.fig = Figure()
        self.axes = self.fig.add_subplot()

        self.fig_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.fig_canvas.get_tk_widget().grid(row=0, column=0, sticky="NEWS", padx=10, pady=10)
        self.rowconfigure(1, weight=1)

    def show_graph(self):
        """plotting the graph"""
        graph_type = self.GraphTypeSelect.get()
        self.gender = self.GenderSelect.get()
        self.wanted_info = self.InfoSelect.get()
        self.clear_label()
        self.describe_graph()

        self.axes.clear()
        self.fig.subplots_adjust(bottom=0.25)
        self.graph.set_graph(graph_type)
        self.graph.set_gender(self.gender)
        self.graph.plotGraph(self.gender, self.wanted_info, self.axes)
        self.fig_canvas.draw()

    def clear_label(self):
        """clear the label in summary area"""
        for label in self.summary.winfo_children():
            label.destroy()

    def describe_graph(self):
        """summary for the graph"""
        mean_men, MinFare_men, MaxFare_men = self.t.FareInfoMale
        mean_female, MinFare_female, MaxFAre_female = self.t.FareInfoFemale
        male_c1, male_c2, male_c3 = self.t.FareClassMale
        female_c1, female_c2, female_c3 = self.t.FareClassFemale

        all_pass = ttk.Label(self.summary,
                             text=f"Total of passengers on board: {self.t.AllPassengers} passengers",
                             justify="left")
        all_pass.grid(row=0, column=0)

        if self.gender == "male":
            male = ttk.Label(self.summary,
                             text=f"Percentage of men on board: {self.t.MalePercent:.2f}%",
                             justify="left")
            sum_men = ttk.Label(self.summary,
                                text=f"Average fare: {mean_men:.2f}\n "
                                     f"Minimum fare: {MinFare_men:.2f}\n"
                                     f"Maximum fare: {MaxFare_men:.2f} ",
                                justify="center")
            sum_men.grid(row=2, column=1)
            male.grid(row=2, column=0)

            if self.wanted_info == "Age":
                mean_age = ttk.Label(self.summary,
                                     text=f"Men average age: {self.t.AgeMale:.1f}",
                                     justify="left")
                mean_age.grid(row=3, column=0)
            elif self.wanted_info == "Pclass":
                fare_by_class = ttk.Label(self.summary,
                                          text=f"Average Fare by class:\n"
                                               f"           1st class: {male_c1:.2f}\n"
                                               f"           2nd class: {male_c2:.2f}\n"
                                               f"           3rd class: {male_c3:.2f}",
                                          justify="left")
                fare_by_class.grid(row=3, column=0)

        elif self.gender == "female":
            female = ttk.Label(self.summary,
                               text=f"Percentage of women on board: {self.t.FemalePercent:.2f}%",
                               justify="left")
            sum_female = ttk.Label(self.summary, text=f"Average fare: {mean_female:.2f}\n "
                                                      f"Minimum fare: {MinFare_female:.2f}\n"
                                                      f"Maximum fare: {MaxFAre_female:.2f} ",
                                   justify="center")
            sum_female.grid(row=2, column=1)
            female.grid(row=2, column=0)

            if self.wanted_info == "Age":
                mean_age = ttk.Label(self.summary,
                                     text=f"Female average age: {self.t.AgeFemale:.1f}",
                                     justify="left")
                mean_age.grid(row=3, column=0)
            elif self.wanted_info == "Pclass":
                fare_by_class = ttk.Label(self.summary,
                                          text=f"Average Fare by class:\n"
                                               f"           1st class: {female_c1:.2f}\n"
                                               f"           2nd class: {female_c2:.2f}\n"
                                               f"           3rd class: {female_c3:.2f}",
                                          justify="left")
                fare_by_class.grid(row=3, column=0)

    def check_input(self, event=None):
        """check if the combobox have been all fill"""
        try:
            self.show_graph()
        except:
            if self.GenderSelect.get() == "":
                self.gender_select.set("Please pick information")
            if self.InfoSelect.get() == "":
                self.info_select.set("Please pick information")
            if self.GraphTypeSelect.get() == "":
                self.graph_type.set("Please pick information")
