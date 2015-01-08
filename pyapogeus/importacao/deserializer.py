# -*- coding: utf-8 -*-
# Adapted code from http://stackoverflow.com/users/84270/john-machin
# Find at http://stackoverflow.com/questions/4914008/efficient-way-of-parsing-fixed-width-files-in-python/4916375#4916375
import struct
import datetime
import cStringIO
import pprint
import re
from functools import partial

def cnv_alfa(s=''):
    return s.rstrip()

def cnv_num(s=0):
    return int(re.sub(' ', '0', s))

def cnv_hour(s):
    try:
        hour =  datetime.datetime.strptime(s, "%HH%MM%SS")
    except ValueError:
        return False
    else:
        return hour

def cnv_date(s):
    try:
        return datetime.datetime.strptime(s, "%d%m%Y")
    except ValueError:
        return False

#def cnv_float(inteiro, decimal=0):
    #def do_it(s):
        #if decimal == 0:
            #return float(s[:inteiro])
        #return float(s[:inteiro]+'.'+ s[inteiro:(inteiro + decimal)])
    #return do_it

def cnv_float(inteiro, decimal=0):
    def do_it(s):
        if decimal == 0:
            return (s[:inteiro])
        return (s[:inteiro]+'.'+ s[inteiro:(inteiro + decimal)])
    return do_it



def unpack_fields(fieldspecs='', raw_data=''):
    fieldspecs = fieldspecs
    raw_data = raw_data

    fieldspecs.sort(key=lambda x: x[1]) # just in case

    # build the format for struct.unpack
    unpack_len = 0
    unpack_fmt = ""
    for fieldspec in fieldspecs:
        start = fieldspec[1] - 1
        end = start + fieldspec[2]
        if start > unpack_len:
            unpack_fmt += str(start - unpack_len) + "x"
        unpack_fmt += str(end - start) + "s"
        unpack_len = end
    field_indices = range(len(fieldspecs))
    unpacker = struct.Struct(unpack_fmt).unpack_from

    class Record(object):
        pass
        # or use named tuples

    f = cStringIO.StringIO(raw_data)
    for line in f:
        # The guts of this loop would of course be hidden away in a function/method
        # and could be made less ugly
        raw_fields = unpacker(line)
        r = Record()
        for x in field_indices:
            setattr(r, fieldspecs[x][0], fieldspecs[x][3](s=raw_fields[x]))
        return r.__dict__






    #if fieldspecs = '':
        #return False

    #fieldspecs = fieldspecs
    #fieldspecs.sort(key=lambda x: x[1]) #ordena a lista

    #unpack_len = 0
    #unpack_fmt = ""
    #for fieldspec in fieldspecs:
        #start = fieldspec[1] - 1
        #end = start + fieldspec[2]
        #if start > unpack_len:
            #unpack_fmt += str(start - unpack_len) + "x"
        #unpack_fmt += str(end - start) + "s"
        #unpack_len = end
    #field_indices = range(len(fieldspecs))
    #return struct.Struct(unpack_fmt).unpack_from

#class Record(object):
    #pass
### or use named tuples

#def unpack_data(raw_line=False):

    #if not raw_line:
        #return False

    #f = cStringIO.StringIO(raw_line)
    #raw_fields = unpacker(raw_line)
    #r = Record()
    #for x in field_indices:
        #print x
        #setattr(r, fieldspecs[x][0], fieldspecs[x][3](raw_fields[x]))
    #return r.__dict__ #or r