## 2018 - Unsupported version:

I have written this script at 2018 when existing frameworks did not inlucde password dumps fro browsers. 
These days there are many and better scripts to pull creds from browsers using popular frameworks (Empire, MSF...).



<h1>ChromeDataDump</h1>
<h3>By: Idan Taler</h3>
This tool attempts to dump Chrome's saved sensitive user's data:

1. credentials stored in browsers.
2. Autofill data
3. Cookies
4. Credit Cards

It extracts the data from the local broswer's files stored in Windows for the current active user using SQLiTE database commands and Windows API Crypt32.dll and decrypts the encrypted values using the CryptUnprotectData module built on python 'win32crypt' plugin.

Chrome user's files:

C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Login Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Web Data
C:\%APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Cookies 

**Useage:** (for Python 2.7)
<br>
*C:/> chrome.py*
<br>
*C:/> chrome.py > myPasswords.txt*

<h4>Added Features not Seen in Other Tools: <br>
- This source code is publically available, you shouldn't execute other commercial tools on your/clients systems. <br>
- Kill the Chrome's processes if data cannot be extracted. Latest Chrome at the time of writing has a new feature that will  not allow you to extract its data if it's running.</h4>
