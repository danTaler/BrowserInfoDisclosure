<h1>ChromeDataDump</h1>
<h3>By: Idan Taler</h3>
This tool attempts to dump Chrome's saved sensitive user's data:

1. credentials stored in browsers.
2. Autofill data
3. Cookies

It extracts the data from the local broswer's files stored in Windows for the current active user using SQLiTE database commands and Windows API Crypt32.dll and decrypts the encrypted values using the CryptUnprotectData module built on python 'win32crypt' plugin.

Chrome user's files:

C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Login Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Web Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Cookies 

**Useage:** (for Python 2.7)
Windows:
*C:/> chrome.py*

Linux:
*# chrome.py*
