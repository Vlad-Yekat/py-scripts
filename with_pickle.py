# ! don't work with pickle with untrusted sources!

import pickle

some_obj = {
    'a' : 1,
    'b': [1, 2],
    'c': (2, 4)
}

with open('data.pickle', 'wb') as f:
    pickle.dump(some_obj, f)

zzz = pickle.dumps(some_obj)

with open('data.pickle', 'rb') as f:
    some_new = pickle.load(f)

yyy = pickle.loads(zzz)

print(some_new)
print(yyy)


