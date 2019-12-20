# SimpleLoggingServerToCsvFile

This server logs event to a specified CSV file. 

To start the server with Python 3:

python SimpleLoggingServerToCsvFile.py 8080

There is a configuration section in this script allowing to adjust:

LOG_FILE:   Name of the CSV file for storing the events
KEYS:       Set of keys that are allowed to be logged
MASTER_KEY: Key that restart the logging

Note that keys is just a identifer. Not a cryptographic key, just random sequence of numbers and letters. 



