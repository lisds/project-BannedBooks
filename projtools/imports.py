import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from itertools import combinations
from projtools import concordance as conc
from projtools import graph_formats
import statistics

display('Modules imported succesfully')