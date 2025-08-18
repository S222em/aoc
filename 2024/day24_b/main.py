from os import path
from collections import deque

# This one is just a mess and I was able to find the answer
# in the puzzle using parts of what this came up with.
# Needs some work later...


def parse_wires(lines):
    return {line[:3]: bool(int(line[5:])) for line in lines}


def parse_gate(line):
    words = line.split(" ")

    a = words[0]
    op = words[1]
    b = words[2]
    out = words[4]

    return a, op, b, out


def parse_gates(lines):
    gates = dict()

    for line in lines:
        a, op, b, out = parse_gate(line)
        gates[out] = a, op, b

    return gates


def get_wires_and_gates():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        text = puzzle.read().split("\n\n")

    wires = text[0].splitlines()
    gates = text[1].splitlines()

    return parse_wires(wires), parse_gates(gates)


def format_involved_wires(involved_wires):
    return ",".join(sorted(involved_wires))


def format_bit(type, bit):
    return f"{type}{bit:02d}"


def get_z_wire(bit):
    return format_bit("z", bit)


def get_x_wire(bit):
    return format_bit("x", bit)


def get_y_wire(bit):
    return format_bit("y", bit)


def is_head(wire):
    return wire.startswith("x") or wire.startswith("y")


def find_involved_wires(gates):
    involved_wires = set()
    z_wires = [wire for wire in gates.keys() if wire.startswith("z")]
    bits = len(z_wires) - 1

    for bit in range(bits + 1):
        involved = find_involved_wire_from_bit(bit, bits, gates)
        if involved:
            involved_wires.add(involved)

    return format_involved_wires(involved_wires)


def is_xor_or_or(op, bit, bits):
    return (op == "XOR" and bit < bits) or (op == "OR" and bit == bits)


def is_and_with_previous_bit(a, op, b, bit):
    previous_bit = bit - 1
    x_wire = get_x_wire(previous_bit)

    return op == "AND" and a == x_wire or b == x_wire


def is_xor_with_current_bit(a, op, b, bit):
    x_wire = get_x_wire(bit)

    return op == "XOR" and a == x_wire or b == x_wire


def is_and_or_xor(a, op, b, bit):
    return is_and_with_previous_bit(a, op, b, bit) or is_xor_with_current_bit(a, op, b, bit)


def is_and_with_previous_wires(a, op, b, pa, pb):
    return op == "AND" and (a == pa and b == pb) or (b == pa and a == pb)


def is_and_with_previous_wires_or_previous_bit(a, op, b, pa, pb, bit):
    return is_and_with_previous_bit(a, op, b, bit) or is_and_with_previous_wires(a, op, b, pa, pb)

# ---------
# z01 XOR (jfs, wsb)
# |jfs AND (x00, y00)
# |wsb XOR (y01, x01)
# ---------
# z02 XOR (rqf, rjt)
# |rqf OR (vqv, dqt)
# ||vqv AND (x01, y01)
# ||dqt AND (jfs, wsb)
# |||jfs AND (x00, y00)
# |||wsb XOR (y01, x01)
# |rjt XOR (y02, x02)
# ---------
# z03 XOR (nbr, jwm)
# |nbr XOR (y03, x03)
# |jwm OR (bcj, qff)
# ||bcj AND (rqf, rjt)
# |||rqf OR (vqv, dqt)
# ||||vqv AND (x01, y01)
# ||||dqt AND (jfs, wsb)
# |||||jfs AND (x00, y00)
# |||||wsb XOR (y01, x01)
# |||rjt XOR (y02, x02)
# ||qff AND (y02, x02)
def find_involved_wire_from_bit(bit, bits, gates):
    z_wire = get_z_wire(bit)
    a, op, b = gates[z_wire]

    if not is_xor_or_or(op, bit, bits):
        print(f"1 {z_wire}")
        return z_wire

    if is_head(a):
        return None

    aa, aop, ab = gates[a]
    ba, bop, bb = gates[b]

    if is_head(aa) and not is_and_or_xor(aa, aop, ab, bit):
        print(f"2 {a}")
        return a

    if is_head(ba) and not is_and_or_xor(ba, bop, bb, bit):
        print(f"2 {b}")
        return b

    if is_head(aa) and is_head(ba):
        return None

    previous_z_wire = get_z_wire(bit - 1)
    pa, _, pb = gates[previous_z_wire]

    daa, daop, dab = gates[ba if is_head(aa) else aa]
    dba, dbop, dbb = gates[bb if is_head(ab) else ab]

    if daop != "AND":
        print(f"3 {ba if is_head(aa) else aa}")
        return ba if is_head(aa) else aa

    if dbop != "AND":
        print(f"3 {bb if is_head(ab) else ab}")
        return bb if is_head(ab) else ab

    return None

def main():
    _, gates = get_wires_and_gates()

    involved_wires = find_involved_wires(gates)

    print(involved_wires)


if __name__ == "__main__":
    main()
