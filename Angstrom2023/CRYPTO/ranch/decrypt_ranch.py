import string

encrypted_flag = "rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}"
possible_shifts = list(range(26))  # There are 26 possible shift values for Caesar cipher

for shift in possible_shifts:
    decrypted_flag = ""
    for char in encrypted_flag:
        if char in string.ascii_lowercase:
            decrypted_flag += chr(((ord(char) - 97 - shift) % 26) + 97)
        else:
            decrypted_flag += char
    print(f"Shift {shift}: {decrypted_flag}")
