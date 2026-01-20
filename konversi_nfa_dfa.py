def dfa_simulation(input_string):
    # Definisi state awal
    current_state = 'q0'
    
    # Jalankan proses untuk setiap karakter input
    print(f"Start state: {current_state}")
    
    for char in input_string:
        if char not in ['p', 'r']:
            return "Input tidak valid (Hanya p atau r)"
        
        # Logika transisi berdasarkan tabel DFA
        if current_state == 'q0':
            if char == 'p': current_state = 'q1_q2'
            else: current_state = 'DEAD'
            
        elif current_state == 'q1_q2':
            if char == 'p': current_state = 'q1'
            else: current_state = 'q1_q2'
            
        elif current_state == 'q1':
            if char == 'p': current_state = 'DEAD'
            else: current_state = 'q2'
            
        elif current_state == 'q2':
            if char == 'p': current_state = 'q1'
            else: current_state = 'q1'
            
        elif current_state == 'DEAD':
            current_state = 'DEAD'
            
        print(f"Input '{char}' -> State sekarang: {current_state}")

    # Cek apakah state akhir adalah Final State ({q1} atau {q1, q2})
    final_states = ['q1', 'q1_q2']
    if current_state in final_states:
        return "HASIL: String DITERIMA (Accepted)"
    else:
        return "HASIL: String DITOLAK (Rejected)"

# --- Uji Coba ---
print("--- Simulasi DFA ---")
test_input = input("Masukkan string (contoh: prp): ")
hasil = dfa_simulation(test_input)
print(hasil)
