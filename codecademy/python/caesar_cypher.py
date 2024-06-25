ASCII_OFFSET = 96
alphabet = "abcdefghijklmnopqrstuvwxyz"


def decode_char(c, offset):
    shifted = ord(c) - ASCII_OFFSET + offset
    if shifted > 26:
        shifted = shifted % 26
    return chr(shifted + ASCII_OFFSET)


def decode_message(msg, offset):
    decoded = ""
    for c in msg:
        if c in alphabet:
            decoded += decode_char(c, offset)
        else:
            decoded += c
    return decoded


def encode_char(c, offset):
    shifted = ord(c) - ASCII_OFFSET - offset
    if shifted <= 0:
        shifted = 26 + shifted
    return chr(shifted + ASCII_OFFSET)


def encode_message(msg, offset):
    encoded = ""
    for c in msg:
        if c in alphabet:
            encoded += encode_char(c, offset)
        else:
            encoded += c
    return encoded


print(decode_message("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(decode_message("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))
print(encode_message("hi vishal! i recieved your message, and i am sending you a message back.", 10))
