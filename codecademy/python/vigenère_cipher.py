import unittest

alphabet = "abcdefghijklmnopqrstuvwxyz"
# idx of 'a' = 0
# idx of 'z' = 25


def encode_char(c_idx, k_idx):
    encode_idx = c_idx - k_idx
    if encode_idx < 0:
        encode_idx = encode_idx + 26
    return chr(encode_idx + 97)


def encode_message(decoded, key):
    msg_key = generate_key_map(decoded, key)
    encoded = ''

    for i in range(len(decoded)):
        if decoded[i] == ' ':
            encoded += decoded[i]
        else:
            c_idx = alphabet.find(decoded[i])
            if c_idx >= 0:
                encoded += encode_char(c_idx, alphabet.find(msg_key[i]))
            else:
                encoded += decoded[i]
    return encoded


def decode_char(idx, offset):
    decode_idx = idx + offset
    if decode_idx > 25:
        decode_idx = decode_idx - 26
    return chr(decode_idx + 97)


def decode_message(encoded, key):
    msg_key = generate_key_map(encoded, key)
    decoded = ''
    for i in range(len(encoded)):
        if encoded[i] == ' ':
            decoded += encoded[i]
        else:
            c_idx = alphabet.find(encoded[i])
            if c_idx >= 0:
                decoded += decode_char(c_idx, alphabet.find(msg_key[i]))
            else:
                decoded += encoded[i]
    return decoded


def generate_key_map(msg, key):
    mapped_key = ''
    key_idx = 0
    for c in msg:
        if c in alphabet:
            mapped_key += key[key_idx]
            key_idx += 1
            if key_idx == len(key):
                key_idx = 0
        else:
            mapped_key += c
    return mapped_key


class CypherTests(unittest.TestCase):
    def test_encode_char_GivenIndexAndOffset_ReturnsExpectedChar(self):
        self.assertEqual('a', encode_char(1, 1))
        self.assertEqual('z', encode_char(0, 1))
        self.assertEqual('y', encode_char(0, 2))

    def test_generate_key_map_GivenMessage_AndKey_IteratesKeyOverMessage(self):
        self.assertEqual('catcatc atc atcatca!', generate_key_map('ciphers are awesome!', 'cat'))
        self.assertEqual('dogdogd ogd ogdogdo!', generate_key_map('ciphers are awesome!', 'dog'))
        self.assertEqual('dogdogd ogd! ogdogdo!', generate_key_map('ciphers are! awesome!', 'dog'))

    def test_encode_message_GivenMessage_AndKey_ReturnsExpectedEncodedMessage(self):
        self.assertEqual('aiwfeyq ayc adcsvke!', encode_message('ciphers are awesome!', 'cat'))
        self.assertEqual('aiwfeyq ayc! adcsvke!', encode_message('ciphers are! awesome!', 'cat'))
        self.assertEqual('ysapo pkangnn gs msn!', encode_message('astro imaging is fun!', 'cat'))
        self.assertEqual('xenoa cjmafza fe zrz!', encode_message('astro imaging is fun!', 'dog'))

    # ================================

    def test_decode_char_GivenIndexAndOffset_ReturnsExpectedIndex(self):
        self.assertEqual('c', decode_char(1, 1))
        self.assertEqual('a', decode_char(25, 1))
        self.assertEqual('b', decode_char(25, 2))
        self.assertEqual('d', decode_char(15, 14))

    def test_decode_message_GivenEncodedMessage_AndKey_SuccessfullyDecodes(self):
        self.assertEqual('astro imaging is fun!', decode_message('ysapo pkangnn gs msn!', 'cat'))
        self.assertEqual('astro imaging is fun!', decode_message('xenoa cjmafza fe zrz!', 'dog'))
