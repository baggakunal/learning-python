import sys
from urllib.request import urlopen

# URL: 'http://sixty-north.com/c/t.txt'

def fetch_words(url):
    story = urlopen(url);
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        first = True
        for word in line_words:
            if first == True:
                story_words.append(word.capitalize())
                first = False
            else:
                story_words.append(word)
        story_words.append('\n')
    story.close();
    return story_words


def print_items(items):
    for item in items:
        if item == '\n':
            print(item, sep='', end='')
        else:
            print(item, sep='', end=' ')


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
