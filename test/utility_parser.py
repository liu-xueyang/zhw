# Parse example testbench output to format accepetable to MoSAIC programming
# Example: > indicates ZHW input and < indicates ZHW output
# > 0x03fb68a10f857246d
# > 0x03fb68a0ebe2cf1f2
# > 0x03fb68a0f6f29eb34
# < 0x01235d10111006807
# < 0x0887cbc92e5eb83ba
# < 0x04ddc0b5d81ed5df5

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file to parse", 
	type=str, dest="input_fname")
parser.add_argument("-o", help="Parse output file prefix, output to output_fname.in and output_fname.out, output_fname.in32, output_fname.out32", 
	type=str, dest="output_fname")
args= parser.parse_args()

file_in = open(args.input_fname, 'r')
Lines = file_in.readlines()

output_fname_in = args.output_fname+"_in.hex32"
output_fname_out = args.output_fname+"_out.hex32"
if os.path.exists(output_fname_in):
    os.remove(output_fname_in)
if os.path.exists(output_fname_out):
    os.remove(output_fname_out)
file_wr_in = open(output_fname_in, 'a')
file_wr_out = open(output_fname_out, 'a')


# Strips the newline character
for line in Lines:
    if line[0] == '>':
        file_wr_in.write(line[5:13] + '\n')
        file_wr_in.write(line[13:])
    if line[0] == '<':
        file_wr_out.write(line[5:13] + '\n')
        file_wr_out.write(line[13:])