# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
# From type library '{2CE8DF74-618C-498A-8278-3B25D69A82C7}'
# On Wed Feb 12 08:45:01 2020
''
makepy_version = '0.5.01'
python_version = 0x30702f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{2CE8DF74-618C-498A-8278-3B25D69A82C7}')
MajorVersion = 3
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class _USB_Control(DispatchBaseClass):
	CLSID = IID('{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}')
	coclass_clsid = IID('{12E0479C-642F-449A-92A1-1889EF5B72F2}')

	def Connect(self, SN=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809389, LCID, 1, (2, 0), ((8, 17),),SN
			)

	def ConnectByAddress(self, Address=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809391, LCID, 1, (2, 0), ((2, 17),),Address
			)

	def Disconnect(self):
		return self._oleobj_.InvokeTypes(1610809392, LCID, 1, (24, 0), (),)

	def GetExtFirmware(self, a0=defaultNamedNotOptArg, a1=defaultNamedNotOptArg, a2=defaultNamedNotOptArg, a3=defaultNamedNotOptArg
			, DocFirmware=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809345, 1, (2, 0), ((16386, 3), (16386, 3), (16386, 3), (16386, 3), (16392, 3)), 'GetExtFirmware', None,a0
			, a1, a2, a3, DocFirmware)

	def GetSequence_ContinuousMode(self):
		return self._oleobj_.InvokeTypes(1610809366, LCID, 1, (2, 0), (),)

	def GetSequence_Direction(self):
		return self._oleobj_.InvokeTypes(1610809368, LCID, 1, (2, 0), (),)

	def GetSequence_Dwell(self, StepNo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809376, LCID, 1, (3, 0), ((2, 1),),StepNo
			)

	def GetSequence_DwellUnits(self, StepNo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809377, LCID, 1, (2, 0), ((2, 1),),StepNo
			)

	def GetSequence_NoOfCycles(self):
		return self._oleobj_.InvokeTypes(1610809364, LCID, 1, (3, 0), (),)

	def GetSequence_NoOfSteps(self):
		return self._oleobj_.InvokeTypes(1610809372, LCID, 1, (2, 0), (),)

	def GetSequence_SwitchTo(self, StepNo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809374, LCID, 1, (2, 0), ((2, 1),),StepNo
			)

	def GetUSBConnectionStatus(self):
		return self._oleobj_.InvokeTypes(1610809349, LCID, 1, (2, 0), (),)

	def GetUSBDeviceName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610809347, LCID, 1, (8, 0), (),)

	def Get_Address(self):
		return self._oleobj_.InvokeTypes(1610809382, LCID, 1, (2, 0), (),)

	def Get_Available_Address_List(self, SN_List=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809351, 1, (2, 0), ((16392, 3),), 'Get_Available_Address_List', None,SN_List
			)

	def Get_Available_SN_List(self, SN_List=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809350, 1, (2, 0), ((16392, 3),), 'Get_Available_SN_List', None,SN_List
			)

	def Get_SP4T_State(self):
		return self._oleobj_.InvokeTypes(1610809384, LCID, 1, (2, 0), (),)

	def Read_ModelName(self, ModelName=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809362, 1, (2, 0), ((16392, 3),), 'Read_ModelName', None,ModelName
			)

	def Read_SN(self, SN=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809378, 1, (2, 0), ((16392, 3),), 'Read_SN', None,SN
			)

	def Send_SCPI(self, SndSTR=defaultNamedNotOptArg, RetSTR=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809395, 1, (2, 0), ((16392, 3), (16392, 3)), 'Send_SCPI', None,SndSTR
			, RetSTR)

	def SetSequence_ContinuousMode(self, ContinuousMode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809367, LCID, 1, (2, 0), ((2, 1),),ContinuousMode
			)

	def SetSequence_Direction(self, Direction=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809369, LCID, 1, (2, 0), ((2, 1),),Direction
			)

	def SetSequence_NoOfCycles(self, NoOfCycles=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809365, LCID, 1, (2, 0), ((3, 1),),NoOfCycles
			)

	def SetSequence_NoOfSteps(self, NoOfSteps=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809373, LCID, 1, (2, 0), ((2, 1),),NoOfSteps
			)

	def SetSequence_OFF(self):
		return self._oleobj_.InvokeTypes(1610809371, LCID, 1, (2, 0), (),)

	def SetSequence_ON(self):
		return self._oleobj_.InvokeTypes(1610809370, LCID, 1, (2, 0), (),)

	def SetSequence_Step(self, StepNo=defaultNamedNotOptArg, SwitchTo=defaultNamedNotOptArg, Dwell=defaultNamedNotOptArg, DwellUnits=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809375, LCID, 1, (2, 0), ((2, 1), (2, 1), (3, 1), (2, 1)),StepNo
			, SwitchTo, Dwell, DwellUnits)

	def Set_Address(self, Address=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610809380, 1, (2, 0), ((16386, 3),), 'Set_Address', None,Address
			)

	def Set_SP4T_COM_To(self, p=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610809385, LCID, 1, (2, 0), ((2, 1),),p
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}", _USB_Control )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
# From type library '{2CE8DF74-618C-498A-8278-3B25D69A82C7}'
# On Wed Feb 12 08:45:01 2020
''
makepy_version = '0.5.01'
python_version = 0x30702f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{2CE8DF74-618C-498A-8278-3B25D69A82C7}')
MajorVersion = 3
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

