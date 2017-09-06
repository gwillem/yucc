# -*- coding: utf-8 -*-
"""yucc - Your UpCloud CLI.

Copyright (C) Erik Sørensen, 2017.

Usage:
    yucc ls servers [options] [-t <tags>...]
    yucc ls templates [options]
    yucc ls zones [options]
    yucc ls plans [options]
    yucc server create (--hostname=<hostname>) (--plan=<plan>)
      (--login-user=<user> --ssh-key=<ssh-key>) (--os=<os>)
      [--ensure-started] [options]
    yucc server start <uuid> [options]
    yucc server stop <uuid> [options]
    yucc server restart <uuid> [options]
    yucc server delete <uuid> [--delete-storages] [options]
    yucc server info <uuid> [options]
    yucc account [options]
    yucc profile [options]
    yucc [options]

Options:
    --hostname=<hostname>      Hostname of a server
    --title=<title>            Title of a server. If not set it will be the same
                               as the hostname.
    --plan=<plan>              Plan to use for the server
    --login-user=<user>        The username to create on the server
    --ssh-key=<ssh-key>        The ssh public key to deploy to the server
    --zone=<zone>              The zone to deploy to. Default might be read from
                               profile.
    --os=<os>                  The operating system for the new server.
    --ensure-started           Wait for the server to start when creating the
                               server.
    --delete-storages          Also delete storages when deleting server
    -f, --format=<format>      Program output format. [default: json]
    -p, --profile=<profile>    Settings profile to use. Read from
                               ~/.yaccrc file. [default: default]
    -P, --prompt-credentials   Prompt for credentials rather than reading
                               them from profile
    -t, --tags                 Filter on or set tags
    -q, --quiet                Be silent. Only output essential data
    -h, --help                 Show this helpscreen and exit
    -v, --verbose              Verbose output
    --debug                    Output debugging information
    --version                  Print version and exit

Commands:
    ls                         List resources (servers, templates, zones, plans)
    account                    Show basic account information
    profile                    Dump profile information

"""

__version__ = '0.7.2'
__prog__ = 'yucc'
