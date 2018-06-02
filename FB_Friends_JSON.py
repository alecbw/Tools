# -*- coding: utf-8 -*-
from pprint import pprint
from bs4 import BeautifulSoup
from openpyxl import Workbook , load_workbook

wb1 = Workbook()    # Setting up new Workbook (Excel Sheet) to write to
ws1 = wb1.active

ws1['A1'] = "Name"  # Setting up headers in the first row
ws1['B1'] = "Date"
ws1['C1'] = "Link"

count1 = 0          # Setting up counter variable, intentionally at zero

############ ~ Paste your HTML between the three quotation marks ~ ############
FB_HTML = """

YOUR_HTML_GOES_HERE

"""
############ ~ Paste your HTML between the three quotation marks ~ ############


parsed = BeautifulSoup(FB_HTML, 'lxml') # Setting up parser variable
print parsed.a
for parsed_li in parsed.findAll('a'):
    count1 += 1

print count1

for parsed_li in parsed.findAll('li', {'class': "_43q7"}): # Querying into li for each individual

    for a in parsed_li.findAll('a', {'class': "link"}):
        # Info, Name, Date, Link = "" * 4 # Intentionally overwrite holder variables
        count1 += 1                     # Increment counter variable

        Link = a['href']                 # Get FB Profile Link
        Info = a['data-tooltip-content'] # Get string with our wanted substrings in it
        Name = Info.split(" (",1)[0]     # Get Name substring from Info string
        Date = Info.split(" (",1)[1]     # Get Date substring from Info string
        Date = Date.replace(")", "")     # Overwrite Date to remove trailing parenthesis

        ws1['A' + str(count1)] = Name   # Writing each variable to the Workbook
        ws1['B' + str(count1)] = Date
        ws1['C' + str(count1)] = Link

wb1.save("FB Friends2.xlsx") # Saving our file (as an xlsx filetype)

