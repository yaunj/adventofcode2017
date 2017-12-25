#!/usr/bin/env python
from collections import defaultdict
from itertools import count

challenge = open('day13.txt').readlines()
test_case = """0: 3
1: 2
4: 4
6: 4""".split('\n')

def create_firewall(lines):
    fw = defaultdict(int)

    for line in lines:
        layer, _range = map(int, line.strip().split(': '))
        fw[layer] = _range * 2 - 2

    return [fw[i] for i in range(max(fw) + 1)]


def follow_packet(fw, delay=0, debug=False):
    severity = 0
    caught = False

    start = delay
    stop = start + len(fw)

    for step, layer in zip(range(start, stop), fw):
        if layer == 0:
            continue

        if step % layer == 0:
            if debug:
                debugmsg = 'Caught at {step} (depth of layer: {depth})'
                print(debugmsg.format(step=step, depth=layer))
            caught = True
            severity += step * ((layer + 2) // 2)

    return (caught, severity)

test_fw = create_firewall(test_case)
fw = create_firewall(challenge)
print('Checking score for test case:')
print(follow_packet(test_fw, debug=True))

print('Checking score for challenge:')
print(follow_packet(fw))

def break_firewall(fw, debug=False):
    for delay in count():
        if debug and delay % 1000000 == 0:
            print('delay =', delay)
        stopped, severity = follow_packet(fw, delay)
        if not stopped:
            return delay

print('Cheking minimum delay for test case:')
print(break_firewall(test_fw, debug=True))
print('Cheking minimum delay for challenge:')
print(break_firewall(fw, debug=True))
