# ping.py
# 
# Copyright 2011 Satanowski <satanowski@gmail.com>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

from subprocess import call
NULL = open('/dev/null')

class Pinger(object):
    """Wrapper for the system "ping" """
    
    def __init__(self, address):
        self.address = address
    
    def ping(self):
        if call("ping -c 1 %s" % self.address, stdout=NULL, stderr=NULL, shell=True) == 0:
            return True
        return False
    
