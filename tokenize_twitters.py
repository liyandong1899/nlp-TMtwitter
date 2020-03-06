import nltk
file_content = open("/Users/lichao/PycharmProjects/toni_morison/venv/lib/corpora").read()
tokens = nltk.word_tokenize(file_content)
tokenSet=set(tokens)
print(tokenSet)
print(len(tokenSet))
import warnings

warnings.filterwarnings(action='ignore')

import gensim
from nltk.tokenize import sent_tokenize, word_tokenize

from gensim.models import Word2Vec

sample=open('/Users/lichao/PycharmProjects/toni_morison/venv/lib/corpora','r')
s=sample.read()
f=s.replace("\n"," ")
data=[]

for i in sent_tokenize(f):
    temp=[]
    for j in word_tokenize(i):
        temp.append(j.lower())
    data.append(temp)

model1=Word2Vec(data,min_count=1,size=100,window=5,sg=1)
model2=Word2Vec(data,min_count=1,size=100,window=5)

print(model1.similarity("toni","morrison"))
print(model1.similarity("passing","beloved"))

print(model2.similarity("toni","morrison"))
print(model2.similarity("passing","beloved"))