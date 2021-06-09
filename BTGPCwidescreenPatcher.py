import os
import struct
import argparse

# Bionicle: The Game PC widescreen patcher
# Currently only supports the version that runs on Windows 10:

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

f0 = open(args.executable, "r+b")

# patch the aspect ratio
print("Patching aspect ratio...")
f0.seek(0x3CD0B, os.SEEK_SET)
f0.write(struct.pack('I', aspectRatio[args.aspectratio]))

# patch the horizontal resolution
print("Patching horizontal resolution...")
f0.seek(0xC72CC, os.SEEK_SET)

# Calculate the horizontal resolution from the vertical resolution
f0.write(struct.pack('I', (int(args.veritcalresolution) // 0x03) * 0x04))
print("Done!")
f0.close()
