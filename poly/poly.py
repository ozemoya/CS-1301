def read_data(fname):
    with open(fname) as f:
        lines = f.readlines()
    operations_and_data = []
    for line in lines:
        operation, data = line.split(' ', 1)
        operations_and_data.append((operation, data.strip()))
    return operations_and_data

def to_dict(poly_str):
    poly_dict = {}
    for term in poly_str.split(','):
        coeff, exp = term.split(':')
        coeff_int = int(coeff)
        if coeff_int != 0:  # Ensure we don't add terms with zero coefficients
            poly_dict[int(exp)] = coeff_int
    return poly_dict

def add_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return {k: v for k, v in result.items() if v != 0}

def multiply_dicts(dict1, dict2):
    result = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            new_key = key1 + key2
            new_value = value1 * value2
            if new_key in result:
                result[new_key] += new_value
            else:
                result[new_key] = new_value
    return {k: v for k, v in result.items() if v != 0}

def to_string(poly_dict):
    terms = []
    for exp, coeff in sorted(poly_dict.items(), reverse=True):
        if coeff != 0:  # This ensures we don't add terms with zero coefficients
            terms.append(f"{coeff}:{exp}")
    return ','.join(terms)

def main():
    data = read_data('poly.dat')
    results = []

    for operation, poly_data in data:
        poly1_str, poly2_str = poly_data.split()
        poly1 = to_dict(poly1_str)
        poly2 = to_dict(poly2_str)

        if operation == "add":
            result = add_dicts(poly1, poly2)
        elif operation == "mul":
            result = multiply_dicts(poly1, poly2)

        results.append(to_string(result))

    # Display results
    for res in results:
        print(res)

    # Write to file
    with open('poly_answers.dat', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == "__main__":
    main()
