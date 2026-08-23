import requests

url = "https://university-of-pennsylvania.cafebonappetit.com/"
response = requests.get(url) #get the dining page and all the data that it has. this is a blob

print()
print("Scraping the dining page...")
print(response.status_code)
print(len(response.text)) #yeah ur cooked bro 2 million characters

#First part of the puzzle: extracting the data as a String. From reading the HTML, it seems like
# each daypart (what time of day) tells us what dining hall is open (in military time), when it's open, and what menu IDs there are. 
# But we don't actually know what each ID corresponds to what.  

#First part of scraper

text = response.text

dayparts_array = []

while True:
    #this thing should keep looping through the entire string until it finds all the dayparts and stores them in the array

    start = text.find('Bamco.dayparts[')
    end = text.find(']}]',start) #dumbahh implementation icl

    print(start, end)

    if start == -1 or end == -1: #exit the loop if there's no more dayparts to find
        break

    daypart_string = text[start:end+3]
    dayparts_array.append(daypart_string)

    text = text[end+3:]  #hella destructive but wtv we ball

for string in dayparts_array:
    pos = string.find("{")

    replacement = string[pos:] #this is to fix the formatting of the daypart string so that it can be parsed as JSON later
    replacement += "}" #this is to fix the formatting of the daypart string so that it can be parsed as JSON later

    dayparts_array[dayparts_array.index(string)] = replacement

print(dayparts_array[0]) #this is the array of all the dayparts. each daypart has a name, start time, end time, and menu IDs.

"""
#we gonna create ts as a file and then read it manually
with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)
"""