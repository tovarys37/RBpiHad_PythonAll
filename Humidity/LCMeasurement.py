import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

file = open("SensorData.txt", "w") #stores data file in same directory as this program file
PinNumber = 17

#Define function to measure charge time
def RC_Analog(Pin):
    counter=0
    start_time = time.time()
    #Discharge capacitor
    GPIO.setup(PinNumber, GPIO.OUT)
    GPIO.output(PinNumber, GPIO.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    GPIO.setup(PinNumber, GPIO.IN)
#Count loops until voltage across capacitor reads high on GPIO
    while (GPIO.input(PinNumber)==GPIO.LOW):
        counter=counter+1
        #print(counter)
    end_time = time.time()
    return end_time - start_time


    #Main program loop
kolikrat = 0;
while (kolikrat<10):
    time.sleep(1)
    ts = time.time()
    reading = RC_Analog(4) #store counts in a variable
    counter = 0
    time_start = 0
    time_end = 0
    
    print(ts, reading)  #print counts using GPIO4 and time
    file.write(str(ts) + " " + str(reading) + "\n") #write data to file
    kolikrat += 1
    print(kolikrat)

    while (reading < 10.00):
        time_start = time.time()
        counter = counter + 1
        #print(counter, ' < main')
        if counter >= 50:
            break
    time_end = time.time()
    if (counter >= 25 and (time_end - time_start) <= 60): # if you get 25 measurements that indicate dry soil in less than one minute, need to water
        print('Not enough water!') #comment this out for testing
#    else:
 #     print('Your plants are safe and healthy, yay!')


GPIO.cleanup()
file.close()