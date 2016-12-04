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
import check
import shellinfo
import tools

print ""
#check.checkall()
print ""
def submenussh():
    try:
        print ""
        print """==============SSH Opciones============="""
        print """
	1) SSH brute force.
        2) SSH: conexiones fallidas.
        x) salir..
        """
        men=raw_input("Selecciona: ")
        if men == "1":
            try:
                shellinfo.sshbrute()    
                submenussh()
            except KeyboardInterrupt:
                submenussh()
        elif men == "2":
            try:
                shellinfo.sshconf()
                submenussh()
            except KeyboardInterrupt:
                submenussh()
        elif men == "x":
            print "Saliendo."
            pass  
        elif men =="":
            print "La opcion no puede estar vacia"
            submenussh()
        else:
            print "Elige una opcion correcta."
            submenussh()

    except KeyboardInterrupt:
        print "Saliendo."
        pass
    os._exit(0)

def submenufb():
    try:
        print ""
        print """==============Fail2Ban Opciones============="""
        print """
        3) Fail2ban log warning.
	4) Fail2ban log info.
        5) Fail2ban log ALL.
        6) Fail2ban log Ban
        x) salir..
        """
        men=raw_input("Selecciona: ")
        if men == "3":
            try:
                shellinfo.fblogwar()
                submenufb()
            except KeyboardInterrupt:
                submenufb()
        elif men == "4":
            try:
                shellinfo.fbloginfo()
                submenufb()
            except KeyboardInterrupt:
                submenufb()
        elif men == "5":
            try:
                shellinfo.fblogall()
                submenufb()
            except KeyboardInterrupt:
                submenufb()
        elif men == "6":
            try:
                shellinfo.fbloban()
                submenufb()
            except KeyboardInterrupt:
                submenufb()
        elif men == "x":
            print "Saliendo."  
        elif men =="":
            print "La opcion no puede estar vacia"
            submenussh()
        else:
            print "Elige una opcion correcta."
            submenussh()

    except KeyboardInterrupt:
        print "Saliendo."
        pass
    os._exit(0)

def submenuap():
    try:
        print ""
        print """==============Apache2 Opciones============="""
        print """
        7) Apache2: Error log.
        8) Apache2: Access log.
        x) salir..
        """
        men=raw_input("Selecciona: ")
        if men == "7":
            try:
                shellinfo.aperrorlog()
                submenuap()
            except KeyboardInterrupt:
                submenuap()
        elif men == "8":
             try:
                shellinfo.apaccesslog()
                submenuap()
             except KeyboardInterrupt:
                submenuap()
        elif men == "x":
            print "Saliendo."        
        elif men =="":
            print "La opcion no puede estar vacia"
            submenussh()
        else:
            print "Elige una opcion correcta."
            submenussh()

    except KeyboardInterrupt:
        print "Saliendo."
        pass
    os._exit(0)
