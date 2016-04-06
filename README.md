# wlm-history-converter

This function converts a Windows Live Messenger history XML file to a human-readable text file. It searches for specific XML keywords and parses the content.

Sample XML message:

    <Message Date="9/9/2009" Time="12:21:45 AM" DateTime="2009-09-09T07:21:45.871Z" SessionID="1">
      <From>
        <User FriendlyName="Dav!dHsu"/>
      </From>
      <To>
        <User FriendlyName="Tiffany*red+u"/>
      </To>
      <Text Style="font-family:Segoe UI; color:#000000; ">hey</Text>
    </Message>

Sample output:

    (9/9/2009 12:21:45 AM) Dav!dHsu: hey

# Usage
Python source code provided. To use, call the function `convertWindowsLiveMessengerHistoryXML` with the full file path of the Windows Live Messenger XML history file and compile. A `history.txt` file will be generated for the input history file in the calling directory. 

Note: The function `convertWindowsLiveMessengerHistoryXML` will overwrite any existing `history.txt` file.
