# Parse example testbench output to format accepetable to MoSAIC programming
# Example: > indicates ZHW input and < indicates ZHW output
# > 0x03fb68a10f857246d
# > 0x03fb68a0ebe2cf1f2
# > 0x03fb68a0f6f29eb34
# < 0x01235d10111006807
# < 0x0887cbc92e5eb83ba
# < 0x04ddc0b5d81ed5df5

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file to parse", 
	type=str, dest="input_fname")
parser.add_argument("-o", help="Parse output file prefix, output to output_fname.in and output_fname.out, output_fname.in32, output_fname.out32", 
	type=str, dest="output_fname")
args= parser.parse_args()

file_in = open(args.input_fname, 'r')
Lines = file_in.readlines()
file_wr_in = open(args.output_fname+".in", 'a')
file_wr_out = open(args.output_fname+".out", 'a')

# Strips the newline character
for line in Lines:
    if line[0] == '>':
        file_wr_in.write(line[5:])
    if line[0] == '<':
        file_wr_out.write(line[5:])