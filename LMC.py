class Assembler:
    # class containg the methods to parse and decode the LMC assembly into machine code
    def __init__(self):
        self.memory = [0]*100 # memory of 100 cells
        self.pc = 0 # program counter
        self.labels = {}
        self.operations = {
            "ADD": 100,
            "SUB": 200,
            "STA": 300,
            "LDA": 500,
            "BRA": 600,
            "BRZ": 700,
            "BRP": 800,
            "INP": 901,
            "OUT": 902,
            "HLT": 0,
            "DAT": 0
        }
        

    @staticmethod
    def parse_file(file):
        """
        function that takes in input the file object
        and returns in output two different files parsed as a list of strings
        - nocomment_file: file without comments, evey line is a string
            this file will be used in get_labels function
        - parsed_file: file parsed completly, every line is a list of strings
            this file used for decode_instructions function
        """
        # initialize the two files
        nocomment_file = []
        parsed_file = []
        
        for line in file:
            # remove comments
            parsed_line = line.split("//")[0].strip()
            if parsed_line:
                nocomment_file.append(parsed_line.upper())
                parsed_file.append([word.upper() for word in parsed_line.split()]) # split the line
                
        # check if the file is too long to be loaded into LMC memory
        if len(parsed_file) > 100:
            raise FileTooLongError("Program has more than 100 instructions, cannot be load into LMC memory")
        
        return nocomment_file, parsed_file
    
    
    def get_labels(self,nocomment_file):
        """
        function that takes in input the nocomment_file and populates the dictionary self.labels
        with the labels as keys and the corresponding memory address as values
        """
        self.pc == 0
        for line in nocomment_file:
            line = line.split(maxsplit=1)
            if len(line) > 1 and line[0] not in self.operations:
                self.labels[line[0]] = self.pc
            self.pc = (self.pc + 1) % 1000


    def translate_op(self, op, mem = None):
        """
        function that takes in input the instruction as OPERATION and MEMORY ADDRESS
        and returns the corresponding operation code
        """
        if mem is None: # case Operation only
            return self.operations[op]
        elif mem.isdigit(): # case Operation + Number
            return self.operations[op] + int(mem)
        elif mem in self.labels: # case Operation + Label
            return self.operations[op] + self.labels[mem]
        else:
            raise InvalidInstructionError(f"invalid instruction in line {self.pc}:  {op} {mem}")
        
    
    def decode_instructions(self, parsed_file):
        print("Decoding...")
        """ 
        function that takes in input the parsed_file 
        and populates the list self.memory with the instructions translated into machine code
        """
        self.pc = 0
        for line in parsed_file:
            
            if len(line) == 1: # case Operation only
                if line[0] in self.operations:
                    self.memory[self.pc] = Assembler.translate_op(self, line[0])
                else:
                    raise InvalidInstructionError(f"invalid instruction in line {self.pc}:  {line}")
                
            elif len(line) == 2:
                if line[0] in self.operations: # case Operation + Address
                    self.memory[self.pc] = Assembler.translate_op(self, line[0], line[1])
                    
                elif line[0] in self.labels and line[1] in self.operations: # case Label + Operation
                    self.memory[self.pc] = Assembler.translate_op(self, line[1])
                else:
                    raise InvalidInstructionError(f"invalid instruction in line {self.pc}:  {line}")
            
            elif len(line) == 3: # case Label + Operation + Address
                if line[0] in self.labels and line[1] in self.operations:
                    self.memory[self.pc] = Assembler.translate_op(self, line[1], line[2])
                else:
                    raise InvalidInstructionError(f"invalid instruction in line {self.pc}:  {line}")
                    
            else:
                raise InvalidInstructionError(f"invalid instruction in line {self.pc}:  {line}")
            
            self.pc = (self.pc + 1) % 1000
            
        print(f"File compiled successfully.")
        return self.memory
    
    
class FileTooLongError(Exception):
    pass
class InvalidInstructionError(Exception):
    pass
