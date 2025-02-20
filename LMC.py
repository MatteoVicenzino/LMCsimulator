# Matteo Vicenzino SM3201397

class LMC:
    # class containing the methods to simulate the LMC program execution
    def __init__(self, memory):
        self.memory = memory # memory of 100 cells
        self.pc = 0 # program counter
        self.accumulator = 0 # regirster
        self.flag = False # overflow flag
        self.input = [] # input queue
        self.output = [] # output queue
        
        
    def execute_lmc(self, input_list = [], slow = False):
        print("Executing...")
        """
        function that takes in input:
        - input_list: the input list to be used by the program
        - slow: a boolean to run the program step by step if True
        the function simulate the LMC program execution
        """
        [self.input.append(item) for item in input_list] # save input list into the queue
        
        try:
            while self.pc < 100: # loop until HLT instruction, or the program counter is invalid
                
                operation = self.memory[self.pc] // 100 # save the operation
                value = self.memory[self.pc] % 100 # save the memory address of the value

                if slow: # step by step execution
                    print(f"PC: {self.pc} ACC: {self.accumulator} FLAG: {self.flag} INPUT: {self.input} OUTPUT: {self.output}")
                    print("MEMORY: ", self.memory)
                    input("Press Enter to continue...")
                
                self.do_instruction(operation, value)
                
        except StopIteration:
            print("Program executed successfully.")
        
    
    def do_instruction(self, operation, value):
        """
        function that given the operation code and the memory address value as integers,
        performs the corresponding instruction
        """
        if operation == 1: # ADD: add value to accumulator
            sum = self.accumulator + self.memory[value]
            if sum > 999:
                self.accumulator = sum % 1000
                self.flag = True
            else:
                self.accumulator = sum
                self.flag = False
            self.pc = (self.pc + 1) % 1000

        elif operation == 2: # SUB: subtract value from accumulator
            diff = self.accumulator - self.memory[value]
            if diff < 0:
                self.accumulator = diff % 1000
                self.flag = True
            else:
                self.accumulator = diff
                self.flag = False
            self.pc = (self.pc + 1) % 1000

        elif operation == 3: # STA: store value into memory
            self.memory[value] = self.accumulator
            self.pc = (self.pc + 1) % 1000
            
        elif operation == 5: # LDA: load value into accumulator
            self.accumulator = self.memory[value]
            self.pc = (self.pc + 1) % 1000
            
        elif operation == 6: # BRA: unconditional branch to value
            self.pc = value
            
        elif operation == 7: # BRZ: branch to value if accumulator is zero
            self.pc = value if self.accumulator == 0 and self.flag == False else self.pc + 1
            
        elif operation == 8: # BRP: branch to value if accumulator is positive
            self.pc = value if self.flag == False else self.pc + 1
            
        elif operation == 9 and value == 1: # INP: take input from the queue
            try:
                self.accumulator = self.input.pop(0)
            except IndexError:
                raise EmptyInput("Error: empty input queue")
            self.pc = (self.pc + 1) % 1000
            
        elif operation == 9 and value == 2: # OUT: append accumulator to output list
            self.output.append(self.accumulator)
            self.pc = (self.pc + 1) % 1000            
            
        elif operation == 0: # HLT: halt the program
            raise StopIteration
        
        else: # invalid operation
            raise InvalidOperationError(f"invalid operation in line {self.pc}: {operation} {value}")
        
        
class EmptyInput(Exception):
    pass
class InvalidOperationError(Exception):
    pass