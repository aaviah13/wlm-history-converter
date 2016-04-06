# David Hsu Copyright 2015
# Simple XML converter to human readable text, specifically for
# Windows Live Messenger history XML files.

################################################################################
#
#     Function name: convertWindowsLiveMessengerHistoryXML
#
#     This function converts a Windows Live Messenger history XML file. It
#     searches for specific XML keywords and parses the content.
#
#     Sample XML message:
#   <Message Date="9/9/2009" Time="12:21:45 AM" DateTime="2009-09-09T07:21:45.871Z" SessionID="1">
#      <From>
#         <User FriendlyName="Dav!dHsu"/>
#      </From>
#      <To>
#         <User FriendlyName="Tiffany*red+u"/>
#      </To>
#      <Text Style="font-family:Segoe UI; color:#000000; ">hey</Text>
#   </Message>
#
#     Sample output:
#        (9/9/2009 12:21:45 AM) Dav!dHsu: hey
#
#     Inputs:
#        historyFile                - full file path to XML history file
#
#     Outputs:
#        history.txt                - converted text file of XML history file,
#                                     stored in the working directory
#
################################################################################
def convertWindowsLiveMessengerHistoryXML(historyFile) :

   if historyFile == "":
      print "No filepath specified!"
      return

   convertedFileName = "history.txt"

   # Open history XML
   openedFile = open(historyFile, 'r')

   # Open output file
   openedConvertedFile = open(convertedFileName, 'w')

   messageBeginString  = "<Message"
   messageEndString    = "</Message>"
   dateBeginString     = "Date="
   timeBeginString     = "Time="
   fromBeginString     = "<From>"
   fromEndString       = "</From>"
   usernameBeginString = "FriendlyName="
   textBeginString     = "<Text"
   textEndString       = "</Text>"

   # For each line in the history file:
   for line in openedFile :

      # We'll keep track of where we are in the current line
      lineIndex = 0

      # While we didn't reach the end of the line yet:
      while lineIndex < len(line) :

         # Find where message starts and ends
         messageStartIndex = line.find(messageBeginString, lineIndex)
         messageEndIndex   = line.find(messageEndString, lineIndex)

         # Go to the next line if no more messages:
         if messageStartIndex == -1 or messageEndIndex == -1 :
            break

         else :

            # Get message date
            dateStartTagIndex = line.find(dateBeginString, messageStartIndex, messageEndIndex+1)
            if dateStartTagIndex != -1 :
               dateStartIndex = line.find("\"", dateStartTagIndex)
               dateEndIndex   = line.find("\"", dateStartIndex+1)
               date = line[dateStartIndex+1:dateEndIndex]
            else :
               date = "DATE:N/A"

            # Get message time
            timeStartTagIndex = line.find(timeBeginString, messageStartIndex, messageEndIndex+1)
            if timeStartTagIndex != -1 :
               timeStartIndex = line.find("\"", timeStartTagIndex)
               timeEndIndex   = line.find("\"", timeStartIndex+1)
               time = line[timeStartIndex+1:timeEndIndex]
            else :
               time = "TIME:N/A"

            # Get from username
            fromTagBeginIndex = line.find(fromBeginString, messageStartIndex, messageEndIndex+1)
            if fromTagBeginIndex != -1 :
               fromTagEndIndex  = line.find(fromEndString, fromTagBeginIndex, messageEndIndex+1)
               usernameTagIndex = line.find(usernameBeginString, fromTagBeginIndex, fromTagEndIndex)
               if usernameTagIndex != -1 :
                  usernameStartIndex = line.find("\"", usernameTagIndex)
                  usernameEndIndex   = line.find("\"", usernameStartIndex+1)
                  username = line[usernameStartIndex+1:usernameEndIndex]
               else :
                  username = "USERNAME:N/A"
            else :
               username = "USERNAME:N/A"

            # Get message content
            textStartTagIndex = line.find(textBeginString, messageStartIndex, messageEndIndex+1)
            if textStartTagIndex != -1 :
               textEndTagIndex = line.find(textEndString, textStartTagIndex, messageEndIndex+1)
               textBeginIndex  = line.find(">", textStartTagIndex, textEndTagIndex)
               text = line[textBeginIndex+1:textEndTagIndex]
            else :
               text = "TEXT:N/A"

            # Print to output file
            outputString = "(" + date + " " + time + ") " + username + ": " + text + "\n"
            print outputString
            openedConvertedFile.write(outputString)

            lineIndex = messageEndIndex + len(messageEndString) - 1

   # Close files
   openedFile.close()
   openedConvertedFile.close()

   print "done"

# Call function
convertWindowsLiveMessengerHistoryXML("")

