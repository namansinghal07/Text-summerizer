 #Naman Singhal #singhalnaman1999@gmail.com 
#internship NLP task 
#importing 
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import heapq


# In[2]:


#reading the excel file 
df=pd.read_excel('TASK.xlsx')


# In[3]:


#checking the head 
df.head()


# In[4]:


#checking info
df.info()


# In[5]:


#droping unneccessary column 
df.drop(['TEST DATASET'],axis=1,inplace=True)


# In[6]:


#droping first row (introduction)
df.drop([0],inplace=True)


# In[ ]:


#using for loop to access every dataset in the excel sheet one by one to reduce the work to transform every passage again and again 
for i in range(1,16):
    #taking input for the number of lines you want in summary
    n=int(input(f'Enter the Number of Lines you want in summary of data set: {i}'))
    #assinging the original data set to use it for print 
    prnt=df['Unnamed: 1'][i]
    #Data preprocessing 
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', df['Unnamed: 1'][i])
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    #spliting the passage 
    sentence_list = nltk.sent_tokenize(article_text)
    #assinging first line of every data set becuase it is the main description of the medicine 
    Main=sentence_list[0]
    #removing stop words
    stopwords = nltk.corpus.stopwords.words('english')
   
    #Find Weighted Frequency of Occurrence
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
   
    #Calculating Sentence Scores
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 50:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    #using priority queue algorithm Heapq to print the sentance  
    summary_sentences = heapq.nlargest(n, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    #printing the original and summary data 
    print('\n')
    print(f'Original Data set{i}:{prnt}')
    print('\n')
    print(f'summary:{Main}{summary}')
    print('\n')
print('By Naman Singhal')
