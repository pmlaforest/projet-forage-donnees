# Add needed packages-----------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
from dython.nominal import associations

def main():

    # Data importation -------------------------------------------------------------
    df = pd.read_csv("agaricus-lepiota.csv")

    panda_rules()
    # Construct barplot ===================================================
    make_barplot(df,"odor")
    make_barplot(df,"spore-print-color")

    # Make heatmap to show correlation between attribute
    associations(df, nominal_columns="all") # Use Cramer V nominal association
    associations(df, nominal_columns="all", theil_u=True) # Use Theil's U nominal association

    # Construct Pie chart ===================================================
    make_pie_chart(df,"odor")

    # Show the number of mushroom for each odor =============================
    count_value_for_attribute(df,"odor")

    # Find the number of instance in each class ==============================
    find_nb_instance_class(df)
    print("==============================")

    # Count the number of edible mush by odor ==============================
    count_edible_mush_by_odor(df)
    print("==============================")

    # Count the number of toxic mush by odor ==============================
    count_toxic_mush_by_odor(df)
    print("==============================")

    # Count the number of toxic mush by spore color ==============================
    count_toxic_mush_by_spore_color(df)
    print("==============================")

    # Count the number of edible mush by spore-color ==============================
    count_edible_mush_by_spore_color(df)
    print("==============================")

    # All mush with spore-color green are poisonous
    show_rules_two(df)
    print("==============================")

    # All mush with habitat = leaves and cap-color = white are poisonous
    show_rules_four(df)
    print("==============================")
    return


def make_barplot(df,attribute):
    value_count = df[attribute].value_counts()
    sns.set(style="darkgrid")
    sns.barplot(value_count.index, value_count.values, alpha=0.9)
    plt.title('Frequency distribution of mushroom ' + attribute)
    plt.ylabel("Number of Occurences", fontsize=12)
    plt.xlabel(attribute, fontsize=12)
    plt.show()

def make_pie_chart(df,attribute):
    labels = df[attribute].astype('category').cat.categories.tolist()
    counts = df[attribute].value_counts()
    sizes = [counts[var_cat] for var_cat in labels]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True) #autopct is show the % on plot
    ax1.axis('equal')
    plt.title("Distribution of " + attribute)
    plt.show()

def count_value_for_attribute(df,attribute):
    print(df[attribute].value_counts())

def find_nb_instance_class(df):
    # filter the data to only keep the edible mushrooms
    edible = df[df['edibility'] =='e']

    # filter the data to only keep the poisonous mushrooms
    poisonous = df[df['edibility']=='p']

    print("There is "+ str(edible['edibility'].count()) + " edible mushrooms")
    print("There is "+ str(poisonous['edibility'].count()) + " poisonous mushrooms")

def count_edible(df):
    edible = df[df['edibility'] =='e']
    num_edible = edible['edibility'].count()
    return num_edible

def count_toxic(df):
    toxic = df[df['edibility'] =='p']
    num_toxic = edible['edibility'].count()
    return num_toxic

def panda_rules():
    # Modify display rule of panda
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None

    return


def count_edible_mush_by_odor(df):
    almond = df[(df['edibility'] == 'e') & (df['odor'] == 'a')]
    print("There is "+ str(almond['edibility'].count()) + " edible mushrooms who smell almond")

    anise = df[(df['edibility'] == 'e') & (df['odor'] == 'l')]
    print("There is "+ str(anise['edibility'].count()) + " edible mushrooms who smell anise")

    creosote = df[(df['edibility'] == 'e') & (df['odor'] == 'c')]
    print("There is "+ str(creosote['edibility'].count()) + " edible mushrooms who smell creosote")

    fishy = df[(df['edibility'] == 'e') & (df['odor'] == 'y')]
    print("There is "+ str(fishy['edibility'].count()) + " edible mushrooms who smell fishy")

    foul = df[(df['edibility'] == 'e') & (df['odor'] == 'f')]
    print("There is "+ str(foul['edibility'].count()) + " edible mushrooms who smell foul")

    musty = df[(df['edibility'] == 'e') & (df['odor'] == 'm')]
    print("There is "+ str(musty['edibility'].count()) + " edible mushrooms who smell musty")

    none = df[(df['edibility'] == 'e') & (df['odor'] == 'n')]
    print("There is "+ str(none['edibility'].count()) + " edible mushrooms who dont smell anything")

    pungent = df[(df['edibility'] == 'e') & (df['odor'] == 'p')]
    print("There is "+ str(pungent['edibility'].count()) + " edible mushrooms who smell pungent")

    spicy = df[(df['edibility'] == 'e') & (df['odor'] == 's')]
    print("There is "+ str(spicy['edibility'].count()) + " edible mushrooms who smell spicy")

    return

