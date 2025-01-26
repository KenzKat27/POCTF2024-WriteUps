# Crypto 400 - A Question of Perspective

## Challenge Description
You have been hired by a tech company to assess the security of thier quantum communication system. The system uses the BB84 protocol for key distribution. During your assessment, you've intercepted some qubits and their bases during an exchange between Alice and Bob, but some of Bob's measurements are incorrect at every third qubit due to an eavesdropping scenario. Since this is a new system still in testing, the seed space is restricted to positive integers between 1 and 100.

Qubits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]

Bases = ['R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'R', 'D', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'D', 'R', 'R', 'R', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'R', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'R', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'R', 'D', 'D']

Measurements = [0, 1, ?, 1, 0, ?, 1, 1, ?, 0, 1, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 0, 0, ?, 0, 1, ?, 0, 1, ?, 1, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 1, ?, 0, 1, ?, 1, 0, ?, 1, 0, ?, 0, 1, ?, 0, 0, ?, 0, 1, ?, 1, 1, ?, 1, 1]

Encrypted Message = [0x23, 0x59, 0x86, 0x1e, 0x60, 0xcf, 0xdc, 0x4e, 0x6a, 0x0b, 0x0c, 0x50, 0xd4, 0x5a, 0x71, 0x87, 0xdb, 0x0c, 0x46, 0x1d, 0x63, 0x44, 0xba, 0x5e, 0x37, 0xd3, 0x9a, 0x4b, 0x77, 0x4b, 0x3d, 0x4b]

## Solution
This one was fun to solve as I got to learn about [BB84](https://medium.com/quantum-untangled/quantum-key-distribution-and-bb84-protocol-6f03cc6263c5). By the time I got around to attempting this challenge, a hint was given for the basic process of correcting the measurements and decrypting the encrypted message:

>"The basic process for correcting mismeasurements for eavesdropping scenarios with BB84 is to 1) generate bases, 2) correct measurements, 3) sift the key, 4) decrypt. In this case there are a few small steps in between such as extending the key and xoring with key chunks, but that's the basic idea. There is also a separate way to solve the challenge, which I will not provide a hint on, but which you can discover with a little skill in crypto-analysis."

I asked for clarification about the bases we were given, and the bases intercepted were Alice's. So for solving this, I first needed to randomly generate Bob's bases. My solution is aiming for a brute-force approach in this case, since the only knowledge I was given was the seed space being between 1 and 100 (inclusive). I can generate the bases being R or D for Bob as the seed used in the random generator for the encrypted would create the same bases each time subsequently.

`bob_bases = ['R' if random.randint(0, 1) == 0 else 'D' for _ in range(len(alice_bases))]`

The process of correcting the incorrect measurements, in this case, uses the interecepted qubits to replace the ?.

To create the key, a key in BB84 protocol is based off of which bases from both Alice's and Bob's match. If the bases don't match, the corrected measurement is not used in the key (due to the eavesdropping).

After creating the base key, the bits have to be extended to match the number of bits needed for XOR'ing the encrypted message. Qubits are bits, not bytes, so the math is done in respect to bits. I used simple bit repetition across the key until the number of bits were equal to the number of bits in the message.

I then converted the key into bytes as each letter was a byte in the encrypted message, and XOR'd each individual byte with the encrypted message. I had to convert via bit shifting as using numpy gave me issues for converting correctly to decrypt the message. Eventually my program printed out a flag that matched the format for the CTF.

## Flag
`poctf{uwsp_f10w3r5_f0r_41g3rn0n}`