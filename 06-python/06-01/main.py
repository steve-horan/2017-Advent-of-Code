+#!/usr/bin/env python
 +import sys
 +
 +with open("main.txt") as f:
 +   banks = [int(x) for x in f.readline().split("\t")]
 +
 +def high_bank():
 +    return banks.index(max(banks))
 +
 +print(banks)
 +configs_len = len(banks) - 1
 +configs = []
 +num = 0
 +while True:
 +    #configs.append(' '.join(str(x) for x in banks))
 +    bank_val = banks[high_bank()]
 +    start = high_bank()
 +    banks[high_bank()] = 0
 +    while bank_val != 0:
 +        if start >= configs_len:
 +            start = -1
 +        print(start, configs_len, len(banks))
 +        start = start + 1
 +        banks[start] = banks[start] + 1
 +        bank_val = bank_val - 1
 +    configs.append(''.join(str(x) for x in banks))
 +    print(num, configs[-1])
 +    num = num + 1
 +    if len(configs) != len(set(configs)):
 +        print(num)
 +        sys.exit(0)
 +