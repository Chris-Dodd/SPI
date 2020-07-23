
# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
# import time

# Import SPI library (for hardware SPI) and MCP3008 library.
# import Adafruit_GPIO.SPI as SPI
# import Adafruit_MCP3008
# import sys                      # Import sys module
# from time import sleep          # Import sleep from time
# import Adafruit_GPIO.SPI as SPI # Import Adafruit GPIO_SPI Module
# import Adafruit_MCP3008         # Import Adafruit_MCP3008
# import time
# import datetime
# from firebase import firebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
#   'https://plantmonitor-723b4.firebaseio.com/': project_id,
#   'projectId': 'plantmonitor-723b4',
  'projectId': project_id,
#   'projectId': https://plantmonitor-723b4.firebaseio.com/
})

db = firestore.client()

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})



# # firebase = firebase.FirebaseApplication('plantmonitor-723b4',None)
# # firebase.put('plantmonitor-723b4', 'Please Work', 'please the lord')

# # Software SPI configuration:
# CLK  = 18
# MISO = 23
# MOSI = 24
# CS   = 25
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# # Hardware SPI configuration:
# #SPI_PORT   = 0
# #SPI_DEVICE = 0
# #mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# print('Reading MCP3008 values, press Ctrl-C to quit...')
# # Print nice channel column headers.
# print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
# print('-' * 57)
# # Main program loop.
# while True:
#     # Read all the ADC channel values in a list.
#     values = [0]*8
#     for i in range(8):
#         # The read_adc function will get the value of the specified channel (0-7).
#         values[i] = mcp.read_adc(i)
#         if(i==3): #Put capacitive water sensor into ADC port 3
#             firebase.put('plantmonitor-723b4', 'Capactive moisture', str(values[i]))

#         if (i==7): #ie port 7
#             firebase.put('plantmonitor-723b4', 'Beers Jugged', str(values[i]))


#     # Print the ADC values.
#     print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
#     # Pause for half a second.
#     time.sleep(0.5)
