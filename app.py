import streamlit as st
import genelock_core as gc

# Configuration Streamlit (impérativement au début)
st.set_page_config(
    page_title="GeneLock", 
    page_icon="🧬", 
    layout="wide"
)

st.title("🧬 GeneLock — Encryption & DNA Storage Protocol")
st.write("---")

tab1, tab2, tab3 = st.tabs(["🔐 Encodage Texte -> ADN", "🔓 Décodage ADN -> Texte", "🧬 Simulation de Mutations"])

# TAB 1: ENCODAGE
with tab1:
    st.subheader("Convertir un message en séquence d'ADN")
    user_text = st.text_input("Message secret à encoder :", "VANTARI 2026")
    
    if st.button("Chiffrer et Générer ADN"):
        dna_seq = gc.encode_text_to_dna(user_text)
        dna_hash = gc.compute_hash(dna_seq)
        
        st.success("Séquence générée avec succès !")
        st.code(dna_seq, language="text")
        st.info(f"**Empreinte SHA-256 de la séquence :** `{dna_hash}`")

# TAB 2: DÉCODAGE
with tab2:
    st.subheader("Décoder une séquence d'ADN en texte")
    input_dna = st.text_area("Entrez la séquence d'ADN à décoder :", "AGCT")
    
    if st.button("Décoder"):
        decoded_text = gc.decode_dna_to_text(input_dna.strip().upper())
        st.success(f"**Message décodé :** {decoded_text}")

# TAB 3: MUTATIONS & INTÉGRITÉ
with tab3:
    st.subheader("Simuler le bruit biologique (Mutations)")
    original_dna = st.text_input("Séquence ADN d'origine :", "ATGCGATCGATCGATC")
    num_errors = st.slider("Nombre d'erreurs à injecter :", 1, 5, 2)
    
    if st.button("Injecter Mutations"):
        corrupted_dna, pos = gc.inject_mutations(original_dna, num_errors)
        hash_orig = gc.compute_hash(original_dna)
        hash_corrupt = gc.compute_hash(corrupted_dna)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**ADN d'origine :**")
            st.code(original_dna)
            st.write(f"Hash: `{hash_orig[:16]}...`")
        with col2:
            st.write("**ADN altéré :**")
            st.code(corrupted_dna)
            st.write(f"Hash: `{hash_corrupt[:16]}...`")
            
        if hash_orig != hash_corrupt:
            st.error("🚨 Altération détectée ! L'empreinte cryptographique ne correspond plus.")