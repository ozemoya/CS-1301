import sys

def parse_ram_program(filename):
    registers = {}
    code = []
    labels = {}
    
    with open(filename, 'r') as f:
        lines = f.readlines()

        # Initialize mode (True if we are reading register initializations)
        init_mode = True

        for line in lines:
            line = line.strip()
            
            if line.startswith('#') or not line:
                continue
            
            if init_mode:
                if '=' in line:
                    reg, val = line.split('=')
                    registers[reg.strip().upper()] = int(val.strip())
                else:
                    init_mode = False

            if not init_mode:
                instruction = {}
                parts = line.split()

                if ':' in parts[0]:
                    instruction['labeldef'] = parts[0][:-1]
                    labels[instruction['labeldef']] = len(code)
                    parts = parts[1:]

                instruction['opcode'] = parts[0]

                if instruction['opcode'] in ['INC', 'DEC', 'CLR', 'MOV']:
                    instruction['register1'] = parts[1]
                    if instruction['opcode'] == 'MOV':
                        instruction['register2'] = parts[2]
                elif instruction['opcode'] == 'JMP':
                    instruction['jmplabel'] = parts[1]
                elif instruction['opcode'].endswith('JMP'):
                    instruction['register1'] = parts[1]
                    instruction['jmplabel'] = parts[2]

                code.append(instruction)
    
    return registers, code, labels


def execute_ram_program(registers, code, labels, debug=False):
    pc = 0
    while pc < len(code):
        instruction = code[pc]

        if debug:
            print("Executing:", end=' ')
            if 'labeldef' in instruction:
                print(instruction['labeldef'] + ":", end='\t')
            else:
                print("\t", end='')
            print(instruction['opcode'], end=' ')
            if 'register1' in instruction:
                print(instruction['register1'], end=' ')
            if 'register2' in instruction:
                print(instruction['register2'], end=' ')
            if 'jmplabel' in instruction:
                print(instruction['jmplabel'], end=' ')
            print()

        if instruction['opcode'] == 'INC':
            registers[instruction['register1']] += 1
            pc += 1
        elif instruction['opcode'] == 'DEC':
            if registers[instruction['register1']] > 0:
                registers[instruction['register1']] -= 1
            pc += 1
        elif instruction['opcode'] == 'CLR':
            registers[instruction['register1']] = 0
            pc += 1
        elif instruction['opcode'] == 'MOV':
            registers[instruction['register1']] = registers[instruction['register2']]
            pc += 1
        elif instruction['opcode'] == 'JMP':
            pc = labels[instruction['jmplabel']]
        elif instruction['opcode'].endswith('JMP'):
            if registers[instruction['register1']] == 0:
                pc = labels[instruction['jmplabel']]
            else:
                pc += 1
        elif instruction['opcode'] == 'CONTINUE':
            break

def main():
    debug = '-d' in sys.argv
    filename = sys.argv[-1]

    registers, code, labels = parse_ram_program(filename)

    print("Input:")
    for reg, val in registers.items():
        print(f"{reg} ==> {val}")

    execute_ram_program(registers, code, labels, debug)

    print("\nOutput:")
    print(f"R1 = {registers['R1']}")

if __name__ == '__main__':
    main()
