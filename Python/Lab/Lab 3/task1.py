"""Given a text: 
text =  machine learning is powerful 
machine learning helps analyze data 
data science uses machine learning 

Create a program that: 
1. Converts text to lowercase.  
2. Splits it into words.  
3. Counts the frequency of each word using a dictionary.  
4. Finds the most frequently occurring word.  
5. Displays unique words using a set.  
6. Displays words appearing more than once."""


text = "machine learning is powerful machine learning helps analyze data data science uses machine learning"

# Lowercase
text.lower()
print("To lowercase: \n",text)

# Splitting
splitted_text = text.split()
print("Splitting words:\n",splitted_text)

# Freduency
freq={}
for word in splitted_text:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("Frequency of words:\n",freq)


# Most frequent word
count=0
most_freq = None
for key, value in freq.items():
    if value>count:
        count=value
        most_freq=key

print(f"Most frequent word is {most_freq}, occurs {count} times")


# unique words
unique = set(freq)
print("Unique words set:\n",freq)



print("Words appearing more than once are: ")
for key,value in freq.items():
    if value>1:
        print(key)