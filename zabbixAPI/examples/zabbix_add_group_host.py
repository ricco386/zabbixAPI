"""Example script that do an API call to create a sample test data on Zabbix
server.
When you run this script it will create for you a test group, test host. 
For all newly created items in zabbix minimal data required has been used.

You have to define connection parameters in this script in order to run it.
Script was tested on zabbix API 1.4 which is part of Zabbix 2.0.0 or higher.

@author: richard.kellner
@created: 27.10.2012
"""
from zabbix_api import ZabbixAPI

"""You need to specify connection variables"""
server="http://127.0.0.1"
username="api"
password="apipass"

def create_group(group):
    """Function that will create host group on Zabbix Server."""
    result = zapi.hostgroup.create({ 'name' : group })
    try:
        result['groupids']
    except NameError:
        """API throws an exception if such group already exists"""
        print 'There was na error while creating group'

    print 'Group "'+ group +'" has been created with id: '+ \
            result['groupids'][0]
    return result['groupids'][0]

def create_host(host):
    """Function that will create host on Zabbix Server."""
    result = zapi.host.create({ "host" : (host),
        "interfaces" : [{
            "type": 1,
            "main": 1,
            "useip" : 1,
            "ip" : "127.0.0.1",
            "dns" : "",
            "port" : "10050",
            }],
        "groups" : [{
            "groupid" : groupid,
            }],
        })
    try:
        result['hostids']
    except NameError:
        """API throws an exception if such host already exists"""
        print 'There was na error while creating host'
    print 'Host "'+ host +'" has been created with id: '+ \
        result['hostids'][0]
    return result['hostids'][0]

def test_API_version():
    """Method to check if server has compatible version of API."""
    if zapi.api_version() <= 1.4:
        raise Exception('Example script works only with API 1.4 or higher.')

zapi = ZabbixAPI(server=server, path="", log_level=30)
zapi.login(username, password)

test_API_version()
groupid = create_group('test_API_group')
hostid = create_host('test_API_host')
