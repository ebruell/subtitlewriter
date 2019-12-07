# subtitlewriter

This program uses 'time tags' to build an srt file from a transcript. Time tags must be in form <hr:min:sec> or <min:sec>, where hr = number of hours, etc, and there must be a space or newline before and after each timetag. ("<0:00>Welcome" will NOT be properly read as a time tag, nor will "end.<1:02:04.6>"). 

The program will write any text between two timetags into subtitles of 12 words each, so that the first subtitle begins at the first time tag's time, and the last subtitle ends at the last time tag's time. The duration of each subtitle will be determined by the total time between the time tags divided by the number of 12-word subtitles needed. So, time tags MUST be placed at the beginning and end of the file. For more accurate synchronization with the audio, input more time tags. 

Ex: <0:00> This is a test <0:10> And this is a test that will be split into two subtitles because the number of words in this sentence is 29 and each subtitle only has 16 words <0:30> 

returns this srt:

0

00:00:00,000 --> 00:00:10,000
 
 This is a test

1

00:00:10,000 --> 00:00:18,276
 
 And this is a test that will be split into three subtitles

2

00:00:18,276 --> 00:00:26,552
 
 because the number of words in this sentence is 29 and each

3

00:00:26,552 --> 00:00:30,000
 
 subtitle only has 12 words

Note that time is split proportionally between subtitles, so the last subtitle, which only has five words, is given 3.448 seconds while the others receive 8.276. 

To run this program, download your time-tagged transcription and ensure that it is in the same directory as this program, then enter the transcription document's name after the program name in commandline. (ex: python3 writesubtitles.py myInputFile.txt) * Note that transcription document's title must be one word. *

The program will write to a file called myOutFile.txt. You can then upload that file to youtube, or use it in any other setting where srt files are used (though some may require the extension to be changed from 'txt' to 'srt') 

This model works particularly well for videos in an interview format because one can just timetag the beginning and end of each question being asked (as well as the last second of the final response). If using this in conjunction with oTranscribe, use command-J frequently while transcribing to automatically insert timestamps, then go through the document after transcription and change each timestamp to a time tag by changing the surrounding parenthesis to <>.
