# cara install textblob
# 1. buka anaconda promt
# 2. ketik -> conda --ver
# 3. ketik -> pip install textblob -->buat install textblob untuk sentiment analysis nya

import pandas as pd
import json
# Natural Language Toolkit ini sangat mendukung proses pengolahan bahasa natural 
# seperti classification, tokenization, stemming, tagging, parsing dll.
import nltk
from nltk.corpus import stopwords
import re

df = pd.read_json('hasil/ASEAN(en).js', lines=True)

# clean
# nltk.download('stopwords') ->sekali aja jalanin abistu bisa tinggal komen
stop_words = set(stopwords.words('english')) 

# pembuatan fungsi preprocessing atau pembersihan
def text_cleaner(text):
    newString = text.lower()
	# newString = re.sub(r'[\(\)@.\*\)]', '', newString) #ilangin @ . dan tanda kurung
	# newString = re.sub('"','', newString) # ilangin "" 
	# newString = re.sub(r"'s\b","",newString) #buat steming
    newString = re.sub("[^a-zA-Z]", " ", newString) # ilangin semua tanda baca kecuali huruf -> ^ kecuali
    # https://regex101.com/

    # ngehapus stopword -> c/: in, at dll || split -> pemisah
    tokens = [w for w in newString.split() if not w in stop_words] #isi kata2 yang bukan stopword
    
    return (" ".join(tokens)).strip() #strip() untuk ngilangin \n
	
# SENTIMENT ANALYSIS
from textblob import TextBlob

# plaritas digunakan untuk melihat seberapa positif atau negatif sebuah teks
all_polarity = 0
label = ['Positive', 'Negative']
data = [0, 0]

df1 = df['tweet']
for tweet in df1:
    tweet = text_cleaner(tweet)
    print(tweet)
    
    an = TextBlob(tweet)
    # .sentiment yang digunakan untuk mengklasifikasi atau memprediksi tweet
    if (an.sentiment.polarity >= 0):
        print("Positive")
        data[0] += 1
    else:
        print("Negative")
        data[1] += 1
    
    print(an.sentiment)
    # nilai sentiment berupa : polaritas dan subjektivitas
    # subjektivitas -> melihat value dari tweet itu adalah opini atau faktual, semakin tinggi nilainya maka opini
    
    all_polarity += an.polarity
    print("")

	
# NENTUIN RATA2 DARI POLARITY
if (all_polarity/100 > 0):
    print(all_polarity/100)
    print("")
    print('Positive')
else:
    print(all_polarity/100)
    print("")
    print('Negative')
	
	
# VISUALISASI DATA
import matplotlib.pyplot as plt

# warna hex code
colors = ['#A4F9C8', '#FFBDBD']

# Create a pie chart
plt.pie(
    # using data total)arrests
    data,
    # with the labels being officer names
    labels=label,
    # with no shadows
    shadow=True,
    # dia nanti ada yang keluar
    explode = (0.1, 0),
    # with colors
    colors=colors,
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%.1f%%',
    # size font nya
    textprops={'fontsize': 14},
)

# View the plot drop above
plt.axis('equal')

# View the plot
# plt.tight_layout()
plt.title("Sentimen Analisis ASEAN dari 100 Data Twitter Terbaru")

plt.show()