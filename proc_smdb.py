# !python
import sys
import json

def load_targ(targ='smdb.json'):
    with open(targ) as f:
        return json.load(f)

def find_key(key, targ=None):
    if targ is None:
        targ = load_targ()
    """ Search JSON string `targ` for `keys`, return path and value """
    if isinstance(targ, dict):
        for k, v in targ.items():
            if k == key:
                yield [k], v
            for path, vn in find_key(key, v):
                yield [[k, *path], vn]
    if isinstance(targ, list):
        for i, v in enumerate(targ):
            for path, vn in find_key(key, v):
                yield [[i, *path], vn]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        find_key(sys.argv[1], load_targ())
    else:
        find_key(sys.argv[1], sys.argv[2])
