This is a POST Exploitation broswer dump files.
This program attempts to dump sensitive/personal information such as gmail credentials stored in browsers.

It extracts the data from the local broswer's files stored in Windows for the current active user using SQLiTE database commands 
and decrypts the encrypted values usingthe CryptUnprotectData module built on python 'win32crypt' plugin.

Chrome datanase files:

C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Login Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Web Data

IE:


Use of Windows DPAPI:
User Master Key: C:\Users\john\AppData\Roaming\Microsoft\Protect\
System Master key: %APPDATA%\Microsoft\Protect\%SID%
