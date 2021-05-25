
import random

_used_hash_ids = {}

def get_hash():
	hash = random.getrandbits(64)
	while(hash in _used_hash_ids):
		hash = random.getrandbits(64)
	_used_hash_ids[hash] = 1
	return hash