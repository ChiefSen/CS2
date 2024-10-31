#Seneca Greenwood
#Description: A program that takes files of election speeches to then remove any junk words (we, them, going, or) and create a frewuency of words that are used more than 10 times into a different file
#Log: 1.0
#Bugs: Had to add words twice to the junk list for files
#Features: None
#Sources: Gordie Campbell, Python For Everybody Book
import string #gives access to string variables and functions
junk_words = ['than', 'make', 'going', 'never', 'every', 'these', 'them', 'out', 'from', 'by', 'now', 'or', 'been', 'other', 'because', 'new', 'ever', 'even', 'its', 'more', 'were', 'when', 'would', 'not', 'one', 'will', 'we', 'their', 'be', 'that', 'i','said', 'come', 'comes', 'for','of','the','but', 'you', 'your', 'as','an','my','and','to','with','are','was','who','where','a','is','so','very','am','has','his','her','him','she','he','much','no','do','put','at','on','it','us','I','in','they','what','then','all','our','me','can','know','this','both','have'] #list of all words that will be deleted from the dictionary
fhand = open('trump_new.txt')        #opens the text file of Kamala's speech to the code 
counts = dict()                      #variable that opens a dictionary
for line in fhand:
    #itterates for every word in the text and gets rid of all the words in the list and measures the frequency of words
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words= line.split()
    for word in words:
        #skips the words inside the list and if it is not in the list, then it will be added to the dictonary and counted in the frequency
        if word in junk_words: 
            continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
file = open("trump_election_words.csv", "w")       #opens new file 
for key, value in counts.items():
     #when the value of the frequency of the words is more than 10 adds the words that are more than 10 to the file 
    if value > 10:                        
        file.write(key + ", " + str(value) + "\n")   
print(counts)                                       #prints the words and frequency number to file
        
