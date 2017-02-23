#!/usr/bin/python
import sys, random

def encodeChar(char):
	ec = hex(ord(char))
	ec = "\u00" + ec[2:]
	return ec

def isEncodeableChar(char):
	try:
		c = ord(char)
	except TypeError:
		return False

	if c >= 48 and c <= 57:
		return True
	elif c >= 65 and c <= 90:
		return True
	elif c >= 97 and c <= 122:
		return True
	else:
		return False

def encodeLine(line):
	newLine = ""
	for char in line:
		if isEncodeableChar(char):
			#10% chance char wont be encoded because why not
			if random.randint(0,99) <= 90:
				newLine += encodeChar(char)
			else:
				newLine += char
		else:
			newLine += char
	return newLine

def main():
	try:
		input_file_name = sys.argv[1]
		output_file_name = "javfuscate_output_" + input_file_name
	except IndexError:
		print "Invalid args. Correct usage:"
		print "    javfuscate <input_file.java>"
		return -1

	try:
		output_program = open(output_file_name, 'w')
	except IOError:
		print "Could not open program " + input_file_name
	try:
		java_program = open(input_file_name, 'r')
		java_program_lines = java_program.readlines()	
	except IOError:
		print "Could not create file " + output_file_name
	
	for line in java_program_lines:
		output_program.write(encodeLine(line))

	output_program.close()
	java_program.close()

if __name__ == "__main__":
	main()
