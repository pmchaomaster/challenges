#!/usr/bin/env python

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


class DoubleLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None