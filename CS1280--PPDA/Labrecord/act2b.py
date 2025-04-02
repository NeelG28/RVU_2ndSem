def word_count(sentence):
    words=sentence.split()
    word_freq={}
    for w in words:
        if w in word_freq:
            word_freq[w]+=1
        else:
            word_freq[w]=1
    return len(words),word_freq
sentence=input("Enter a sentence : ")
print(f"The number of words in the sentence and their respective frequences are : {word_count(sentence)}")
