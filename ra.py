def parse_file(filename):
    registers = {}
    code = []
    labels = {}
    with open(filename,'r') as file:
        lines = file.readlines()   
    
    init_section, code_section = [],[]
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
        registers[reg.strip().upper()]= int(value.strip())
    for i, line in enumerate(code_section):
        instruction = {}
        if ':' in line:
            label, line = line.split(':')
            instruction['labeldef'] = label.strip().upper()
            label[label.strip().upper()] = i
        tokens = line.strip().split()
        instruction['opcode'] = tokens[0]
        if tokens[0] in ['INC','DEC', 'CLR']:
            instruction['register1']
        elif tokens[0] == 'MOV':
            instruction['register1'], instruction['register2'] = tokens[1], tokens[2]
        elif tokens[0] == 'JMP':
            instruction ['opcode'] = 'UJMP'
            instruction['jmplabel'] = tokens[1].upper()
        elif tokens[0].startswith('R') and 'JMP' in tokens:
            instruction['opcode'] = tokens[0]
            instruction['register1'] = tokens[0]
            instruction['jmplabel'] = tokens[2].upper()
        code.append(instruction)

    return registers, code, labels
def execute_ram_program(registers, code, labels, debug=False):
    print("Input:")
    for reg,value in registers.items():
        print(f"{reg} ==> {value}")
    print()

    instr_ptr = 0
    while instr_ptr < len(code):
        instr = code[instr_ptr]
    if debug:
            if 'labeldef' in instr:
                print(f"Executing: {instr['labeldef']}: {instr['opcode']}", end=' ')
            else:
                print(f"Executing: \t{instr['opcode']}", end=' ')
            if 'register1' in instr:
                print(f"{instr['register1']}", end=' ')
            if 'register2' in instr:
                print(f"{instr['register2']}", end=' ')
            if 'jmplabel' in instr:
                print(f"JMP {instr['jmplabel']}", end=' ')
            print()

        # Execute instruction based on opcode
    if instr['opcode'] == 'INC':
            registers[instr['register1']] += 1
    elif instr['opcode'] == 'DEC':
            if registers[instr['register1']] > 0:
                registers[instr['register1']] -= 1
    elif instr['opcode'] == 'CLR':
            registers[instr['register1']] = 0
    elif instr['opcode'] == 'MOV':
            registers[instr['register1']] = registers[instr['register2']]
    elif instr['opcode'] == 'UJMP':
            instr_ptr = labels[instr['jmplabel']]
            pass
    elif instr['opcode'] == 'CJMP':
            if registers[instr['register1']] == 0:
                instr_ptr = labels[instr['jmplabel']]
                pass
    elif instr['opcode'] == 'CONTINUE':
            continue



