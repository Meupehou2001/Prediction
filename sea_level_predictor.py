import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lecture des données
    data = pd.read_csv('epa-sea-level.csv')
    
    # Création du nuage de points
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Données observées')

    # Ligne de tendance pour l'ensemble des données
    result_all = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = result_all.intercept + result_all.slope * x_all
    plt.plot(x_all, y_all, color='orange', label='Ligne de tendance (1880-2050)')

    # Ligne de tendance à partir de 2000
    data_2000 = data[data['Year'] >= 2000]
    result_2000 = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = result_2000.intercept + result_2000.slope * x_2000
    plt.plot(x_2000, y_2000, color='green', label='Ligne de tendance (2000-2050)')

    # Configuration des étiquettes et du titre
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Sauvegarde et affichage de l'image
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()