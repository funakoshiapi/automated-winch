import RPi.GPIO as GPIO
import ms5837
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def stop():
    
    #GPIO.cleanup
    
    GPIO.setup(35,GPIO.OUT)
    GPIO.output(35,GPIO.HIGH)

    GPIO.setup(33,GPIO.OUT)
    GPIO.output(33,GPIO.HIGH)
    
    GPIO.setup(40,GPIO.OUT)
    GPIO.output(40,GPIO.HIGH)

    GPIO.setup(37,GPIO.OUT)
    GPIO.output(37,GPIO.HIGH)
    
    GPIO.cleanup
    
stop()


# Set up GPIO pins 40 and 37 to LOW
# activating the winch to rotate counter clockwise 

def move_up():
    stop()
    GPIO.cleanup
    GPIO.setup(40,GPIO.OUT)
    GPIO.output(40,GPIO.LOW)

    GPIO.setup(37,GPIO.OUT)
    GPIO.output(37,GPIO.LOW)
   
    GPIO.cleanup
    
# Set up GPIO pins 35 and 33 to HIGH
# activating the winch to rotate counter clockwise   
  
def move_down():
    stop()
    GPIO.cleanup
    GPIO.setup(35,GPIO.OUT)
    GPIO.output(35,GPIO.LOW)

    GPIO.setup(33,GPIO.OUT)
    GPIO.output(33,GPIO.LOW)
    
    
    GPIO.cleanup
    
 # Set every pin to HIGH in order to turn
 # the winch off
        

    
 # Function in charge of the Depeth
 # Will ask the user for insert a desired depth
 # therefore activating the winch to move up or down in order to 
 # reach the depth prompted by the user.   
 
def depth_sensor(value=0.0): 
    
    flag = True # this flag is being used in order to signal the very first value read by the sensor
    first_depth_read = 0.0 # initialize the first_temp_read to float 
    
    """print("Input the desired depth")   # CHANGE TO DEPTH LATER"""
    """value = float(raw_input("> "))  # Desired depth to be reached"""
    
    
    
    # We must initialize the sensor before reading it
    if not sensor.init():
        print ("Sensor could not be initialized")
        exit(1)
        
    # We have to read values from sensor to update depth   
    if not sensor.read():
        print ("Sensor read failed!")
        exit(1)
        
    if sensor.read():   # statr sensor reading
        if flag == True :  # flag helps to only store the first sensor read
                first_depth_read = sensor.depth()
                print("first_read:", first_depth_read*39.3701, "inches")
                flag = False # makes that this if statement is only true once
        # Print readings
        print("Depth: %.3f inches (freshwater)") % (
                sensor.depth()*39.3701  )
        if sensor.depth()*39.3701 < value:  # is depth from the sensor less then the target depth prompted by the user?
            while True:
                move_down() # activates winch to move down 
                time.sleep(0.2) # time period the winch is activated, WILL NEED TO TEST HOW MUCH CABLE IS RELEASED IN ONE ROTATION OF THE WINCH / HOW MANY SECONDS FOR ONE ROTATION
                #stop() # force the winch to stop rotating
                if sensor.depth()*39.3701 >=  value : # when similar depth is reach, break from the loop. Later depth can be adjusted by using calculations
                    loop_flag = False
                    stop()
                    break
        elif sensor.depth()*39.3701 >  value:  # is depth from the sensor is greater then the target depth prompted by the user?
            while True:
                move_up() # activates winch to move up
                time.sleep(0.2) # time period the winch is activated, WILL NEED TO TEST HOW MUCH CABLE IS RELEASED IN ONE ROTATION OF THE WINCH / HOW MANY SECONDS FOR ONE ROTATION
                #stop() # force the winch to stop rotating
                if sensor.depth()*39.3701 <=  value : # when similar depth is reach, break from the loop. Later depth can be adjusted by using calculations
                    loop_flag = False
                    stop()
                    break
    else:
        print ("Sensor read failed!")

def presentation():

    move_down()
    time.sleep(0.1)
    move_up()
    time.down(0.1)                                      
    stop()

    
sensor = ms5837.MS5837_30BA() # Default I2C bus is 1 (Raspberry Pi 3)
    
func_dict = {'up':move_up, 'down':move_down, 'stop':stop, 'depth':depth_sensor, 'present':presentation}
    
if __name__ == "__main__":
    
    
    print("\nInput desired command: \n")
    
    print("up -> to move up the winch")
    print("\n")
    print("down -> to move down the winch")
    print("\n")
    print( "stop -> to force to stop" )
    print("\n")
    print( "depth -> to seat winch at desired depth" )
    print("\n")
    print("exit -> exit winch control")
    print("\n")
    
    command = raw_input(">>> ")

    while command != 'exit':
        try:
            control = ['up','down','stop', 'depth','present']

            if command in control:
                func_dict[command]()
            else:
                print("wrong input")
                print("\n")
            command = raw_input(">>> ")
            if command == 'exit':
                stop()
        except KeyboardInterrupt:
            stop()
            command = 'exit'

    print("\n")
    print("terminated")
            






    








