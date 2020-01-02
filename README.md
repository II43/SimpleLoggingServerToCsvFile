# SimpleLoggingServerToCsvFile

This server logs event to a specified CSV file based on Python's default "http.server" class.

To start the server with Python 3:

<b>python SimpleLoggingServerToCsvFile.py 8080 </b>

There is a configuration section in this script allowing to adjust:

LOG_FILE:   Name of the CSV file for storing the events <br>
KEYS:       Set of keys that are allowed to be logged <br>
MASTER_KEY: Key that restart the logging <br>

Note that keys is just a identifer. Not a cryptographic key, just random sequence of numbers and letters. 


Statistics by hour
The <b>charthour.html</b>shows event statistics by hour of the day in a form or clock spider plot.

Examples