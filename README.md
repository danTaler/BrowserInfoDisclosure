<h1>ChromeDataDump</h1>

This is a -POST Exploitation- broswer sensitive files dump.
This program attempts to dump sensitive/personal information from gmail such as:

1. credentials stored in browsers.
2. Autofill data
3. Cookies

It extracts the data from the local broswer's files stored in Windows for the current active user using SQLiTE database commands 
and decrypts the encrypted values using the CryptUnprotectData module built on python 'win32crypt' plugin.

Chrome database files:

C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Login Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Web Data

IE:


Use of Windows DPAPI:
User Master Key: C:\Users\john\AppData\Roaming\Microsoft\Protect\
System Master key: %APPDATA%\Microsoft\Protect\%SID%
