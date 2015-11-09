#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import redis
import click

@click.command()
@click.option('--host', default='localhost', help='redis host')
@click.option('--port',default=6379,help='redis host')
@click.option('--each',help='show result per seconds')
@click.argument('command',nargs = 1)
@click.argument('name',nargs = 1)
def monitor_key(host,port,each,command, name):
    """tools to monitor key'length using llen for list or scard for sets """
    r = redis.StrictRedis(host=host, port=port, db=0)
    try:
        command = getattr(r,command)
    except AttributeError:
        click.echo('unsupported command')
        return
    if each:
        while 1:
            result = command(name)
            click.echo(result)
            time.sleep(3)

    result = command(name)
    click.echo(result)
            
if __name__ == '__main__':
    monitor_key()
    
