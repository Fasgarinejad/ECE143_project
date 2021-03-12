# ECE143_project (Group 2)

**Structure of files**


- **Analysis**
    - **Codes**
        - **Authors** | **Genres** | **Books Features**
    - **Datasets**
    - **images**
    
- **PDF of Slides**
- **Jupyter Notebook**
- **Website**
    - **Website**
    - **Images**
- **Timeline**


**Running our code**


**All Third-party modules we have used**
1. Basemap
2. Pandas #for importing csv file and working with dataframes
3. Numpy #for sum mathematical stuff in the dataframes
4. matplotlib #for plotting
5. csv #for opening datafiles and reading them into dataframes
6. seaborn #to add more plot features and layout
7. collections #for OrderedDict, sort dict
8. nltk  #for string analysis (stopwords, punctuations, etc.)
9. random #for generating random numbers for random colors 
10. string #for working with string data
11. time For calculating time spent for prediction




import re  
import collections
from collections import Counter
from wordcloud import WordCloud
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import ShuffleSplit
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


