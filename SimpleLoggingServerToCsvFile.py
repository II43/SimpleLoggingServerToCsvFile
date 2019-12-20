#!/usr/bin/env python3
"""
Simple HTTP server in Python for logging events to CSV file
Motivation: Use this CSV file later for data agregation and plotting

Inspired by: Very simple HTTP server in Python for logging requests
https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7

Usage::
    ./SimpleLoggingServerToCsvFile.py [<port>]
"""

#----------------------------------------------------------------------#
# Import                                                               #
#----------------------------------------------------------------------#

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

from datetime import datetime

import csv

from os import curdir, sep, path


#----------------------------------------------------------------------#
# Configuration                                                        #
#----------------------------------------------------------------------#

# Log file
LOG_FILE = r'events.log'

# Master key
MASTER_KEY = "jQw5xZVq9Kp4fm7hiZko"

# All the allowed keys
KEYS = ["q67idhrJ56oQj7IElukH", 
        MASTER_KEY]

#----------------------------------------------------------------------#
# Classes                                                              #
#----------------------------------------------------------------------#
      
class S(BaseHTTPRequestHandler):
    def prepare_for_html_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # datetime object containing current date and time
        now = datetime.now()
        print("now =", now)
        # dd/mm/YY H:M:S
        time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", time_stamp)
        
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self.prepare_for_html_response()
        #self.wfile.write("<html><head><title>Title goes here.</title></head>")
        #self.wfile.write("<body><p>This is a test.</p>")
        #self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        #self.wfile.write("</body></html>")
        
        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        
        # Return HTML,CSV or LOG file if requested
        if self.path.endswith(".html") or self.path.endswith(".csv") or self.path.endswith(".log") or \
           self.path.endswith(".js") or self.path.endswith(".css"):
            f_path = curdir + sep + self.path
            if not path.exists(f_path):
                # Requested file doesn't exists
                self.wfile.write("Request file does not exist!".encode('utf-8'))
            else:
                #Open the static HTML file requested and send it
                f = open(f_path,'rb') 
                self.wfile.write(f.read())
                f.close()
            # Nothing more to do    
            return;
        
        # Otherwise try to log the event for given key   
        received_key = str(self.path)[1:]
        isKeyValid = False
        
        for key in KEYS:
            if key == received_key:
                self.wfile.write("Valid key! Logging event to a output file!".encode('utf-8'))
                isKeyValid = True
                # If master key is received, logger file is replaced with new one
                if received_key == MASTER_KEY:
                    method_to_log = 'w'
                else:
                    method_to_log = 'a'
                
                # Logging an event to CSV
                with open(LOG_FILE, method_to_log, newline='\n') as f:
                    writer = csv.writer(f)
                    if method_to_log == 'w':
                        writer.writerow(["Timestamp", "Key"])
                    writer.writerow([time_stamp, received_key])
                       
        if not isKeyValid:
            # No valid key had been received
            self.wfile.write("Unknown key! Nothing to do!".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self.prepare_for_html_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

#----------------------------------------------------------------------#
# Functions                                                            #
#----------------------------------------------------------------------#


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

#----------------------------------------------------------------------#
# Main                                                                 #
#----------------------------------------------------------------------#

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()