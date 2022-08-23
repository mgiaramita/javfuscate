#!/usr/bin/python
import sys, random

def encode_char(char):
	ec = hex(ord(char))
	ec = r"\u00" + ec[2:]
	return ec

def is_encodable_char(char):
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

def encode_line(line):
	new_line = ""
	for char in line:
		if is_encodable_char(char):
			# 10% chance char won't be encoded because why not
			if random.randint(0,99) <= 90:
				new_line += encode_char(char)
			else:
				new_line += char
		else:
			new_line += char
	return new_line

def main():
	try:
		input_file_name = sys.argv[1]
		output_file_name = "javfuscate_output_" + input_file_name
	except IndexError:
		print("Invalid args. Correct usage:")
		print("    javfuscate <input_file.java>")
		input_file_name = input("You can also type the file name here with format <input_file.java>: ")
		output_file_name = "javfuscate_output_" + input_file_name

	try:
		with open(input_file_name, "r") as java_program:
			java_program_lines = java_program.readlines()	
	except IOError:
		print("Could not open program " + input_file_name)
	
	try:
		output_program = open(output_file_name, "w")
		for line in java_program_lines:
			output_program.write(encode_line(line))
	except IOError:
		print("Could not create and write to program " + output_file_name)

	output_program.close()
	print("File " + output_file_name + " was successfully created")

if __name__ == "__main__":
	main()
