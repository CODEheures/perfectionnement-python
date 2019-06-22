import pandas as pd

famille = [
    [100, 20, 5, 30], #papa
    [80, 18, 4, 25], #maman
    [40, 10, 2.5, 15], #bb
]

index = ['papa', 'maman', "bb"]
columns = ['pattes', 'poil', 'griffes', 'tete']

famille_dataFrame = pd.DataFrame(data=famille, index=index, columns=columns)
print(famille_dataFrame.columns)

print(famille_dataFrame)
print(famille_dataFrame.griffes)
print(famille_dataFrame.griffes.values)

for ligne in famille_dataFrame.iterrows():
    index = ligne[0]
    contenu = ligne[1]
    print("{index} panda".format(index=index))
    print(contenu)
    print("==============")

#bb panda
print(famille_dataFrame.iloc[2])
print(famille_dataFrame.loc['bb'])

print(famille_dataFrame.griffes >= 4)
masque = famille_dataFrame.griffes >= 4
print(famille_dataFrame[masque])
print(famille_dataFrame[~masque])

# ajout
ajout_pandas = pd.DataFrame([[85, 17, 4, 22], [100, 20, 5, 30]], columns=famille_dataFrame.columns)
tous = famille_dataFrame.append(ajout_pandas)
print(tous)

#without duplicates
print(tous.drop_duplicates())

# ajout colonne
tous['sexe'] = ['M', 'F', 'F', 'M', 'M']
print(tous)

#len
print(len(tous))

# valeurs uniques
print(tous.griffes.unique())

#read csv
mps = pd.read_csv("data/current_mps.csv", sep=";")