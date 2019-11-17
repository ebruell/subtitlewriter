
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
    timelist = timestring.split(':')
    seconds = float(timelist[-1])
    minutes = int(timelist[-2])
    hours = 0
    if len(timelist) == 3:
        hours = int(timelist[0])
    if len(timelist) > 3:
        print("Error: could not read time tag ", timestring)   
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
    mseconds = (seconds % 1) * 1000
    mseconds = round(mseconds)
    if mseconds < 10:
        mseconds = "00" + str(mseconds)
    elif mseconds < 100:
        mseconds = "0" + str(mseconds)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0" + str(minutes)
        
    if seconds < 10:
        seconds = "0" + str(seconds)
    timestamp = timestamp + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "," + str(mseconds)
    return timestamp
        
    
def calculateLineTime(numwords, start, finish):
    sectiontime = finish - start
    numsections = numwords/12
    linetime = sectiontime / numsections
    roundlinetime = round(linetime*1000)/1000
    return roundlinetime
    

def writeSection(sectionList, tstart, tfinish):
    numwords = len(sectionList)
    start = secondscalc(tstart)
    finish = secondscalc(tfinish)
    linetime = calculateLineTime(numwords, start, finish)
    wordIndex = 0
    linetext = ""
    wordCount = 0
    while wordIndex < numwords:
        word = sectionList[wordIndex]
        if wordCount < 11 and wordIndex < len(sectionList) - 1:
            linetext = linetext + " " + word 
            wordIndex += 1
            wordCount += 1
        else: 
            endtime = start + linetime 
            if endtime > finish:
                endtime = finish
            linetext = linetext + " " + word 
            writeLine(linetext, start, endtime)
            start = endtime
            linetext = ""
            wordIndex += 1
            wordCount = 0
            
            
    
def main():
    transcript = sys.argv[1]
    inputF = open(transcript, "r")
    transcriptWords = inputF.read().split()
    wordIndex = 0
    word = transcriptWords[wordIndex]
    if word[1] == '<':
        word = word[1:]
    tstart = word.strip('<>')
    print("tstart is: ", tstart)
    while wordIndex + 1 < len(transcriptWords):
        wordIndex += 1
        word = transcriptWords[wordIndex]
        sectionList = []
        while word[0] != "<":
            sectionList.append(word)
            wordIndex += 1
            word = transcriptWords[wordIndex]
        tfinish = word.strip("<").strip(">")
        writeSection(sectionList, tstart, tfinish)
        tstart = tfinish
        
            

                
                    

        
main()
        
    