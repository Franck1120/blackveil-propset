# PROP B — Technical log (DOC_1)

The "captured enemy device log." This is where the **key value**, the **BT PIN**, the **node
table**, and the **intercepted ciphertext** all hide in plain sight, mixed with plausible
technical noise. Format it as a monospace dump for immersion.

> Sanitized template. Replace `{{...}}` with your own values. The art here is camouflage: the
> operative code should sit between a firmware version and a pairing code so it doesn't scream
> "I am the key."

---

```
================================================================
  {{UNIT_TAG}}  FIELD COMMS LOG  —  device {{DEVICE_ID}}
================================================================
  firmware ............. {{FW_VERSION}}        e.g. 2.5.x
  BT pairing PIN ....... {{BT_PIN}}            e.g. 868477   (-> used to connect)
  operative code ....... {{OPERATIVE_CODE}}    e.g. VEILGHOST (-> THIS is the cipher key)
  band ................. {{ISM_BAND}}          e.g. 868 MHz

  ---- authorized node list ----
  {{NODE_1}}    {{NODE_2}}    {{NODE_3}}    {{NODE_4}}
       e.g. SIGMA-CMD   SIGMA-RELAY   SIGMA-3   GHOST-4

  [!] anomaly: unauthorized node detected on the network,
      transmitting at irregular intervals — DO NOT RESPOND.
      ( id: {{INFILTRATOR_NODE}}  e.g. ECHO-9 )    <-- the double bluff

  ---- intercepted transmission (undeciphered) ----
  {{CIPHERTEXT}}                                e.g. ISLZ KJVG GJZM
================================================================
```

---

### Design notes (remove before printing)

- `{{OPERATIVE_CODE}}` is the Vigenère key. Generate the matching `{{CIPHERTEXT}}` with
  `python/encrypt_message.py --key {{OPERATIVE_CODE}} "{{PLAINTEXT}}"`.
- The **anomaly line is a double bluff**: the in-fiction "do not respond" node is exactly the
  friendly infiltrator the players must DM. The decrypted plaintext confirms it.
- Add 1–2 fake fields (sequence numbers, voltages) to thicken the camouflage around the real key.
