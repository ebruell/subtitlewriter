#input in commandline linetime, names
#allow shorttime, longtime for questions
import sys

outF = open("myOutFile.txt", "w")
currseconds = 18 #are these global yet?? I remember there's weirdness about this... 
subtitlenum = 0


def writeline(text, linetime):
    global currseconds
    global subtitlenum
    tstart = timestamp(currseconds)
    currseconds += linetime
    tfinish = timestamp(currseconds)
    duration = tstart + " --> " + tfinish
    outF.write(str(subtitlenum))
    outF.write('\n')
    outF.write(duration)
    outF.write('\n')
    outF.write(text)
    outF.write('\n')
    outF.write('\n')
    
    subtitlenum += 1
    
    
def timestamp(linetype):
    timestamp = "0"
    global currseconds
    minutes =  currseconds//60
    hours = minutes//60
    hours = int(hours)
    minutes = minutes % 60
    minutes = int(minutes)
    seconds = currseconds % 60
    mseconds = (currseconds % 1) * 10
    mseconds = int(mseconds)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0" + str(minutes)
        
    if seconds < 10:
        seconds = "0" + str(seconds)
    timestamp = timestamp + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "," + str(mseconds) + "00"
    return timestamp
        
    
def main():
    global currseconds
    transcript = sys.argv[1]
    linetime = sys.argv[2]
    linetime = int(linetime)
    names = sys.argv[3]
    listnames = names.split(',') #will give error if I don't do anything?
    for name in listnames:
        name = name + ":"
    inputF = open(transcript, "r")
    transcriptWords = inputF.read().split()
    wordIndex = 0
    word = transcriptWords[wordIndex]
    while wordIndex < len(transcriptWords):
        word = transcriptWords[wordIndex]
        print("big while loop starting! at", word)
        currlinetime = linetime
        if word == "<longq>":
            print("found long q after word ", transcriptWords[wordIndex - 1])
            wordIndex += 1
            word = transcriptWords[wordIndex]
            if transcriptWords[wordIndex - 2] != "</longq>":
                currseconds += 1
            question = ""
            tempWordIndex = wordIndex
            
            while word != "</longq>":
                print("lq: ", word)
                question = question + " " + word
                wordIndex += 1
                if wordIndex >= len(transcriptWords):
                    print("error: missing lonq closer after word ", transcriptWords[tempWordIndex + 1])
                    exit()
                word = transcriptWords[wordIndex]
            wordIndex += 1
                
                
                
                
            writeline(question, 13)
            currseconds += 0.5
        elif word == "<shortq>":
            print("found shortq after word ", transcriptWords[wordIndex - 1])
            currseconds += 1
            question = ""
            wordIndex += 1
            word = transcriptWords[wordIndex]
            tempWordIndex = wordIndex
            while word != "</shortq>":
                print("q: ", word)
                question = question + " " + word
                wordIndex += 1
                if wordIndex >= len(transcriptWords):
                    print("error: missing shortq closer after word ", transcriptWords[tempWordIndex + 1])
                    exit()
                word = transcriptWords[wordIndex]
            writeline(question, 4)
            wordIndex += 1
        elif word == "</shortq>":
            print("error: encountered shortq closer without open")
            exit()
        elif word == "</longq>":
            print("error: encountered longq closer without open")
            exit()
        else:
            wordCount = 0
            currline = ""
            caughtq = False
            while wordCount < 16 and not caughtq:
                if wordIndex >= len(transcriptWords):
                    currlinetime = (wordCount // 2) + 1
                    break
                word = transcriptWords[wordIndex]
              
                if word in listnames:
                    currline = currline + "\n"
                
                
                
                if word == "<longq>" or word == "<shortq>":
                    currlinetime = (wordCount // 2) + 1
                    caughtq = True
                else:
                    currline = currline + " " + word
                    print(word)
                    wordIndex += 1
                    wordCount += 1
            writeline(currline, currlinetime)
            
                    

        
main()
        
    