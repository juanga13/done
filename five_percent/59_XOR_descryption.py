import os

"""
lowercase [32, 97, ...122]
"""
KEY_LENGTH = 3
VALID_ASCII_LOWER = 32
VALID_ASCII_UPPER = 126


def is_valid(n):
    return VALID_ASCII_LOWER <= n <= VALID_ASCII_UPPER


if __name__ == '__main__':
    print("Problem 59 - XOR Decryption")
    encrypted_ascii = []
    with open('59_cipher.txt', 'r') as f:
        encrypted_ascii = f.read().split(',')

    result_keys = [[], [], []]
    for key_offset in range(0, KEY_LENGTH):
        for temp_key in range(0, 256):
            # for temp_key in range(110, 112):
            valid = True
            i = key_offset
            while i < len(encrypted_ascii) and valid:
                curr = int(encrypted_ascii[i])
                xor = int(curr ^ temp_key)
                # print("i: " + str(i) + ", temp_key: " +
                #       str(temp_key) + ", xor: " + str(xor))
                if not is_valid(xor):
                    valid = False
                i += KEY_LENGTH
            if valid:
                result_keys[key_offset].append(temp_key)
    # print(result_keys)

    all_three_keys = []
    for i in result_keys[0]:
        for j in result_keys[1]:
            for k in result_keys[2]:
                all_three_keys.append([i, j, k])
    # print(all_three_keys)

    decrypted_results = []
    for keys in all_three_keys:
        decrypted_result = ''
        e_char_count = 0
        key_i = 0
        for enc_key in encrypted_ascii:
            decrypted_result += chr(int(enc_key) ^ keys[key_i])
            if key_i == 2:
                key_i = 0
            else:
                key_i += 1
        for char in decrypted_result:
            if char.lower() == 'e':
                e_char_count += 1
        decrypted_results.append((e_char_count, decrypted_result, keys))

    decrypted_results.sort(reverse=True)
    only_e_char_quants = []
    for item in decrypted_results:
        only_e_char_quants.append(item[0])
    # print(only_e_char_quants)

    file_name = '59_XOR_decryption_OUT.txt'
    with open(file_name, 'w') as f:
        for line in decrypted_results:
            f.write(str(line[2]))
            f.write('\n')
            f.write(line[1])
            f.write('\n\n')
    i += 1

    # get sum result
    sum_result = 0
    for key in decrypted_results[0][1]:
        sum_result += ord(key)
    print(sum_result)
