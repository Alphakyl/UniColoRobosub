'''

State Synchronization System

'''

import json, redis

r = redis.StrictRedis()

ser, deser = json.dumps, json.loads

DELIM = '.'

# Effectively isomorphic to a dictionary (JSON-limited).

class Mapper:
  def __init__(self, k):
    self.k = k
  
  def __call__(self, v = None):

    if v is None:
      sub = [x for x in map(lambda x:x.decode('ascii'), r.keys(self.k + '*')) if x != self.k]
 
      if len(sub) > 0:
        c = len(self.k)
        sub = [x[c:][1:] for x in sub]
        sub = [x[:x.index('.') if '.' in x else len(x)] for x in sub]
        return {k: self.__getattr__(k)() for k in sub}

      else:
        v = r.get(self.k)
        return deser(v.decode('ascii')) if v is not None else v

    else:
      if type(v) is dict:
        for (k, v) in v.items():
          self.__getattr__(k)(v)

      elif type(v) in (float, int, str):
        r.set(self.k, ser(v))

      else:
        raise Exception('Unserializable')

  def __getattr__(self, attr):
    return Mapper(self.k + DELIM + attr)

state = Mapper('')
state.k = 'state'
