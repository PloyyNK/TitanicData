import pandas as pd

class Titanic:
    """Provide information of titanic.csv"""

    def __init__(self):
        raw = pd.read_csv("titanic.csv")
        self.titanic = pd.DataFrame(raw)
        self.male, self.female = self.SexPercentage()
        self.AllPassengers = len(self.titanic.index)
        self.meanAge = self.titanic.Age.mean()

    def SexPercentage(self):
        """Calculate percent of all male and female passengers"""
        AllPass = len(self.titanic.index)  # number of all passengers
        AllMale = (self.titanic.Sex == 'male').sum()
        AllFemale = (self.titanic.Sex == 'female').sum()
        male = AllMale / AllPass * 100
        female = AllFemale / AllPass * 100
        return male, female

    @property
    def MalePercent(self):
        """Return percentage of male passengers"""
        return self.male

    @property
    def FemalePercent(self):
        """Return percentage of female passengers"""
        return self.female

    @property
    def FareInfoMale(self):
        """Describe female's fare information"""
        mean = self.titanic[self.titanic.Sex == "male"].Fare.mean()
        MinFare = self.titanic[self.titanic.Sex == "male"].Fare.min()
        MaxFare = self.titanic[self.titanic.Sex == "male"].Fare.max()
        return mean, MinFare, MaxFare

    @property
    def FareInfoFemale(self):
        """Describe male's fare information"""
        mean = self.titanic[self.titanic.Sex == "female"].Fare.mean()
        MinFare = self.titanic[self.titanic.Sex == "female"].Fare.min()
        MaxFare = self.titanic[self.titanic.Sex == "female"].Fare.max()
        return mean, MinFare, MaxFare

    @property
    def ComboboxTopic(self):
        """for combobox choices"""
        return list(self.titanic.Sex.unique())

    @property
    def AgeFemale(self):
        """return female average age"""
        return self.titanic[self.titanic.Sex == "female"].Age.mean()

    @property
    def AgeMale(self):
        """return male average age"""
        return self.titanic[self.titanic.Sex == "male"].Age.mean()

    @property
    def FareClassFemale(self):
        """describe each class for female gender"""
        female_df = self.titanic[self.titanic.Sex == "female"]
        class1 = female_df[female_df.Pclass == 1].Fare.mean()
        class2 = female_df[female_df.Pclass == 2].Fare.mean()
        class3 = female_df[female_df.Pclass == 3].Fare.mean()

        return class1, class2, class3

    @property
    def FareClassMale(self):
        """describe each class for male gender"""
        male_df = self.titanic[self.titanic.Sex == "male"]
        class1 = male_df[male_df.Pclass == 1].Fare.mean()
        class2 = male_df[male_df.Pclass == 2].Fare.mean()
        class3 = male_df[male_df.Pclass == 3].Fare.mean()

        return class1, class2, class3


