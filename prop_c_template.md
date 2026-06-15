# PROP C — Intel payload (DOC_2)

The situation report the players must **exfiltrate** — as a direct message to the one friendly
node, never broadcast. Keep it short and structured: LoRa bandwidth is tiny, and a short payload
is referee-verifiable in seconds.

> Sanitized template. Replace `{{...}}` with your own values. Keep it to ~3 facts. Include one
> coordinate **and** make sure a decoy prop carries a *similar-but-wrong* coordinate — that near-
> miss is the nastiest, fairest trap in the design.

---

```
================================================================
  SITREP — {{CLASSIFICATION}}     (transmit to friendly node ONLY)
================================================================
  1. {{FACT_1}}     e.g. unit ALPHA repositioned NW
  2. {{FACT_2}}     e.g. anti-air emplacement ACTIVE
  3. {{FACT_3}}     e.g. logistics depot at {{COORD}}  (short grid ref)
================================================================
```

Recommended DM payload (what a correct solve actually sends):

```
{{SHORT_PAYLOAD}}     e.g. ALPHA->NW; AA-BATTERY ACTIVE; DEPOT 33T-REDACTED
```

---

### Design notes (remove before printing)

- This is the only payload that scores full marks. A team that transmits the **decoy** coordinate
  (from the patrol-route decoy prop) scores partial — by design.
- Hide PROP C separately from PROP B so finding the key material and finding the payload are
  distinct search acts.
- The referee check is binary: did the DM go to the correct node, and did it carry these facts?