def count_toxic_mush_by_odor(df):
    almond = df[(df['edibility'] == 'p') & (df['odor'] == 'a')]
    print("There is "+ str(almond['edibility'].count()) + " toxic mushrooms who smell almond")

    anise = df[(df['edibility'] == 'p') & (df['odor'] == 'l')]
    print("There is "+ str(anise['edibility'].count()) + " toxic mushrooms who smell anise")

    creosote = df[(df['edibility'] == 'p') & (df['odor'] == 'c')]
    print("There is "+ str(creosote['edibility'].count()) + " toxic mushrooms who smell creosote")

    fishy = df[(df['edibility'] == 'p') & (df['odor'] == 'y')]
    print("There is "+ str(fishy['edibility'].count()) + " toxic mushrooms who smell fishy")

    foul = df[(df['edibility'] == 'p') & (df['odor'] == 'f')]
    print("There is "+ str(foul['edibility'].count()) + " toxic mushrooms who smell foul")

    musty = df[(df['edibility'] == 'p') & (df['odor'] == 'm')]
    print("There is "+ str(musty['edibility'].count()) + " toxic mushrooms who smell musty")


    none = df[(df['edibility'] == 'p') & (df['odor'] == 'n')]
    print("There is "+ str(none['edibility'].count()) + " toxic mushrooms who dont smell anything")

    pungent = df[(df['edibility'] == 'p') & (df['odor'] == 'p')]
    print("There is "+ str(pungent['edibility'].count()) + " toxic mushrooms who smell pungent")

    spicy = df[(df['edibility'] == 'p') & (df['odor'] == 's')]
    print("There is "+ str(spicy['edibility'].count()) + " toxic mushrooms who smell spicy")

    return

def count_toxic_mush_by_spore_color(df):
    # toxic mushroom with green spore color
    green = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'r')]
    print("There is "+ str(green['edibility'].count()) + " poisonous mushroom with green spore")

    # toxic mushroom with brown spore color
    brown = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'n')]
    print("There is "+ str(brown['edibility'].count()) + " poisonous mushroom with brown spore")

    # toxic mushroom with black spore color
    black = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'k')]
    print("There is "+ str(black['edibility'].count()) + " poisonous mushroom with black spore")

    # toxic mushroom with buff spore color
    buff = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'b')]
    print("There is "+ str(buff['edibility'].count()) + " poisonous mushroom with buff spore")

    # toxic mushroom with chocolate spore color
    chocolate = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'h')]
    print("There is "+ str(chocolate['edibility'].count()) + " poisonous mushroom with chocolate spore")

    # toxic mushroom with orange spore color
    orange = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'o')]
    print("There is "+ str(orange['edibility'].count()) + " poisonous mushroom with orange spore")

    # toxic mushroom with purple spore color
    purple = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'u')]
    print("There is "+ str(purple['edibility'].count()) + " poisonous mushroom with purple spore")

    # toxic mushroom with white spore color
    white = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'w')]
    print("There is "+ str(white['edibility'].count()) + " poisonous mushroom with white spore")

    # toxic mushroom with yellow spore color
    yellow = df[(df['edibility'] == 'p') & (df['spore-print-color'] == 'y')]
    print("There is "+ str(yellow['edibility'].count()) + " poisonous mushroom with yellow spore")

    return

def count_edible_mush_by_spore_color(df):
     # toxic mushroom with green spore color
     green = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'r')]
     print("There is "+ str(green['edibility'].count()) + " edible mushroom with green spore")

     # toxic mushroom with brown spore color
     brown = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'n')]
     print("There is "+ str(brown['edibility'].count()) + " edible mushroom with brown spore")

     # toxic mushroom with black spore color
     black = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'k')]
     print("There is "+ str(black['edibility'].count()) + " edible mushroom with black spore")

     # toxic mushroom with buff spore color
     buff = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'b')]
     print("There is "+ str(buff['edibility'].count()) + " edible mushroom with buff spore")

     # toxic mushroom with chocolate spore color
     chocolate = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'h')]
     print("There is "+ str(chocolate['edibility'].count()) + " edible mushroom with chocolate spore")

     # toxic mushroom with orange spore color
     orange = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'o')]
     print("There is "+ str(orange['edibility'].count()) + " edible mushroom with orange spore")

     # toxic mushroom with purple spore color
     purple = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'u')]
     print("There is "+ str(purple['edibility'].count()) + " edible mushroom with purple spore")

     # toxic mushroom with white spore color
     white = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'w')]
     print("There is "+ str(white['edibility'].count()) + " edible mushroom with white spore")

     # toxic mushroom with yellow spore color
     yellow = df[(df['edibility'] == 'e') & (df['spore-print-color'] == 'y')]
     print("There is "+ str(yellow['edibility'].count()) + " edible mushroom with yellow spore")

def show_rule_one(df):
    count_toxic_mush_by_odor(df)

def show_rules_two(df):
    # All mush with spore-color green are poisonous
    toxic = df[df['spore-print-color'] == 'r']
    print(toxic['edibility'])

def show_rules_four(df):
    # All mush with habitat = leaves and cap-color = white are poisonous
    toxic = df[(df['habitat'] == 'l') & (df['cap-color'] == 'w')]
    print(toxic['edibility'])

main()
