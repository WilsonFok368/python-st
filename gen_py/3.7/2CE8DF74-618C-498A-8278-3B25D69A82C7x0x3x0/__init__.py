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

RecordMap = {
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}' : '_USB_Control',
	'{12E0479C-642F-449A-92A1-1889EF5B72F2}' : 'USB_Control',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
	'{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}' : '_USB_Control',
}


NamesToIIDMap = {
	'_USB_Control' : '{B512BCEF-895B-41B5-A6E6-BA3AB6529F6F}',
}


