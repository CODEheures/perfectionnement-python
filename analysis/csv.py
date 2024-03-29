import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class SetOfParliamentMembers:

    def __init__(self, name):
        self.name = name
        self.dataframe = None

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";")

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        data = self.dataframe
        femmes = data[data.sexe == "F"]
        hommes = data[data.sexe == "H"]

        counts = np.array([len(femmes), len(hommes)])
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["femmes ({})".format(counts[0]), "hommes ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis('equal')
        ax.pie(proportions, labels=labels, autopct="%1.1f pourcents")
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        # parties list
        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party {party}'.format(party=party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party=False):
    sopm = SetOfParliamentMembers('All Mps')
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, subset in sopm.split_by_political_party().items():
            subset.display_chart()
