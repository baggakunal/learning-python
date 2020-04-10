"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
    Sample url: http://sixty-north.com/c/t.txt
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of string containing the words from the document.

    Raises:
        None
    """
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
    """Print items in the same line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        if item == '\n':
            print(item, sep='', end='')
        else:
            print(item, sep='', end=' ')


def main(url):
    """Print each word from a text document retrieved from the url.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
