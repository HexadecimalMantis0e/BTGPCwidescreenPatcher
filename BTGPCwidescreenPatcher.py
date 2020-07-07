import os
import struct
import argparse

# Bionicle: The Game PC widescreen patcher
# Currently only supports this version that runs on win10:
# http://biomediaproject.com/bmp/play/retail-games/bionicle/

parser = argparse.ArgumentParser()
parser.add_argument("executable", help = "BIONICLE.exe")
parser.add_argument("aspectratio", help = "Monitor aspect ratio")
parser.add_argument("veritcalresolution", help = "Monitor vertical resolution")
args = parser.parse_args()

aspectRatio = {
    "5:4": 0x3FA00000,
    "4:3": 0x3FAAAAAB,
    "3:2": 0x3FC00000,
    "16:10": 0x3FCCCCCD,
    "15:9": 0x3FD55555,
    "16:9": 0x3FE38E39,
    "21:9": 0x4017B426,
    "3x5:4": 0x40700000,
    "3x4:3": 0x40800000,
    "3x16:10": 0x4099999A,
    "3x15:9": 0x40A00000,
    "3x16:9": 0x40AAAAAB
}

f0 = open(args.executable,"r+b")

# patch the aspect ratio

f0.seek(0x3CD0B, os.SEEK_SET)
f0.write(struct.pack("i", aspectRatio[args.aspectratio]))

# patch the horizontal resolution

f0.seek(0xC72CC, os.SEEK_SET)

# Calculate the horizontal resolution from the vertical resolution

f0.write(struct.pack("h",(int(args.veritcalresolution)//3) * 4))

f0.close()
