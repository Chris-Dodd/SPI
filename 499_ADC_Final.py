#499 Project ADC Code

'''
Code to take ADC values from MCP3008 chip and send to firebase. THIS MUST be
ran in the same folder as the firebase JSON ServiceAccountKey
'''


import sys                      # Import sys module
from time import sleep          # Import sleep from time
import Adafruit_GPIO.SPI as SPI # Import Adafruit GPIO_SPI Module
import Adafruit_MCP3008         # Import Adafruit_MCP3008
import time                     # Import Time
import datetime                 #Import datetime
import firebase_admin           #Import Firebase/firestore
import google.cloud             #Import Google cloud
from firebase_admin import credentials, firestore        #Import Firebase

'''
First we use our unique ServiceAccountKey downloaded from our database.
This Json file must be saved in the working directory of the script in
order to read/write/access the firestore database.
Then the firestore is initialized.
'''


cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()

'''
In Firestore the collection is initialized for each plant. This can be
easily scaled up with the format:
doc_ref[i] = store.collection(u'plant_data').document('plant[i]')
'''
doc_ref0 = store.collection(u'plant_data').document('plant_0')
doc_ref1 = store.collection(u'plant_data').document('plant_1')


'''
Checking if there is data, if there is format to dictionary, if not throw
an exception
'''

#try:
    #docs = doc_ref.get()
    #print(u'Doc Data:{}'.format(docs.to_dict()))
#except google.cloud.exceptions.NotFound:
    #print(u'Missing data')

'''
At this point the Firestore is configured and ready to accept data for the
docs we have initialized (ie plant_0 and plant_1} at this time
'''
#/////////////////////////////////////////////////////////////////////////
# * Now we will initialize the ADC circuit*
#/////////////////////////////////////////////////////////////////////////

'''
For software SPI, CLK, MISO, MOSI, and CS are set to general GPIO pins.
Currently they are configured at 18,23,24, and 25 as below for localization
and cleaner wiring
Then the MCP chip is initialized from the Adafruit library
'''
# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

'''
Currently Hardware SPI is commented out as the GPIO pins are being used
'''
# Hardware SPI configuration:
# #SPI_PORT   = 0
# #SPI_DEVICE = 0
# #mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


#/////////////////////////////////////////////////////////////////////////
# * Now we will read the values and send values to firestore*
#/////////////////////////////////////////////////////////////////////////


'''
Starting with a print statement to give column headers for pins 0 to 7 then
the values are read into the ADC, assigned a variable and send to firestore
Here is where it can be customized depending on the readings. Assume there are
4 different readings we would like for 2 plants:
we would like to read: Temperature, Moisture, PH, and EC for each plant. To
accomplish this, we will wire:
for plant_0:
Temperature(plant_0) - pin0 on MCP3008
Moisture(plant_0)    - pin1 on MCP3008
PH(plant_0)          - pin2 on MCP3008
EC(plant_0)          - pin3 on MCP3008
for plant_1:
Temperature(plant_1) - pin4 on MCP3008
Moisture(plant_1)    - pin5 on MCP3008
PH(plant_1)          - pin6 on MCP3008
EC(plant_1)          - pin7 on MCP3008
Remember that doc_ref0 = plant0, doc_ref1 = plant1 and so on.
'''
print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)

'''
The following While loop is what reads the values and prints it to Firebase.
It is a constant while loop that creates an array called 'values' which stores
the sensor value at each pin on the MCP3008 ADC.
Then a for loop goes through the values array and sends the appropriate pin
value with a corresponding label to the correct plant in firebase
'''

while True:
    # Read all the ADC channel values in a list.
     values = [0]*8
     for i in range(8):
         # The read_adc function will get the value of the specified channel (0-7).
         values[i] = mcp.read_adc(i)
         print(values)
         if(i==0): #Temperature for plant0
            #For the temperature sensor range is from 0 - 100 degrees Celsius
            #Will scale using: T = (Tmax - Tmin) * Tread / 1023), for 10 bit read_adc
            vt0 = values[i] *((100)/1023)
            print(values[i])
            print(vt0)
            doc_ref0.set({u'humidity': vt0})
            print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
            # Pause for half a second.
            time.sleep(2)
            '''
        if(i==1): #Moisture for plant0
         #The Moisture sensor range is from 0 - 100
         #Will scale using: M = (Mmax - Mmin) * Mread / 1023), for 10 bit read_adc
            vt1 = values[i] *[(100)/1023]
            doc_ref0.set({u'humidiy: vt1})

         if(i==2): #PH for plant0]
            vt2 = values[i] * [14/1023]
            doc_ref0.set({u'PH': vt2})
         if(i==3): #EC for plant0
            vt3 = values[i] *[(100)/1023]
            doc_ref0.set({u'EC': vt3})
         if(i==4): #Temperature for plant1
            vt4 = values[i] *[(100)/1023]
            doc_ref1.set({u'Temperature': vt4})
         if(i==5): #Moisture for plant1
            vt5 = values[i] *[(100)/1023]
            doc_ref1.set({u'Moisture': vt5})
         if(i==6): #PH for plant1
            vt6 = values[i] *[(14)/1023]
            doc_ref1.set({u'PH': vt6})
         if(i==7): #EC for plant1
            vt7 = values[i] *[(100)/1023]
            doc_ref1.set({u'EC': vt7})
            '''
