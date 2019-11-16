#input in commandline linetime, names
#allow shorttime, longtime for questions
import sys

outF = open("myOutFile.txt", "w")
subtitlenum = 0


def writeLine(text, tstart, tfinish):
    global subtitlenum
    tstart = timestamp(tstart)
    tfinish = timestamp(tfinish)
    duration = tstart + " --> " + tfinish
    outF.write(str(subtitlenum))
    outF.write('\n')
    outF.write(duration)
    outF.write('\n')
    outF.write(text)
    outF.write('\n')
    outF.write('\n')
    
    subtitlenum += 1
    
    
def secondscalc(timestring):
    seconds = int(timestring[-2:])
    if len(timestring) == 4:
        minutes = int(timestring[0])
    else:
        minutes = int(timestring[-5:-3])
    hours = 0
    if len(timestring) > 5:
        hours = 1    
    numseconds = seconds + (minutes*60) + (hours * 3600)
    return numseconds

def timestamp(numseconds):
    timestamp = "0"
    minutes =  numseconds//60
    hours = minutes//60
    hours = int(hours)
    minutes = minutes % 60
    minutes = int(minutes)
    seconds = numseconds % 60
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0" + str(minutes)
        
    if seconds < 10:
        seconds = "0" + str(seconds)
    timestamp = timestamp + str(hours) + ":" + str(minutes) + ":" + str(seconds) + ",000"
    return timestamp
        
    
def writeSection(sectionList, tstart, tfinish):
    numwords = len(sectionList)
    start = secondscalc(tstart)
    finish = secondscalc(tfinish)
    sectiontime = finish - start
    linetime = 12 * sectiontime // numwords
    wordIndex = 0
    linetext = ""
    wordCount = 0
    while wordIndex < len(sectionList) - 1:
        word = sectionList[wordIndex]
        if wordCount < 12 and wordIndex < len(sectionList) - 1:
            linetext = linetext + " " + word 
            wordIndex += 1
            wordCount += 1
        else: 
            endtime = start + linetime 
            if endtime > finish:
                endtime = finish
            writeLine(linetext, start, endtime)
            start = endtime
            linetext = ""
            wordCount = 0
            
            
    
def main():
    transcript = sys.argv[1]
    names = sys.argv[2]
    listnames = names.split(',') #will give error if I don't do anything?
    for name in listnames:
        name = name + ":"
    inputF = open(transcript, "r")
    transcriptWords = inputF.read().split()
    wordIndex = 0
    word = transcriptWords[wordIndex]
    tstart = word.strip("<").strip(">")
    while wordIndex + 1 < len(transcriptWords):
        print(word)
        wordIndex += 1
        word = transcriptWords[wordIndex]
        sectionList = []
        while word[0] != "<":
            if word in listnames:
                word = "\n" + word
            sectionList.append(word)
            wordIndex += 1
            word = transcriptWords[wordIndex]
        tfinish = word.strip("<").strip(">")
        writeSection(sectionList, tstart, tfinish)
        tstart = tfinish
        
            

                
                    

        
main()
        
    