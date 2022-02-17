import PyPDF2
import pyttsx3
import argparse

# create argument parser to grab the filename
parser = argparse.ArgumentParser(description='Recieve Input Pdf')
parser.add_argument('-f', type=str, help='the pdf file to read')
parser.add_argument('-p', type=int, help='start page for pdf')
parser.add_argument('-r', type=int, help='rate to read the book')

# parse arguments form command line
args = parser.parse_args()

# start the pdf at the page entered or default to 1
if args.p:
    startpage = args.p
else:
    startpage = 1

# initialize the reader engine
engine = pyttsx3.init()

# set the reading rate
if args.r:
    engine.setProperty('rate', args.r)
else:
    engine.setProperty('rate', 250)


# open the pdf file
pdfFileObj = open(args.f, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in the pdf
numofPages = pdfReader.numPages

for pagenum in range(startpage, numofPages):
    engine.say(f'Starting {pagenum}')
    print('Reading page ', pagenum)
    pageObj = pdfReader.getPage(pagenum)
    page = pageObj.extractText()
    lines = page.splitlines()
    for line in lines:
        engine.say(line)

# run the engine
engine.runAndWait()
