def ubah_huruf(sentence, geser=10):
    pattern = ""
    for teks in sentence:
        if teks.isalpha():
            ubah_ke_unicode = ord('A') if teks.isupper() else ord('a')
            ubah_ke_char = chr((ord(teks) - ubah_ke_unicode + geser) % 26 + ubah_ke_unicode)
            pattern += ubah_ke_char
        else:
            pattern += teks
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB