"""Example script that do an API connection to Zabbix server and print API
version.

You have to define connection parameters in this script in order to run it.

@author: richard.kellner
@created: 28.10.2012
"""
import sys
from zabbix_api import ZabbixAPI, ZabbixAPIException

"""You need to specify connection variables"""
server="http://127.0.0.1"
username="api"
password="apipass"

zapi = ZabbixAPI(server=server, path="", log_level=30)
zapi.login(username, password)

try:
    zapi.login(username, password)
    print "Logged in: %s" % str(zapi.test_login())
    print "Zabbix API Version: %s" % zapi.api_version()
except ZabbixAPIException, e:
    sys.stderr.write(str(e) + '\n')
