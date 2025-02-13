
# Little Man Computer (LMC) Simulator


## Overview

This project is a simulation of the Little Man Computer (LMC), a simple computer model designed for educational purposes. The simulator includes an assembler to convert LMC assembly code into machine code and execute the program.


## Features

- **Assembler**: Translates LMC assembly code into machine code.
- **Simulator**: Executes the compiled LMC programs with input handling.
- **Step by step execution**: Option to run programs in slow mode.
- **Error handling**: Detects invalid instructions, missing input, and memory overflows.


## File Structure

```
├── main.py        # Entry point for the simulator
├── Assembler.py   # Assembler to translate LMC assembly into machine code
├── LMC.py         # LMC execution
├── lmc/           # Directory for LMC assembly programs
└── README.md      # Project documentation
```


## Usage

To run this project, ensure you have Python installed on your system.

Run the simulator using:
```sh
python main.py
```

### Steps:

1. Provide the filename of the LMC program (without extension). The file should be inside the `lmc/` directory and have a `.lmc` extension.
2. Enter input values when prompted, separated by spaces.
3. Choose between normal execution or slow mode.
4. The program executes and prints the output queue at the end.


## LMC Assembly Syntax

Each instruction follows a simple format:

- `ADD X` - Add value at memory location X to the accumulator
- `SUB X` - Subtract value at memory location X from the accumulator
- `STA X` - Store accumulator value at memory location X
- `LDA X` - Load value from memory location X into the accumulator
- `BRA X` - Unconditional branch to instruction at X
- `BRZ X` - Branch to X if accumulator is 0
- `BRP X` - Branch to X if accumulator is positive
- `INP` - Get a value from the input queue and write it in the accumulator
- `OUT` - Write the accumulator value in the output queue
- `HLT` - Halt execution
- `DAT X` - Define a memory location with value X


## Error Handling

The simulator includes custom error handling:

- **FileTooLongError**: Program exceeds 100 instructions.
- **InvalidInstructionError**: Unknown or malformed instruction.
- **EmptyInput**: No input provided when required.
- **InvalidOperationError**: Execution encountered an invalid operation.
