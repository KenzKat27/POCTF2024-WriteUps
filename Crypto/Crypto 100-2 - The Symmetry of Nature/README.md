# Crypto 100-2 - The Symmetry of Nature

## Challenge Description
Consider these tales of brothers...

You've probably heard of the constellation Gemini. Most people hear that they're identical twins, but that's actually not true. One, was the son of a mortal, the other the son of Zeus. Can you imagine what it would be like to be Castor, the mortal one? If you guessed they would end up enemies, you'd be wrong.

There was another set of brothers that went by the same names. I'm speaking, of course, of the award-winning film Face/Off where Castor (played by Nicolas Cage) would be considered the leader of the two, though the brother in that case is definitely the brains of the operation. Both brothers die in that film and it seems to me they were both pretty mortal.

84150717615789492248{688795176222681450_8273783252253178253147624750271202558794588687556525149_25153414179812378489258473}

x-.x-.x-.x

## Solution
This was a [pollux cipher](https://toebes.com/codebusters/Samples/Solving_Pollux.htm) with the hint mentioning Castor. I made a python script that translated to morse code based on the knowledge of the key mentioned at the end. Each character in the key correlates to a chart of 0-9 for decrypting the numbers in the ciphertext.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| x | - | . | x | - | . | x | - | . | x |

The resulting [morse code](https://en.wikipedia.org/wiki/Morse_code) can then be decrypted into its respective letters to obtain the flag. The x's denote where the morse code pauses for another letter.

`.--.x---x-.-.x-x..-.{x..-x.--x...x.--.x_..-x-.x.....x--...x---x.--.x.--.x....-x-...x.-..x...--x_..-.x-----x.-.x-.-.x...--x}`

## Flag
POCTF{UWSP_UN57OPP4BL3_F0RC3}