# -*- coding: utf-8 -*-

import sys

from redis import Redis
from redis.exceptions import RedisError
import argparse

from hotwatch import __version__
from hotwatch.query import length_for_names


# Instantiate the argument parser:
parser = argparse.ArgumentParser(prog='hotwatch', description="Command line "
    "utility for monitoring the status of HotQueue queue instances.",
    epilog="Exit status will be 1 if an error occurred, 0 otherwise.")

# Add the version argument:
parser.add_argument('--version', action='version', version=__version__)

# Add Redis-related arguments (host, port, db to connect to):
parser.add_argument('--host',
    help="Server hostname (example: 127.0.0.1)")
parser.add_argument('--port', type=int,
    help="Server port (example: 6379)")
parser.add_argument('--db', type=int,
    help="Database number (example: 1)")

# Add queue name positional args:
parser.add_argument('queue_names', nargs='+', metavar='QUEUE_NAME')


def main():
    args = parser.parse_args()
    
    # Connect to the given Redis host:
    store_kwargs = {}
    for arg_name in ['host', 'port', 'db']:
        value = getattr(args, arg_name, None)
        if value is None:
            continue
        store_kwargs[arg_name] = value
    store = Redis(**store_kwargs)
    
    try:
        store.ping() # Test the connection to Redis.
    except RedisError, e:
        print >> sys.stderr, "Error:", e
        sys.exit(1)
    
    # Print the queue names and lengths:
    for item in length_for_names(store, *args.queue_names):
        print "%s: %d items" % item


if __name__ == '__main__':
    main()
