import binascii

def reseed_inverse(s, enc_byte):
    # Mendekripsi ulang operasi reseed
    d = (enc_byte ^ s) * 12297829382473034410 % 2147483647
    return d

def decrypt(s, enc):
    assert s <= 2**32
    c, d = 0, s
    dec = b''
    l = len(enc)
    while c < l:
        d = reseed_inverse(d, enc[c])
        dec += (enc[c] ^ ((d >> 16) & 0xff)).to_bytes(1, 'big')
        c += 1
    return dec

enc_hex = b'b0cb631639f8a5ab20ff7385926383f89a71bbc4ed2d57142e05f39d434fce'
enc = binascii.unhexlify(enc_hex)

# Memecahkan kode dengan mencoba seed yang berbeda
for s in range(2**32):
    dec = decrypt(s, enc)
    if b'CCTF{' in dec:
        print("Seed:", s)
        print("Plaintext:", dec.decode())
        break

