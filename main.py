# Matteo Vicenzino SM3201397

from Assembler import Assembler
from LMC import LMC

# get program filename from user and open file
try:
    filename = input("Insert file name: ")
    filepath = f"./lmc/{filename}.lmc"
    file = open(filepath, "r")
except (FileNotFoundError, PermissionError):
    raise FileNotFoundError(f"File {filename}.lmc not found or permission denied")

# get the parsed file as a list
nocomment_file, parsed_file = Assembler.parse_file(file)

# convert instruction into machine code and save it in memory
compile = Assembler()
compile.get_labels(nocomment_file)
compile.decode_instructions(parsed_file)

file.close()


# get input from user
get_input = input("Insert input numbers separated by spaces: ").split()
if all((v.isdigit() and int(v) < 1000) for v in get_input):
    input_list = list(map(int, get_input))
else:
    raise ValueError("Invalid input")

# ask for option to run the program step by step
slow = input("Do you want to run the program in slow mode? (y/n): ")
if slow not in ["y", "n"]:
    raise ValueError("Invalid input")

# simulate the program execution 
execute = LMC(compile.memory)
if slow == "n":
    execute.execute_lmc(input_list, False)
elif slow == "y":
    execute.execute_lmc(input_list, True)

# print the output queue
print("Output queue: ", execute.output)