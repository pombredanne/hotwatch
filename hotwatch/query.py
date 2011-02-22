# -*- coding: utf-8 -*-

from hotqueue import key_for_name


def length_for_names(store, *queue_names):
    """Return a generator that yields the queue name and number of items for
    each of the given queue names in the given Redis class instance.
    """
    for queue_name in queue_names:
        yield queue_name, store.llen(key_for_name(queue_name))
