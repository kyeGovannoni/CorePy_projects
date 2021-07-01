import sys
import urllib.request as request

def get_words(url):
    words = []
    line_of_words = request.urlopen(url)
    for line in line_of_words:
        list_words = line.decode('utf-8').split()
        for word in list_words:
            words.append(word)
    return words
    
def print_items(item):
    print(item)

def main(url):
    item = get_words(url)
    print_items(item)

if __name__ =='__main__':
    main(sys.argv[1])
    



