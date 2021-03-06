# -*- coding: utf-8 -*-
"""Q7-Revised.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sjtiD6MftbTkqYx1Q__XfGWIcwYsLLG5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('NetflixOriginals.csv', encoding='ISO-8859-1')

top_10_movies_df = df.loc[df["IMDB Score"].nlargest(10).keys()]
top_10_movies_df[["Title", "IMDB Score"]].style.hide_index()
