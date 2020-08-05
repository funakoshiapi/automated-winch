from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#-- Connect to the vehicle
import argparse
parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()

connection_string = args.connect


print("Connection to the vehicle on %s"%connection_string)
vehicle = connect(connection_string, wait_ready=True)

#-- Define the function for takeoff
def arm_and_takeoff(tgt_altitude):
    print("Arming motors")
    
    while not vehicle.is_armable:
        time.sleep(0.5)
        
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    while not vehicle.armed: time.sleep(1)
    
    print("Takeoff")
    vehicle.simple_takeoff(tgt_altitude)
    
    #-- wait to reach the target altitude
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        
        if altitude >= tgt_altitude -1:
            print("Altitude reached")
            break
            
        time.sleep(1)
        
#-- define function to move the drone     
def move_drone():
    #-- show current location
            print("Current Latitude: ", vehicle.location.global_relative_frame.lat)
            print("Current Longitude: ", vehicle.location.global_relative_frame.lon)
            #-- select new location
            lat = input("New Latitude: ")
            lon = input("New Longtitude: ")
            #-- set the default speed
            vehicle.airspeed = input("Select Speed: ")
            #-- go to new location
            print ("Going to new location")
            wp1 = LocationGlobalRelative(lat, lon, 10)
            vehicle.simple_goto(wp1)
            moving = True
            #-- notify when arrived at new location
            while moving:
                if lat - .000005 < vehicle.location.global_relative_frame.lat < lat + .000005 and \
                lon - .000005 < vehicle.location.global_relative_frame.lon < lon + .000005:
                    print("Arrived")
                    moving = False

#------ MAIN PROGRAM ----
arm_and_takeoff(10)

home_lat = vehicle.location.global_relative_frame.lat
home_lon = vehicle.location.global_relative_frame.lon

active = True
winch = False

while active:
    option = raw_input("Select an Option:\nMove, Winch, or Land: ")

    if option == "Move":
        if winch == False:
            move_drone()
        else:
            print("Cannot move while winch is deployed")
    elif option == "Winch":
        if winch == False:
            print("Deploying Winch")
            time.sleep(3)
            print("Winch Deployed")
            winch = True
        else:
            print("Returning Winch")
            time.sleep(3)
            print("Winch Returned")
            winch = False
    elif option == "Land":
        if winch == False:
            active = False
        else:
            print("Cannot land while winch is deployed")
    else:
        print("Invalid Option, Try Again")


#--- Coming back
print("Coming back to land")
vehicle.mode = VehicleMode("RTL")
homing = True
#-- notify when arrived at home location
while homing:
    if home_lat - .000005 < vehicle.location.global_relative_frame.lat < home_lat + .000005 and \
    home_lon - .000005 < vehicle.location.global_relative_frame.lon < home_lon + .000005:
        print("Landing")
        homing = False
#-- notify when landed
landing = True
while landing:
    if vehicle.location.global_relative_frame.alt < 1:
        print("Landed")
        landing = False

time.sleep(5)

#-- Close connection
vehicle.close()