import upcloud_api

from .common import upcloud_api_call
from ..logger import Logger
from ..outputter import output

@upcloud_api_call
def list_servers(logger, creds):
    manager = upcloud_api.CloudManager(creds['username'], creds['password'])
    servers = manager.get_servers()
    output('server', servers)
