import pandas as pd


class Graph:
    def __init__(self):
        self.scatter = ScatterGraph()
        self.bar = BarGraph()
        self.graph = None

    def set_graph(self, type_graph):
        if type_graph == "scatter":
            self.graph = self.scatter
        elif type_graph == "bar":
            self.graph = self.bar

    def set_gender(self, sex):
        self.graph.sex = sex

    def plotGraph(self, gender, x_type, ax):
        return self.graph.plotGraph(gender, x_type, ax)


class GraphState:

    def __init__(self):
        self.titanic = pd.read_csv("titanic.csv")
        self._gender = ""

    def plotGraph(self, gender, x_type, ax):
        pass

    @property
    def sex(self):
        return self._gender

    @property
    def gender(self):
        return self.titanic[self.titanic.Sex == self.sex]

    @sex.setter
    def sex(self, value):
        self._gender = value


class ScatterGraph(GraphState):
    def __init__(self):
        super().__init__()

    def plotGraph(self, gender, x_type, ax):
        return self.gender.plot.scatter(x=x_type, y="Fare", ax=ax)


class BarGraph(GraphState):
    def __init__(self):
        super().__init__()

    def plotGraph(self, gender, x_type, ax):
        bar_graph = self.gender.groupby(self.titanic[x_type])["Fare"].mean()
        return bar_graph.plot.bar(ax=ax)
