#!/usr/bin/python2
# encoding: utf-8
# Testing Web Framework - Copyright (C) <2016>
#
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
from modules import check
from modules import shellinfo
from modules import tools
from modules import submenu
import argparse
version='v1.1 stable'

shellstt = argparse.ArgumentParser(prog='shellstatus.py',usage='python2 shellstatus.py',description='Con este programa podras revisar y guardar logs.. irc.fukin.tech #PentSec #dev mailto:pentsec@cock.li')
shellstt.add_argument("-u", "--update", help="Actualiza Shellstatus a la mas version mas reciente.", action="store_true")
shellstt.add_argument("-v", "--version", help="Version de Shellstatus", action="store_true")
muestra = shellstt.parse_args()

if muestra.update:   
       print "Actualizando Shellstatus..."
       print ""
       print "Mostrando Cambios.."
       os.system("git pull")
       print "Shellstatus Se actualizo correctamente."
       os._exit(0)

if muestra.version:
    print "Versión: ",version
    os._exit(0)

try:
    print ""
    check.checkall()
    print ""
    def pmenu():
        print ""
        print """==============ShellStatus============="""
        print """
	1) SSH opciones.
        2) Fail2ban opciones.
        3) Apache2: opciones.
        """
        print ""
        print """==============TOOL BOX================"""
        print """
	9) Uso de Disco.
        0) Uptime.
        x) salir..
        """
        men=raw_input("Selecciona: ")
        if men == "1":
            try:
                submenu.submenussh()    
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "2":
            try:
                submenu.submenufb()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "3":
            try:
                submenu.submenuap()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "9":
            try:
                tools.usodisk()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "0":
            try:
                tools.uptime()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "x":
            print "Saliendo."
                
        else:
            pmenu()
    pmenu()

except KeyboardInterrupt:
    print "Saliendo."
    pass
os._exit(0)
