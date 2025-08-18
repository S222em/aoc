from os import path

OPERATORS = ["OR", "AND", "NOT", "LSHIFT", "RSHIFT"]
BITS = 16

def parse_instruction(line: str):
    contents = line.strip().split(" ")

    return contents[:-2], contents[-1]

def get_circuit():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return [parse_instruction(line) for line in lines]

def is_gate(instruction):
    return len(instruction[0]) > 1

def can_signal(params, out, state):
    if out in state:
        return False

    for item in params:
        if item in OPERATORS:
            continue

        if item.isdigit():
            continue

        if item not in state:
            return False

    return True

def transform_params(params, state):
    transformed = []

    for param in params:
        if param in OPERATORS:
            transformed.append(param)
        elif param.isdigit():
            transformed.append(int(param))
        else:
            transformed.append(state[param])

    return transformed

def get_signal(params, state):
    params = transform_params(params, state)

    if "OR" in params:
        return params[0] | params[2]

    if "AND" in params:
        return params[0] & params[2]

    if "NOT" in params:
        # as ~ is with signed integer....
        return (1 << BITS) - 1 - params[1]

    if "LSHIFT" in params:
       return params[0] << params[2]

    if "RSHIFT" in params:
        return params[0] >> params[2]

    return params[0]

def run_circuit(circuit, state):
    count = len(circuit)

    while count != 0:
        for params, out in circuit:
            if not can_signal(params, out, state):
                continue

            count -= 1

            state[out] = get_signal(params, state)

    return state

def get_signal_from_wire_a(circuit):
    state = run_circuit(circuit, dict())

    return state["a"]

def main():
    circuit = get_circuit()

    a = get_signal_from_wire_a(circuit)

    print(a)


if __name__ == "__main__":
    main()
