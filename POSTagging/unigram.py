from __future__ import division
from collections import defaultdict as ddict,Counter

def main():
    corpus = open("HW2_F17_NLP6320_POSTaggedTrainingSet-Windows.txt").read()
    tag = {}
    tokens = corpus.split()
    for i in range(0, len(tokens)):
        tokens[i] = tokens[i].split("_")
    wordTagCounts = ddict(lambda: ddict(lambda: 0))
    #Get the counts of all tags of the world
    for words, tags in tokens:
        wordTagCounts[words][tags] += 1
    for word in wordTagCounts:
        tagCounts = wordTagCounts[word]
        mostProbableTag = max(tagCounts, key=tagCounts.get)
        tag[word] = mostProbableTag
    file = open("unigrams.txt","w")
    file.write("\nMost Probable tags of the words given\n")
    file.write(str(tag))

    print("\nEnter the sentence for POS Tagging:")
    sentence = input()
    sentenceSplit = sentence.split()
    sentenceTags = []
    for i,word in enumerate(sentenceSplit):
        if(word in tag):
            sentenceTags.append([word,tag[word]])
        else:
            sentenceTags((word,"NN"))
    print(sentenceTags)
    print("\nEnter tagged sentence:")
    taggedSentence = input()
    taggedSentenceSplit = taggedSentence.split()
    for i in range(0, len(taggedSentenceSplit)):
        taggedSentenceSplit[i] = taggedSentenceSplit[i].split("_")
    print(taggedSentenceSplit)
    denominator = len(sentenceSplit)
    numerator = 0.0
    for i in range(0 , len(sentenceSplit)):
        if taggedSentenceSplit[i][1] != sentenceTags[i][1]:
            numerator +=1
    errorProbability = numerator/denominator
    print("\nThe error in the tagged sentence is:")
    print(errorProbability)
    print("\nTotal number of wrongly Tagged words is:")
    print(numerator)
        

if __name__=="__main__":
    main()
