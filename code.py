import base64
import requests
import re
import Queue
import config

q = Queue.Queue()

def populate_queue():
        for ch in 'This is test content':
        	q.put(ch)

def get_char():
	if q.empty():
		populate_queue()
	return q.get()