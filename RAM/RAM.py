import sys

def parse_ram_file(filename):
    """Parse the RAM program file and return registers, code, and labels."""
    registers = {}
    code = []
    labels = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    init_section, code_section = [], []
    in_init_section = True
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line and in_init_section:
            init_section.append(line)
        else:
            in_init_section = False
            code_section.append(line)

    for line in init_section:
        reg, value = line.split('=')
        registers[reg.strip().upper()] = int(value.strip())

    for idx, line in enumerate(code_section):
        instruction = {}
        if ':' in line:
            label, line = line.split(':')
            instruction['labeldef'] = label.strip().upper()
            labels[label.strip().upper()] = idx

        tokens = line.strip().split()
        if not tokens:
            continue

        instruction['opcode'] = tokens[0].upper()
        if tokens[0].upper() in ['INC', 'DEC', 'CLR']:
            instruction['register1'] = tokens[1].upper()
        elif tokens[0].upper() == 'MOV':
            instruction['register1'], instruction['register2'] = tokens[1].upper(), tokens[2].upper()
        elif tokens[0].upper() == 'JMP':
            instruction['opcode'] = 'UJMP'
            instruction['jmplabel'] = tokens[1].upper()
        elif tokens[0].upper().startswith('R') and 'JMP' in tokens:
            instruction['opcode'] = 'CJMP'
            instruction['register1'] = tokens[0].upper()
            instruction['jmplabel'] = tokens[2].upper()
        code.append(instruction)
    return registers, code, labels

def execute_ram_program(registers, code, labels, debug=False):
    """Execute the RAM program."""
    print("Input:")
    for reg, value in registers.items():
        print(f"{reg} ==> {value}")
    print()

    instr_ptr = 0
    while instr_ptr < len(code):
        instr = code[instr_ptr]

        if debug:
            print(f"Executing:", end=' ')
            if 'labeldef' in instr:
                print(f"{instr['labeldef']}:", end=' ')
            print(f"\t{instr['opcode']}", end=' ')
            if 'register1' in instr:
                print(f"{instr['register1']}", end=' ')
            if 'register2' in instr:
                print(f"{instr['register2']}", end=' ')
            if 'jmplabel' in instr:
                print(f"JMP {instr['jmplabel']}", end=' ')
            print()

        if instr['opcode'] == 'INC':
            registers.setdefault(instr['register1'], 0)
            registers[instr['register1']] += 1
        elif instr['opcode'] == 'DEC':
            registers.setdefault(instr['register1'], 0)
            if registers[instr['register1']] > 0:
                registers[instr['register1']] -= 1
        elif instr['opcode'] == 'CLR':
            registers[instr['register1']] = 0
        elif instr['opcode'] == 'MOV':
            registers.setdefault(instr['register1'], 0)
            registers.setdefault(instr['register2'], 0)
            registers[instr['register1']] = registers[instr['register2']]
        elif instr['opcode'] == 'UJMP':
            instr_ptr = labels[instr['jmplabel']]
            continue
        elif instr['opcode'] == 'CJMP':
            if registers[instr['register1']] == 0:
                instr_ptr = labels[instr['jmplabel']]
                continue
        instr_ptr += 1

    print(f"\nOutput:\nR1 = {registers.get('R1', 0)}")

def main():
    """Main function to execute the RAM program."""
    debug_mode = False
    if '-d' in sys.argv:
        debug_mode = True
        sys.argv.remove('-d')

    if len(sys.argv) != 2:
        print("Usage: RAM.py [-d] <ram>")
        return

    filename = sys.argv[1]
    registers, code, labels = parse_ram_file(filename)
    execute_ram_program(registers, code, labels, debug=debug_mode)

main()
