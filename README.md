# 🧬 GeneLock — DNA Data Storage & Integrity Protocol

> **A prototype exploring how digital information can be prepared, encoded, and integrity-checked before DNA-based storage.**

Developed for the **Come Build with AI Hackathon (2026)**.

---

## About The Project

As global digital data creation explodes, conventional storage media (HDDs, SSDs) are reaching physical limits. DNA data storage offers unprecedented density and longevity. However, the biological processes of DNA synthesis and sequencing can introduce mutations and errors, corrupting the stored digital payload.

**GeneLock** is a middleware proof-of-concept designed to ensure data integrity during the encoding and pre-synthesis stages.

---

## Key Features

- **Binary to Quaternary Encoding**: Converts digital text into valid DNA nucleotide sequences ($A, T, C, G$).
- **Cryptographic Guardrail**: Generates a **SHA-256** cryptographic fingerprint of the biological sequence before synthesis.
- **Biological Error Simulation**: Simulates point mutations (substitutions) to stress-test data integrity.
- **Integrity Alert System**: Instant detection of sequence corruption upon reading/decoding.

---
