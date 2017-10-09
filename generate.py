#!/usr/bin/env python

import argparse
from jinja2 import Environment, FileSystemLoader
from pyclibrary import CParser


def generate(header, struct):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('offsets.c')
    parser = CParser(header)
    members = [member[0] for member in parser.defs['structs'][struct].members]

    with open("offsets.c", "w") as fd:
        fd.write(template.render(header=header, struct=struct, members=members))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate c code to find all offsets of a struct.')
    parser.add_argument('header', type=str, help='the header file defining the struct')
    parser.add_argument('struct', type=str, help='the target structure')
    args = parser.parse_args()

    generate(args.header, args.struct)