_USB_Control_vtables_dispatch_ = 1
_USB_Control_vtables_ = [
	(( 'GetExtFirmware' , 'a0' , 'a1' , 'a2' , 'a3' , 
			 'DocFirmware' , None , ), 1610809345, (1610809345, (), [ (16386, 3, None, None) , (16386, 3, None, None) , 
			 (16386, 3, None, None) , (16386, 3, None, None) , (16392, 3, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetUSBDeviceName' , None , ), 1610809347, (1610809347, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetUSBConnectionStatus' , None , ), 1610809349, (1610809349, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'Get_Available_SN_List' , 'SN_List' , None , ), 1610809350, (1610809350, (), [ (16392, 3, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'Get_Available_Address_List' , 'SN_List' , None , ), 1610809351, (1610809351, (), [ (16392, 3, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'Read_ModelName' , 'ModelName' , None , ), 1610809362, (1610809362, (), [ (16392, 3, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_NoOfCycles' , None , ), 1610809364, (1610809364, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_NoOfCycles' , 'NoOfCycles' , None , ), 1610809365, (1610809365, (), [ (3, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_ContinuousMode' , None , ), 1610809366, (1610809366, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_ContinuousMode' , 'ContinuousMode' , None , ), 1610809367, (1610809367, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_Direction' , None , ), 1610809368, (1610809368, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_Direction' , 'Direction' , None , ), 1610809369, (1610809369, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_ON' , None , ), 1610809370, (1610809370, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_OFF' , None , ), 1610809371, (1610809371, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_NoOfSteps' , None , ), 1610809372, (1610809372, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_NoOfSteps' , 'NoOfSteps' , None , ), 1610809373, (1610809373, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_SwitchTo' , 'StepNo' , None , ), 1610809374, (1610809374, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'SetSequence_Step' , 'StepNo' , 'SwitchTo' , 'Dwell' , 'DwellUnits' , 
			 None , ), 1610809375, (1610809375, (), [ (2, 1, None, None) , (2, 1, None, None) , (3, 1, None, None) , 
			 (2, 1, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_Dwell' , 'StepNo' , None , ), 1610809376, (1610809376, (), [ (2, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'GetSequence_DwellUnits' , 'StepNo' , None , ), 1610809377, (1610809377, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Read_SN' , 'SN' , None , ), 1610809378, (1610809378, (), [ (16392, 3, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'Set_Address' , 'Address' , None , ), 1610809380, (1610809380, (), [ (16386, 3, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Get_Address' , None , ), 1610809382, (1610809382, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'Get_SP4T_State' , None , ), 1610809384, (1610809384, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Set_SP4T_COM_To' , 'p' , None , ), 1610809385, (1610809385, (), [ (2, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'SN' , None , ), 1610809389, (1610809389, (), [ (8, 17, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ConnectByAddress' , 'Address' , None , ), 1610809391, (1610809391, (), [ (2, 17, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'Disconnect' , ), 1610809392, (1610809392, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Send_SCPI' , 'SndSTR' , 'RetSTR' , None , ), 1610809395, (1610809395, (), [ 
			 (16392, 3, None, None) , (16392, 3, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}", _USB_Control )
