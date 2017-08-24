#!/usr/bin/python2

"""
Reads one or more hex encoded values from a file (split by newlines),
writes them to the specified subdir using the SHA1 of the contents as
the file name.
"""

import os
import sys
import hashlib

def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 3:
        print("Usage: %s input_file target_dir" % (args[0]))
        return 1

    input_file = args[1]
    target_dir = args[2]

    for vec in open(input_file).readlines():
        vec = vec.strip()
        vec_bin = vec.decode('hex')
        sha1 = hashlib.sha1()
        sha1.update(vec_bin)
        hash = sha1.hexdigest()

        out_file = open(os.path.join(target_dir, hash), 'w')
        out_file.write(vec_bin)

if __name__ == '__main__':
    sys.exit(main())
