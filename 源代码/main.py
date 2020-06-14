import sys, os, struct

def encodeString(str):
    key_index = 0
    str_encode = ''
    bytes = bytearray(str)
    for b in bytes:
        b_encode = (b + key_bytes[key_index]) % 256
        str_encode += struct.pack('B', b_encode)
        key_index = (key_index + 1) % len(key_bytes)
    return str_encode

def decodeString(str):
    key_index = 0
    str_decode = ''
    bytes = bytearray(str)
    for b in bytes:
        b_decode = (b + 256 - key_bytes[key_index]) % 256
        str_decode += struct.pack('B', b_decode)
        key_index = (key_index + 1) % len(key_bytes)
    return str_decode

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print 'Usage: python', sys.argv[0], 'encode/decode file [key]'
    exit(1)
if sys.argv[1] not in ('encode', 'decode'):
    print 'Usage: ', sys.argv[0], 'encode/decode'
    exit(1)
filename = sys.argv[2]
if not os.path.isfile(filename):
    print 'File "' + filename + '" is not exsisted'
    print 'Usage: python', sys.argv[0], 'encode/decode file [key]'
    exit(1)

key = 'KEY'
if len(sys.argv) == 4:
    key = sys.argv[3]
key_bytes = bytearray(key)

mode = sys.argv[1]

file_mode_name = filename + '.after' + mode

if mode == 'encode':
    file = open(filename, 'r')
    file_encode = open(file_mode_name, 'w')
    str = file.read()
    str_encode = encodeString(str)
    file_encode.write(str_encode)
    file.close()
    file_encode.close()
    os.system("sh out.sh"+' '+mode+' '+filename+' '+file_mode_name)
    
if mode == 'decode':
    file = open(filename, 'r')
    file_decode = open(file_mode_name, 'w')
    str = file.read()
    str_decode = decodeString(str)
    file_decode.write(str_decode)
    file.close()
    file_decode.close()
    os.system("sh out.sh"+' '+mode+' '+filename+' '+file_mode_name)
