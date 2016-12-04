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
import datetime

datos = datetime.datetime.now()
dato = str(datos)[:10]

def usodisk():
    try:
        print "Sacando logs.."
        print ""
        os.system("df -ah | grep /dev/sd")
        print "Desea guardar estos logs ?"
        pregunta=raw_input("s/n : ")
        if pregunta == "s":
            os.system("df -ah | grep /dev/sd >> logs/DATOS-Usodisco-logs_.txt")
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

def uptime():
    os.system("uptime")


    
