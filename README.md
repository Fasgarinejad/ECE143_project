# ECE143_project (Group 2)

**Structure of files**


- **Analysis**
    - **Codes**
        - **Authors** | **Genres** | **Books Features**
    - **Datasets**
    - **images**
         - plots we have generated from our data analysis
    
- **PDF of Slides**
    -  titled Group2_ppt_final.pdf
- **Jupyter Notebook** (Code.ipynb)
- **Website**
    - **Website**
    - **Images**
- **Timeline**
- **Method Test Cases Assignment**
    -  the file is named "Group-2_Assignment-1.ipynb"


**Running our code**

We have uploaded the Jupyter notebook containing all genres in the main page and also the `.py` files for each plot/querry in the Analysis folder 

STEPS TO RUN OUR NOTEBOOK:
(1) Clone our repository 
```
git clone https://github.com/Fasgarinejad/ECE143_project
```
(2) After the download has finished, unzip the file and follow filepath: Analysis > Datasets
(3) Download all the files in the Dataset folder ('good_reads_final.csv' and 'books.csv' are already downloaded, but you need to unzip 'book_data.csv.zip' and click the README.md to get a link to download 'final_dataset.csv')
(4) create a new folder and move all four .csv files into it.
(5) drag the 'Code.ipynb' Jupyter notebook into the same folder you have created
(6) open Terminal, and type in the command 'jupyter notebook'. a window should pop up and follow the file path to get to where your 'Code.ipynb' and click to open it
(7) make sure to pip or conda install the 3rd party modules we have listed below 
(8) Run our Jupyter Notebook

Note: We are using this version of Python:
```
Python 3.8 
```

**All Third-party modules we have used**

Main ones:

- matplotlib
- pandas
- sklearn
- numpy
- nltk
- wordcloud #!conda install -c conda-forge wordcloud=1.6.0 

1. from sklearn.ensemble import RandomForestClassifier #Random Forest
2. Pandas #for importing csv file and working with dataframes
3. Numpy #for sum mathematical stuff in the dataframes
4. matplotlib #for plotting
5. csv #for opening datafiles and reading them into dataframes
6. seaborn #to add more plot features and layout
7. collections #for OrderedDict, sort dict
8. nltk  #for string analysis (stopwords, punctuations, etc.)
9. random #for generating random numbers for random colors 
10. string #for working with string data
11. time #For calculating time spent for prediction
12. basemap
13. import re
14. import collections
15. from collections import Counter
16. from wordcloud import WordCloud
17. from wordcloud import WordCloud, ImageColorGenerator
18. from PIL import Image
19. import seaborn as sns 
20. from sklearn.preprocessing import StandardScaler
21. from sklearn.pipeline import make_pipeline
22. from sklearn.svm import SVC
23. from sklearn.model_selection import train_test_split
24. from sklearn.metrics import accuracy_score
25. from sklearn.model_selection import ShuffleSplit
26. import sklearn
27. from sklearn.ensemble import RandomForestClassifier
28. from sklearn.datasets import make_classification


