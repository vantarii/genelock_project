import hashlib
import random

# Dictionnaire basique d'encodage texte -> ADN (2 bits par nucléotide)
BIT_TO_DNA = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}
DNA_TO_BIT = {v: k for k, v in BIT_TO_DNA.items()}

def text_to_bits(text: str) -> str:
    """Convertit une chaîne de texte en séquence binaire."""
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_text(bits: str) -> str:
    """Convertit une séquence binaire en texte."""
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(b, 2)) for b in bytes_list if len(b) == 8)

def encode_text_to_dna(text: str) -> str:
    """Encode un texte en séquence d'ADN."""
    bits = text_to_bits(text)
    # S'assurer que la longueur des bits est paire
    if len(bits) % 2 != 0:
        bits += '0'
    dna = ''.join(BIT_TO_DNA[bits[i:i+2]] for i in range(0, len(bits), 2))
    return dna

def decode_dna_to_text(dna_seq: str) -> str:
    """Décode une séquence d'ADN en texte."""
    bits = ''.join(DNA_TO_BIT.get(n, '00') for n in dna_seq)
    return bits_to_text(bits)

def compute_hash(sequence: str) -> str:
    """Génère l'empreinte cryptographique SHA-256 d'une séquence."""
    return hashlib.sha256(sequence.encode('utf-8')).hexdigest()

def inject_mutations(dna_seq: str, num_errors: int = 2) -> tuple[str, list[int]]:
    """Simule des erreurs/mutations biologiques dans la séquence."""
    seq_list = list(dna_seq)
    nucleotides = ['A', 'C', 'G', 'T']
    corrupted_positions = random.sample(range(len(seq_list)), min(num_errors, len(seq_list)))
    
    for pos in corrupted_positions:
        current = seq_list[pos]
        options = [n for n in nucleotides if n != current]
        seq_list[pos] = random.choice(options)
        
    return ''.join(seq_list), sorted(corrupted_positions)

# --- TEST DE BASE ---
if __name__ == "__main__":
    original_message = "Reine's Secret DNA Message 🌸"
    print(f"Message d'origine : {original_message}")
    
    dna_sequence = encode_text_to_dna(original_message)
    original_hash = compute_hash(dna_sequence)
    print(f"Séquence ADN : {dna_sequence[:30]}...")
    print(f"SHA-256 Origine : {original_hash}")
    
    corrupted_dna, error_pos = inject_mutations(dna_sequence, num_errors=3)
    corrupted_hash = compute_hash(corrupted_dna)
    print(f"\n⚠️ Séquence Corrompue : {corrupted_dna[:30]}...")
    print(f"SHA-256 Corrompu : {corrupted_hash}")
    print(f"Positions des erreurs : {error_pos}")
