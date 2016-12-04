#!/usr/bin/python2
# encoding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import subprocess
import sys
def sshbrute():
    try:
        print "Sacando logs.."
        print ""
        os.system("grep sshd.\*Did /var/log/auth.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep sshd.\*Did /var/log/auth.log >> logs/SSH-brute-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def sshconf():
    try:
        print "Sacando logs.."
        print ""
        os.system("grep sshd.\*Failed /var/log/auth.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep sshd.\*Failed /var/log/auth.log >> logs/SSH-ConnectionFailed-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def fblogwar():
    try:
        print "Sacando logs.."
        print ""
        os.system("grep WARNING /var/log/fail2ban.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep WARNING /var/log/fail2ban.log >> logs/Fail2ban-warnings-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def fbloginfo():
    try:
        print "Sacando logs.."
        print ""
        os.system("grep INFO /var/log/fail2ban.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep INFO /var/log/fail2ban.log >> logs/Fail2ban-info-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def fblogall():
    try:
        print "Sacando logs.."
        print ""
        os.system("grep fail2ban.* /var/log/fail2ban.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep fail2ban.* /var/log/fail2ban.log >> logs/Fail2ban-ALL-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def aperrorlog():
    try:
        print "Sacando logs.."
        print ""
        os.system("cat /var/log/apache2/error.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("cat /var/log/apache2/error.log >> logs/Apache2-error-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def apaccesslog():
    try:
        print "Sacando logs.."
        print ""
        os.system("cat /var/log/apache2/access.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("cat /var/log/apache2/access.log >> logs/Apache2-Acces-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

def fbloban():
    try:
        print "Sacando logs.."
        print ""
        print "Monstrando lista de baneos."
        os.system("grep '\[ssh\] Ban' /var/log/fail2ban.log")
        print "Mostrando lista de desbaneos"
        os.system("grep '\[ssh\] Unban' /var/log/fail2ban.log")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("grep '\[ssh\] Ban' /var/log/fail2ban.log >> logs/Fail2ban-Ban-logs_`date`_.txt")
            os.system("grep '\[ssh\] Unban' /var/log/fail2ban.log >> logs/Fail2ban-Unban-logs_`date`_.txt")
            pass
        elif pregunta == "n":
            print "Gracias por usar mi scripts :D!"
            pass
        else:
            print "Opcion incorrecta eliga una."
            sshbrute()
    except KeyboardInterrupt:
        print "Saliendo."
        sys.exit(0)

        

