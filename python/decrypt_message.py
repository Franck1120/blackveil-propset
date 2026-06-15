#!/usr/bin/env python3
"""Black Veil — Vigenere decryptor / solve-verifier.

Decrypt an intercepted ciphertext, or verify a team's solve in the field.
Dependency-free standard-library Python (3.8+).

Examples:
    python decrypt_message.py --key VEILGHOST "ISLZ KJVG GJZM"
    # -> NODO ECHO NOVE

    # Verify a solve against the expected plaintext (exit code 0 = match):
    python decrypt_message.py --key VEILGHOST --expect "NODO ECHO NOVE" "ISLZ KJVG GJZM"
"""
from __future__ import annotations

import argparse
import sys

# Reuse the single source of truth for the cipher.
from encrypt_message import vigenere


def _normalize(text: str) -> str:
    """Collapse to compare meaningfully: uppercase, single-spaced."""
    return " ".join(text.upper().split())


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Vigenere-decrypt / verify a Black Veil solve.")
    parser.add_argument("ciphertext", help="the intercepted ciphertext (quote it)")
    parser.add_argument("--key", "-k", required=True, help="the Vigenere key, e.g. VEILGHOST")
    parser.add_argument(
        "--expect",
        "-e",
        default=None,
        help="optional expected plaintext; exit 0 if it matches, 2 otherwise",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    try:
        plaintext = vigenere(args.ciphertext, args.key, decrypt=True)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(plaintext)

    if args.expect is not None:
        if _normalize(plaintext) == _normalize(args.expect):
            print("[OK] solve matches expected plaintext", file=sys.stderr)
            return 0
        print("[MISMATCH] solve does NOT match expected plaintext", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
