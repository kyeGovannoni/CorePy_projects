import sys #sys GLOBAL name bound by import sys.
import urllib.request as request

def get_words(url): #get_words GLOBAL name bound by def get_words
    words = []
    line_of_words = request.urlopen(url)
    for line in line_of_words:# local bound by outer for loop
        list_words = line.decode('utf-8').split() # LOCAL line words bound by assignment.
        for word in list_words: # LOCAL name bound by the inner for loop.
            words.append(word)
    return words
    
def print_items(item):
    print(item)

def main(url): #LOCAL bound by function main
    item = get_words(url) #item LOCAL bound by assignment.
    print_items(item)

if __name__ =='__main__': #global dunder name bound by the sys runtime.
    main(sys.argv[1])
    



