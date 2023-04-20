from tkinter import *
import random

with open("Bible ASV", "r") as Bible:
    BibleText = Bible.read()

Verses = BibleText.split("\n")

allBooks = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
            "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms",
            "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel",
            "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi",
            "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians",
            "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy",
            "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"] 

openPage = ""
currentPage = 0

def createInterface():
    global bibleText
    global variable
    global verseSelector
    window = Tk()

    variable = StringVar(window)
    variable.set(allBooks[0])

    BookSelector = OptionMenu(window, variable, *allBooks)
    BookSelector.grid(row = 0, column = 1)

    verseSelector = Entry(window)
    verseSelector.grid(row = 0, column = 2)

    searchVerse = Button(window, text="search verse", bg="cyan", width = 15, height = 4,
                         command = lambda verseSelector = verseSelector, variable = variable:search(variable.get(), verseSelector.get()))
    searchVerse.grid(row = 0, column = 3)

    bibleText = Text(window, width=60, height=30, bg="aqua")
    bibleText.grid(row = 1, column = 0, columnspan = 4)

    empty = Label(window, height=1, bg="darkturquoise")
    empty.grid(row = 2)

    backwards = Button(window, width=20, height=3, text="← Page", bg = "cyan", font=("Dosis", 12),
                       command=lambda: changePages(-1))
    backwards.grid(row = 3, column = 1)

    backwards = Button(window, width=20, height=3, text="Page →", bg = "cyan", font=("Dosis", 12),
                       command=lambda: changePages(1))
    backwards.grid(row = 3, column = 3)

    window.configure(bg = "darkturquoise")    
    window.title("Bible")
    window.geometry("520x650")
    window.mainloop()

def search(book, verse):
    global bibleText
    global openPage
    global currentPage

    currentPage = 0

    openPage = book + " " + verse
    
    if ":" in verse:
        verse += "\t"
    elif len(verse) == 1:
        verse += ":"

    result = ""
    for each in Verses:
        if book + " " + verse in each:
            result += each.split(":")[-1].replace("\t", " ") + "\n"
            
    bibleText.delete("1.0", "end")
    bibleText.insert("1.0", result)

def showverse(verseIndex):
    global currentPage
    global bibleText
    currentPage = verseIndex 
    bibleText.delete("1.0", "end")
    bibleText.insert("1.0", Verses[currentPage])    

def changePages(Direction):
    global openPage
    global verseSelector

     
    if currentPage == 0:
        if ":" in openPage:
            openPage += "\t"
        else:
            openPage += ":1"

        for each in Verses:
            if openPage in each:
                first = Verses.index(each)    
                break

        if Verses[0] == Verses[first] and Direction == -1:
            pass
        elif Verses[-1] == Verses[first] and Direction == 1:
            pass
        else:
            showverse(first + Direction)
            
    else:
        if currentPage + Direction != -1 and currentPage + Direction != len(Verses) + 1:
            showverse(currentPage + Direction)
        
    
createInterface()
