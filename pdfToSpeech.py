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

# start the loop to read the pdf from the first page or selected page
for pagenum in range(startpage, numofPages):
    # printe a header to organize the text printed
    print(pagenum, '-'*50)
    print()
    print()
    # read the page from the pdf reader
    pageObj = pdfReader.getPage(pagenum)
    # extract the text from the page obj
    page = pageObj.extractText()
    # turn the text into lines, speech engine errors out if not
    lines = page.splitlines()
    # feed each line into the engine.say() for reading when engine run called
    for line in lines:
        engine.say(line)
        print(line)
    # run the engine to read lines fed in for this page
    engine.runAndWait()
