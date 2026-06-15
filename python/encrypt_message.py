#!/usr/bin/env python3
"""Black Veil — Vigenere encryptor.

Generate the ciphertext your players will intercept, from a plaintext and a key.
Dependency-free standard-library Python (3.8+), so a referee can run it on anything.

Example:
    python encrypt_message.py --key VEILGHOST "NODO ECHO NOVE"
    # -> ISLZ KJVG GJZM
"""
from __future__ import annotations

import argparse
import sys

ALPHABET_SIZE = 26
ASCII_A = ord("A")


def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    """Classic Vigenere over A-Z. Non-letters pass through untouched.

    The key advances only on alphabetic characters, so spaces and punctuation
    in the plaintext do not desync the key stream.
    """
    key_shifts = [ord(k) - ASCII_A for k in key.upper() if k.isalpha()]
    if not key_shifts:
        raise ValueError("Key must contain at least one letter A-Z.")

    sign = -1 if decrypt else 1
    out: list[str] = []
    ki = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = sign * key_shifts[ki % len(key_shifts)]
            out.append(chr((ord(ch) - ASCII_A + shift) % ALPHABET_SIZE + ASCII_A))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Vigenere-encrypt a Black Veil message.")
    parser.add_argument("plaintext", help="the message to encrypt (quote it)")
    parser.add_argument("--key", "-k", required=True, help="the Vigenere key, e.g. VEILGHOST")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    try:
        print(vigenere(args.plaintext, args.key, decrypt=False))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
