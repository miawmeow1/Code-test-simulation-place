def generate_hamming(data_bits):
    """
    Membuat kode Hamming (even parity) dari data_bits (string biner).
    """
    m = len(data_bits)
    # Tentukan jumlah bit parity
    p = 0
    while (2 ** p) < (m + p + 1):
        p += 1

    # Buat array dengan posisi parity kosong (0 sementara)
    total_len = m + p
    hamming = ['0'] * total_len
    j = 0
    for i in range(1, total_len + 1):
        if i & (i - 1) == 0:  # posisi pangkat dua = parity
            continue
        hamming[i - 1] = data_bits[j]
        j += 1

    # Hitung nilai parity
    for i in range(p):
        parity_pos = 2 ** i
        count = 0
        for bit_pos in range(1, total_len + 1):
            if bit_pos & parity_pos:
                if hamming[bit_pos - 1] == '1':
                    count += 1
        hamming[parity_pos - 1] = '1' if count % 2 != 0 else '0'

    return ''.join(hamming)


def detect_error(hamming_code):
    """
    Mendeteksi posisi error pada kode Hamming (even parity).
    """
    n = len(hamming_code)
    error_pos = 0
    p = 0
    while (2 ** p) <= n:
        parity_pos = 2 ** p
        count = 0
        for bit_pos in range(1, n + 1):
            if bit_pos & parity_pos:
                if hamming_code[bit_pos - 1] == '1':
                    count += 1
        if count % 2 != 0:
            error_pos += parity_pos
        p += 1
    return error_pos


# === MAIN PROGRAM ===
data = "10110001"
print("Data asli:", data)

# 1. Buat kode Hamming
hamming_code = generate_hamming(data)
print("Kode Hamming (benar):", hamming_code)

# 2. Perkenalkan error di bit ke-4 (ubah 1 -> 0 atau 0 -> 1)
error_pos = 4
hamming_list = list(hamming_code)
hamming_list[error_pos - 1] = '0' if hamming_list[error_pos - 1] == '1' else '1'
hamming_with_error = ''.join(hamming_list)
print("Kode Hamming (dengan error di bit ke-4):", hamming_with_error)

# 3. Deteksi error
detected_error = detect_error(hamming_with_error)
if detected_error == 0:
    print("Tidak ada error terdeteksi.")
else:
    print(f"Error terdeteksi pada bit ke-{detected_error}")
