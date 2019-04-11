
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import sys
import os

@click.command()
@click.option('--source', default="./2017-07-13.tmk.geojson", help="Source file to split")
@click.option('--destination', default="./tmp", help="Destination folder for files")
@click.option('--count_per_file', default=10000, help="Number of polygons per file")
def split(source, destination, count_per_file):
    file = open(source, 'r')
    line = file.readline()
    header = ''
    while is_not_a_feature(line):
        if (not line.startswith('"crs')):
          header += line
          line = file.readline()
    number=0
    while True:
        output=open("%s/%s.geojson" %(destination, number),'w')
        output.write(header)
        number+=1
        feature=file.readline()
        # Stop when we find the end of the file
        if is_not_a_feature(feature):
            break
        else:
            for i in range(count_per_file):
                if is_not_a_feature(feature):
                    print(feature)
                    if (i < count_per_file -1):
                        print(i)
                        print(count_per_file)
                        # remove last ',' on features
                        output.seek(-1, os.SEEK_END)
                        output.truncate()
                    output.write("]}")
                    output.close()
                    sys.exit("Done!")
                else:
                    if feature == '}':
                        print("wrong!!!")
                    output.write(feature)
                    feature=file.readline()
            output.write("]}")
            output.close()

def is_not_a_feature(str):
  # Pretty weak way to check if the given string is not a geojson feature
  return not str.startswith('{ "type":')

if __name__ == "__main__":
    split()
