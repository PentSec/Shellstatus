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
import sys
from modules import check
from modules import shellinfo
version='v1.0n stable'

try:
    print ""
    check.checkall()
    print ""
    def pmenu():
        print ""
        print """Selecciona una de las siguientes opciones."""
        print """
	1) SSH brute force.
        2) SSH: conexiones fallidas.
        3) Fail2ban log warning.
	4) Fail2ban log info.
        5) Fail2an log ALL.
        6) Apache2: Error log.
        7) Apache2: Access log.
        8) Salir.
        """
        men=raw_input("Selecciona: ")
        if men == "1":
            try:
                shellinfo.sshbrute()    
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "2":
            try:
                shellinfo.sshconf()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "3":
            try:
                shellinfo.fblogwar()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "4":
            try:
                shellinfo.fbloginfo()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "5":
            try:
                shellinfo.fblogall()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "6":
            try:
                shellinfo.aperrorlog()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "7":
            try:
                shellinfo.apaccesslog()
                pmenu()
            except KeyboardInterrupt:
                pmenu()
        elif men == "8":
            print "Saliendo."
                
        else:
            pmenu()
    pmenu()

except KeyboardInterrupt:
    print "Saliendo."
    pass
os._exit(0)
