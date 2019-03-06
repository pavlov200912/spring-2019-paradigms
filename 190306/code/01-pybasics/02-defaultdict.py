#!/usr/bin/env python3

class defaultdict:
    # d = {} # static

    def get(self, key):
        if not hasattr(self, 'd'):
            self.d = {}
        if key not in self.d:
            self.d[key] = []
        return self.d[key]

# defaultdict.d = {}
# defaultdict.get = lambda self, key: ...

a = defaultdict()
defaultdict.get(a, 'key').append(10)
a.get('key').append(20)
assert a.get('key') == [10, 20]
assert a.get('not_found') == []

b = defaultdict()
print(b.get('key'))
