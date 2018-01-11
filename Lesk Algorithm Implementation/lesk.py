from nltk.corpus import wordnet, stopwords 
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import sys

def main():
    sentence = input("Enter the Sentence :")
    word = input("Enter the word :")
    synset = lesk(sentence, word)
    print("\nThe sense with maximum overlap and the sense of word in sentence")
    print("-------------------------------------------------------------------")
    print(synset)
    
    
def lesk(sentence, word):  
    
    print("The senses and the overlaps")
    print("-----------------------------")
    maxoverlap = 0
    bestsense = None
    for synset in wordnet.synsets(word):
        overlap = getoverlap(sentence, synset)
        for hyponym in synset.hyponyms():
            overlap += getoverlap(sentence, hyponym)
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = synset
        print(synset, overlap, sep=':', end='\n', file=sys.stdout)
    return bestsense

def getoverlap(sentence, synset):
    tokenizer = RegexpTokenizer(r'\w+')
    gloss = set(tokenizer.tokenize(synset.definition()))
    stop_words = set(stopwords.words('english'))
    for i in synset.examples():
        gloss.union(i)
    gloss = gloss.difference(stop_words)
    sentence = set(sentence.split(" "))
    sentence = sentence.difference(stop_words)
    overlap = len(gloss.intersection(sentence))
    return overlap




if __name__ == "__main__":
    main()
