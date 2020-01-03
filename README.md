# SimpleLoggingServerToCsvFile

This server logs event to a specified CSV file based on Python's default "http.server" class.

To start the server with Python 3:

<b>python SimpleLoggingServerToCsvFile.py 8080 </b>

There is a configuration section in this script allowing to adjust:

<table>
<tr><th>Parameter</th><th>Description</th><th>Default value</th?</tr>
<tr><td>LOG_FILE</td><td>Name of the CSV file for storing the events</td><td>events.log</td></tr>
<tr><td>KEYS</td><td>Set of keys that are allowed to be logged</td><td>q67idhrJ56oQj7IElukH</td></tr>
<tr><td>MASTER_KEY</td><td>Key that restarts the logging</td><td>jQw5xZVq9Kp4fm7hiZko</td></tr>
</table>


Note that keys is just an identifer. Not a cryptographic key, just random sequence of numbers and letters. <br><br>

<b>Statistics by hour</b><br>
======
The <b>charthour.html</b> shows event statistics by hour of the day in a form or clock spider plot.

<b>Getting started</b><br>
======
<ol>
<li>Start the SimpleLoggingServerToCsvFile server using Python</li>
<li>Access the key to log an event:
*http://localhost:8080/jQw5xZVq9Kp4fm7hiZko*
</li>
<li>Access the master key to reset the logger:
<div class="text-purple">http://localhost:8080/q67idhrJ56oQj7IElukH</div></li>
<li>To view the spider plot:
<div class="text-purple">http://localhost:8080/charthour.html</div></li>
</ol>
 :+1: