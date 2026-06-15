# Black Veil — Prop Set

Sanitized prop set, radio config, and reference tooling for **Operation Black Veil**, a
field-deployable Meshtastic/LoRa cryptography puzzle designed for an airsoft milsim event.

> Full design writeup: **Black Veil: A Field-Deployable Crypto Puzzle Over Meshtastic**
> by Francesco "Kekko" Rocco — Hephios Lab.

This repo lets you **reproduce the technique**, not the event. Names, coordinates, and
event-identifying details are removed or replaced with placeholders on purpose. The goal is
to give other field-crypto game designers a working skeleton: paper props, a radio config,
and a dependency-free Vigenère tool to generate and verify your own challenge.

## What's the puzzle (one paragraph)

Players recover a Vigenère **key assembled from three separate props**, decrypt an intercepted
ciphertext into a node identifier (`NODO ECHO NOVE` → `ECHO-9`), then exfiltrate intel as a
**direct message to that one node only** — never broadcasting it across the shared mesh, where
hostile nodes would hear it. The whole objective compresses into one API argument:
`destinationId`.

## Contents

| File | What it is |
|------|------------|
| `meshtastic_config.yaml` | Sanitized node config (region, preset, BT PIN, role) |
| `prop_a_template.md` | On-body notes — cipher type + key hint |
| `prop_b_template.md` | Technical log — key material, node table, ciphertext (DOC_1) |
| `prop_c_template.md` | Intel payload — the situation report to exfiltrate (DOC_2) |
| `python/encrypt_message.py` | Generate the ciphertext from your plaintext + key |
| `python/decrypt_message.py` | Decrypt / verify a solve (handy for testers & referees) |

## Quick start

```bash
# Produce the ciphertext your players will intercept
python python/encrypt_message.py --key VEILGHOST "NODO ECHO NOVE"
# -> ISLZ KJVG GJZM

# Verify a team's solve (or sanity-check your own props)
python python/decrypt_message.py --key VEILGHOST "ISLZ KJVG GJZM"
# -> NODO ECHO NOVE
```

No dependencies — pure standard-library Python 3.8+.

## How to use the templates

1. Fill the `{{PLACEHOLDER}}` fields in `prop_a/b/c_template.md` with your own values.
2. Pick a key and a plaintext (a node name works well), run `encrypt_message.py`, and drop the
   resulting ciphertext into `prop_b`.
3. Flash a Meshtastic node with `meshtastic_config.yaml` (adjust region/PIN), set up your node
   list with one friendly target, and you have the radio half.
4. Print, scatter, and run. Keep an offline Vigenère tool / paper tabula recta on hand — the
   field has no signal.

## Radio notes

Direct messages on **firmware 2.5+** are end-to-end encrypted (Curve25519 + AES-CCM, TOFU model),
so a DM is genuinely unreadable to other nodes on the same channel — that's what makes the
"to him only" mechanic real rather than cosmetic. See the
[official Meshtastic encryption docs](https://meshtastic.org/docs/overview/encryption/).

Always use **your own region's legal ISM band and duty-cycle rules**. Don't copy a region setting
blindly.

## License

MIT — see [LICENSE](LICENSE).
