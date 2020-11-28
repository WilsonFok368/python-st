import win32com.client
import argparse

parser = argparse.ArgumentParser(description='RF Switch Control')
parser.add_argument('port', type=int, default=8, choices=range(1, 9), 
					help="Sets COM to port specified.")
args = parser.parse_args()

try:
	foo = None
	win32com.client.gencache.EnsureDispatch('MCL_SolidStateSwitch.USB_Control')
	switch = win32com.client.Dispatch("MCL_SolidStateSwitch.USB_Control")
	ret = switch.Connect() # Connects to first switch detected. 
	if not ret:
		raise RuntimeError("Failed to connect to RF switch.")
	print("RF Switch Connected: {}; SN: {}".format(
		switch.Read_ModelName(foo)[1], 
		switch.Read_SN(foo)[1]
	))	

	if ret:
		print("\nSetting switch from {} to port {}...".format(
			switch.Send_SCPI(":SP8T:STATE?", foo)[2], 
			args.port
		))

		ret = switch.Send_SCPI(":SP8T:STATE:{}".format(args.port), foo)
		print("Done.")
	else:
		print("Operation failed")
	

except Exception as e:
	raise e

finally:
	switch.Disconnect()
	print("K")