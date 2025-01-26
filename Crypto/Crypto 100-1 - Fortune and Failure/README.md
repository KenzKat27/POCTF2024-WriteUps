# Crypto 100-1 - Fortune and Failure

## Challenge Description
Normally in a situation like this I'd have to give you a clue about the key. Well, this time I don't need to. Three reasons: 1) The key is short. 2) You know part of the message. 3)

Cipher text: hottx{unsh_4_w4ck_7zrfuyh_7y3_h1dl5}

# Solution
This was encrypted with a [Vigenere Cipher](https://www.dcode.fr/vigenere-cipher).

To decipher the key, I knew the first portion was poctf{uwsp. Assuming A is a shift of 0 with the Vigenere addition/subtraction cipher rules, shifting p -> h is an addition of 18, which translates to S for the key. o -> o is 0, which is A. c -> t is a shift of 17, which is R. t -> t is also A, and then the pattern repeats with xunsh -> fuwsp. Removing the repetition, the key works out to be **SARA**.

Decoding the cipher reveals the entire flag.

## Flag
`poctf{uwsp_4_w4lk_7hrough_7h3_h1ll5}`