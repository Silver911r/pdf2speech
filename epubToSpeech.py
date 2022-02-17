import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import pyttsx3
import argparse

# create argument parser to grab the filename
parser = argparse.ArgumentParser(description='Recieve Input epub')
parser.add_argument('-f', type=str, help='the epub file to read')
parser.add_argument('-c', type=int, help='start chapter for epub')
parser.add_argument('-r', type=int, help='rate to read the book')

# parse arguments from command line
args = parser.parse_args()

# start the pdf at the page entered or default to 1
if args.c:
    startchapter = args.c
else:
    startchapter = 0

# initialize the reader engine
engine = pyttsx3.init()

# set the reading rate
if args.r:
    engine.setProperty('rate', args.r)
else:
    engine.setProperty('rate', 250)


def chap2text(chap):
    blacklist = ['[document]', 'noscript', 'header',
                 'html', 'meta', 'head', 'input', 'script']
    output = ""
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{}'.format(t)
    return output


book = epub.read_epub(args.f)

chapters = []
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        chapters.append(item.get_content())


for chapter in chapters[startchapter:]:
    # read the page from the epub reader
    text = chap2text(chapter)
    engine.say(text)
    engine.runAndWait()

# text = chap2text(chapters[2])
# lines = text.splitlines()
