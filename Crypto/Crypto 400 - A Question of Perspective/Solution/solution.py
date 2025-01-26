import random

# Given data, copied over
qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
# clarified it's alice's bases
alice_bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']
bob_measurements = [0, 1, None, 1, 0, None, 1, 1, None, 0, 1, None, 0, 1, None, 0, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 1, None, 1, 0, None, 0, 0, None, 0, 1, None, 0, 1, None, 1, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 1, None, 0, 1, None, 1, 0, None, 1, 0, None, 0, 1, None, 0, 0, None, 0, 1, None, 1, 1, None, 1, 1]
encrypted_message = [
    0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 0x6a, 0x0b, 0x0c, 0x50, 
    0xd4, 0x5a, 0x71, 0x87, 0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 
    0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b
]


def bb84(seed):
    # set seed
    random.seed(seed)
    
    # generate bob's bases using seed
    bob_bases = ['R' if random.randint(0, 1) == 0 else 'D' for _ in range(len(alice_bases))]
    
    # correct bob's measurements
    # done by replacing None with relative qubit
    corrected_measurements = bob_measurements[:]
    for i in range(len(corrected_measurements)):
        if corrected_measurements[i] is None:
            corrected_measurements[i] = qubits[i]
    
    # create key by matching alice's and bob's bases
    key = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            if corrected_measurements[i] is not None:
                key.append(corrected_measurements[i])
            
    # extend key with bit repetition
    key_length = len(key)
    message_length = len(encrypted_message) * 8
    extended_key_bits = []
    if key_length < message_length:
        while len(extended_key_bits) < message_length:
            extended_key_bits.extend(key)
    
    # get bytes of the key with bit shifting
    key_bytes = []
    for i in range(0, len(extended_key_bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(extended_key_bits):
                byte |= (extended_key_bits[i + j] << (7 - j))
        key_bytes.append(byte)
    
    # create list of xor'd bytes
    # xor the integers then convert to chars and join the string
    decrypted_message = ''.join(chr(c ^ k) for c, k in zip(encrypted_message, key_bytes))
    
    # check for first flag character
    if decrypted_message[0] == 'p' or decrypted_message[0] == 'P':
        print(decrypted_message)

if __name__ == "__main__":

    # try every random seed in the given seed space
    for seed in range(1, 101):
        bb84(seed)