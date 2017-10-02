from __future__ import print_function
from collections import defaultdict as ddict
import itertools


class Bigrams():
    def __init__(self):
         self.biGrams = ddict(lambda: 0)

    def createDictionary(self,tokens):
        for i, word in enumerate(tokens):
           self.biGrams[tokens[i]] += 1
        for i, word in enumerate(tokens):
            if (i + 2) <= len(tokens):
                bigram = [tokens[j] for j in range(i, i+2)]
                self.biGrams[tuple(bigram)] += 1
        file = open("bigram.txt","w")
        file.write("\nBigram without Smoothing\n")
        file.write(str(self.biGrams))
       
       
    def createTable(self, sentence):
        wordProbability = []
        wordCount = []
        sentenceProbability = 0.0
        totalProbability = 0.0
        sentenceSplit = sentence.split()
       
        for i, word in enumerate(sentenceSplit):
            if(i+2) <= len(sentenceSplit):
                bigram = [sentenceSplit[j] for j in range(i, i+2)]
                wordCount.append((tuple(bigram),self.biGrams[tuple(bigram)]))
                bigram_count = self.biGrams[tuple(bigram)]
                prefix_count = self.biGrams[sentenceSplit[i]]
                if bigram_count and prefix_count:
                    wordProbability.append((tuple(bigram),bigram_count/prefix_count))
                else:
                     wordProbability.append((tuple(bigram),0.0))
                totalProbability = totalProbability + wordProbability[i][1]
    
        
        print("\nBiGram Details Without Smoothing")
        print("-----------------------------------------------")
        print(wordCount)
        print(wordProbability)
        print("Total Probability : ",sep='',end='')
        print(totalProbability)

class BigramsSmoothing():
    def __init__(self):
         self.biGramsSmoothing = ddict(lambda: 1)

    def createDictionary(self,tokens):
        for i, word in enumerate(tokens):
           self.biGramsSmoothing[tokens[i]] += 1
        for i, word in enumerate(tokens):
            if (i + 2) <= len(tokens):
                bigram = [tokens[j] for j in range(i, i+2)]
                self.biGramsSmoothing[tuple(bigram)] += 1
        file = open("bigramSmooting.txt","w")
        file.write("\nBigram with Smoothing\n")
        file.write(str(self.biGramsSmoothing))
       
       
    def createTable(self, sentence):
        wordProbability = []
        wordCount = []
        sentenceProbability = 0.0
        totalProbability = 0.0
        sentenceSplit = sentence.split()
       
        for i, word in enumerate(sentenceSplit):
            if(i+2) <= len(sentenceSplit):
                bigram = [sentenceSplit[j] for j in range(i, i+2)]
                wordCount.append((tuple(bigram),self.biGramsSmoothing[tuple(bigram)]))
                bigram_count = self.biGramsSmoothing[tuple(bigram)]
                prefix_count = self.biGramsSmoothing[sentenceSplit[i]]
                if bigram_count and prefix_count:
                    wordProbability.append((tuple(bigram),bigram_count/prefix_count))
                else:
                    wordProbability.append((tuple(bigram),0.0))
                totalProbability = totalProbability + wordProbability[i][1]
    
        
        print("\nBiGram Details With Smoothing")
        print("-----------------------------------------------")
        print(wordCount)
        print(wordProbability)
        print("Total Probability : ",sep='',end='')
        print(totalProbability)
        
#Turing Starts
class BigramsTuringDiscount():
    def __init__(self):
         self.biGramsInitial = ddict(lambda: 0)
        

    def createDictionary(self,tokens):
        for i, word in enumerate(tokens):
            if (i + 2) <= len(tokens):
                bigram = [tokens[j] for j in range(i, i+2)]
                self.biGramsInitial[tuple(bigram)] += 1
        self.frequencies = [(k, len(list(v))) for k, v in itertools.groupby(sorted( self.biGramsInitial.values()))]
        n1 = self.in_list(1, self.frequencies)
        
        n = len(self.biGramsInitial)
        unseenProb = n1/n
        self.biGramsTuringDiscount = ddict(lambda: unseenProb)
        for i, word in enumerate(tokens):
             if (i + 2) <= len(tokens):
                  bigram = [tokens[j] for j in range(i, i+2)]
                  c = self.biGramsInitial[tuple(bigram)]
                  ncplus = self.in_list(c+1, self.frequencies)
                  nc = self.in_list(c, self.frequencies)
                  cstar = (c + 1)*ncplus/nc
                  prob = cstar/n
                  self.biGramsTuringDiscount[tuple(bigram)] = prob
        file = open("bigramSmootingTuring.txt","w")
        file.write("\nBigram with Smoothing of Turing Discount\n")
        file.write(str(self.biGramsTuringDiscount))
     
                  
                 
    def in_list(self,c, classes):
        for i, sublist in enumerate(classes):
            if c == classes[i][0]:
                return classes[i][1]
        return 1 
       
    def createTable(self, sentence):
        wordProbability = []
        wordCount = []
        sentenceProbability = 0.0
        totalProbability = 0.0
        sentenceSplit = sentence.split()
       
        for i, word in enumerate(sentenceSplit):
            if(i+2) <= len(sentenceSplit):
                bigram = [sentenceSplit[j] for j in range(i, i+2)]
                wordCount.append((tuple(bigram),self.biGramsInitial[tuple(bigram)]))
                wordProbability.append((tuple(bigram), self.biGramsTuringDiscount[tuple(bigram)]))
        for word, prob in wordProbability:
            totalProbability = totalProbability + prob
                 
                 
        print("\nBiGram Details With Turing Discount Smoothing")
        print("-----------------------------------------------")
        print(wordCount)
        print(wordProbability)
        print("Total Probability : ",sep='',end='')
        print(totalProbability)

def main():
    textfile = "HW2_F17_NLP6320-NLPCorpusTreebank2Parts-CorpusA-Windows.txt"
    corpus = open(textfile).read()
    tokens = corpus.split()
    bigram = Bigrams()
    bigramSmoothing = BigramsSmoothing()
    bigramsTuringDiscount = BigramsTuringDiscount()
    bigram.createDictionary(tokens)
    bigramSmoothing.createDictionary(tokens)
    bigramsTuringDiscount.createDictionary(tokens)
    print("Enter the sentence")
    sentence = input()
    bigram.createTable(sentence)
    bigramSmoothing.createTable(sentence)
    bigramsTuringDiscount.createTable(sentence)
    
                 
    
    


if __name__ == "__main__":
    main()
