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
import subprocess
f2b=os.path.isfile("/usr/bin/fail2ban-client") or os.path.isfile("/usr/bin/fail2ban-server")
ap2=os.path.isfile("/usr/bin/apache2")

def requerimientos():
    print "No tiene los requerimientos necesarios para la visualisasion del log. no podra usar este Script."
    os._exit(0)

def checkall():
    if f2b and ap2:
        print("Todo esta instalado..")
    else:
        requerimientos()
