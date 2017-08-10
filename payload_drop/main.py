
#####################################################
# Project: Payload Drop								#
# Created by: William Gregory						#
# Description: ArduPlane targeted payload drop		#
# Last Modified Date: August 24th 2017				#
# Version: 1.0										#
#####################################################

# Import
#-------------------------------------------------------------

import math
import clr
import time
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities")
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink")
import MAVLink

# Variables
#-------------------------------------------------------------

## Settings
# target
target_lat = 39.40456			# lat of target
target_lon = -119.761292		# lon of target
# general
real_drop = True				# real or dummy drop
target_waypoint = 6				# waypoint to perform drop
countdown_range = 50			# countdown range in addition to release_distance
release_pin = 7					# physical drop device pin number

## State Variables
# general
mode = 0						# current mode 0: idle, 1:run, 2:done, 3:aborted
target_location = [] 			# lat, lon of target
drop_location = []				# lat, lon of determined drop location
# current flight data
ct_a = 0.0 						# altitude
ct_gs = 0.0 					# groundspeed
ct_gc = 0.0						# ground course
ct_d = 0.0 						# distance to waypoint
ct_w = 0						# waypoint number
ct_ws = 0.0						# wind velocity
ct_wd = 0.0						# wind direciton

# General Funcitons
#-------------------------------------------------------------

# get updated flight data
def getFlightData():
	global ct_t, ct_d, ct_a, ct_gs, ct_gc, ct_w, ct_wd, ct_ws
	ct_t = time.time()
	ct_d = cs.wp_dist
	ct_a = cs.alt
	ct_gs = cs.groundspeed
	ct_gc = cs.groundcourse
	ct_w = cs.wpno
	ct_wd = cs.wind_dir
	ct_ws = cs.wind_vel

# print flight data
def printFlightData():
	print("info: flight data")
	print("- altitude: " + str(ct_a))
	print("- distance: " + str(ct_d))
	print("- groundspeed: " + str(ct_gs))
	print("- groundcourse: " + str(ct_gc))
	print("- waypoint: " + str(ct_w))
	print("- wind direction: " + str(ct_wd))
	print("- wind speed: " + str(ct_ws))

# release the payload
def dropPayload():
	if mode == 1:
		if real_drop:
			Script.SendRC(release_pin, 953, True)
		print ("noteice: payload released")
		if real_drop:
			Script.Sleep(5000)
			Script.SendRC(release_pin, 2028, True)
		Script.ChangeMode("AUTO")
		#Script.ChangeMode('RTL')
		return True
	return False

# Autostart
#-------------------------------------------------------------

def autostart():
	print("payload drop script - online")
	# test drop
	dropPayload();
	# test data
	getFlightData();
	printFlightData();
	print("payload drop script - offline")

## --
autostart();