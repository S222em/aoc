from os import path

def parse_wires(lines):
    return { line[:3]: bool(int(line[5:])) for line in lines }

def parse_gate(line):
    words = line.split(" ")

    a = words[0]
    op = words[1]
    b = words[2]
    out = words[4]

    return (a, op, b, out)

def parse_gates(lines):
    return [parse_gate(line) for line in lines]

def get_wires_and_gates():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        text = puzzle.read().split("\n\n")

    wires = text[0].splitlines()
    gates = text[1].splitlines()

    return parse_wires(wires), parse_gates(gates)

def gate(a, b, op):
    if op == "AND":
        return a and b
    if op == "OR":
        return a or b
    if op == "XOR":
        return a != b

def step(wires, gates):
    done = True
    for (a, op, b, out) in gates:
        if a not in wires or b not in wires or out in wires:
            continue

        done = False
        va = wires[a]
        vb = wires[b]

        wires[out] = gate(va, vb, op)

    return done, wires

def calculate_z_wires_number(wires):
    z_wires = [wire for wire in wires if wire.startswith("z")]
    z_wires.sort(reverse=True, key=lambda wire: int(wire[1:]))

    binary = "".join("1" if wires[wire] else "0" for wire in z_wires)

    return int(binary, 2)

def get_z_wires_number(wires, gates):
    while True:
        done, wires = step(wires, gates)
        if done:
            break

    return calculate_z_wires_number(wires)

def main():
    wires, gates = get_wires_and_gates()

    z_number = get_z_wires_number(wires, gates)

    print(z_number)

if __name__ == "__main__":
    main()
