# IE 6 for XP/Server 2003:
#    Protected Storage - HKEY_CURRENT_USER\Software\Microsoft\Protected Storage System Provider


#----IE 7-9 Only !!-----

#Credentials manager:
    #HTTP-Auth, network login creds - ' -  C:\Users\John\AppData\Roaming\Microsoft\Credentials
    #auto-fill, form-based auth     - 'Registry          - HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\IntelliForms\Storage2
    
    # CredEnumerate"  CredWrite() and CredRead().  of the "win32cred" lib to enumerate the credentials, then CryptUnprotectedData
    #python - Module win32cred  - http://timgolden.me.uk/pywin32-docs/win32cred.html

# Protected Storage - old way windows XP IE6
#    API, pstorec.dll  PStoreCreateInstance function, 



#IE v10 (windows 8 only) onwards stores the passwords in Windows Vault or Credential Manager.
    #Windows.Security.Credentials.PasswordVault

#http://securityxploded.com/iepasswordsecrets.php

import win32process
import win32event
import pywintypes
import win32security
import win32api
import win32con
import ntsecuritycon
import win32cred
from binascii import hexlify
import sys

# hashing the URL of the stored creds in REGISTRY. URLs are in Internet history
#Open Internet History   - C:\Users\John\AppData\Local\Microsoft\Windows\Temporary Internet Files
#hash each URL
#Check to see if any creds have been stored



#Windows Credential Manager:

try:
    creds = win32cred.CredEnumerate(None, 0)
    print creds
except pywintypes.error as e:
                if e[0] == 1004:
                    print "[E] Call to CredEnumerate failed: Invalid flags. This doesn't work on XP/2003."
                elif e[0] == 1168:
                    print "[E] Call to CredEnumerate failed: Element not found. No credentials stored for this user. Run as normal user, not SYSTEM."
                elif e[0] == 1312:
                    print "[E] Call to CredEnumerate failed: No such login session. Only works for proper login session - not network logons."
                else:
                    print "[E] Call to CredEnumerate failed: %s" % e[2]
 