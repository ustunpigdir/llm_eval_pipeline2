# Large Numeric Failure Manual Audit Packet v1

This packet turns the large numeric failure report into human-readable audit cards for candidate logical gates.

Source report: `outputs/large_numeric_failure_gt100pct_v1/`.

Read `LARGE_NUMERIC_FAILURE_MANUAL_AUDIT_PACKET.md` first, then inspect individual gate files. Use `gate_audit_cards.csv` or `.json` if you want to record manual decisions programmatically.

No deterministic labels were changed. No raw outputs, frozen metrics, or database contents were modified.

Rerun with:

```bash
.venv/bin/python scripts/build_large_numeric_failure_manual_audit_packet_v1.py
```
