"""
TIBET Cortex — Zero-trust AI knowledge processing

JIS-gated vector storage, Airlock-protected inference, TIBET-audited provenance.
Data that protects itself.

Usage:
    from cortex import JisClaim, JisPolicy, JisGate, CortexStore, TibetToken

    # Ingest with JIS gating
    store = CortexStore()
    store.ingest("doc_001", embedding, content, jis_level=2)

    # Search with identity claim
    claim = JisClaim(actor="analyst@company.com", clearance=2, role="analyst")
    result = store.search(query_embedding, claim, top_k=5)

    # Sign tokens with Ed25519
    from tibet_cortex.token import generate_keypair
    private_key, public_key = generate_keypair()
    token = TibetToken.create(erin="sha256:...", erachter="query", actor="user", jis_level=2)
    token.sign(private_key)
    assert token.verify_signature(public_key)
"""

__version__ = "0.2.0"

from tibet_cortex.jis import JisClaim, JisPolicy, JisGate, JisVerdict, JisDenialReason
from tibet_cortex.envelope import Envelope, EnvelopeBlock, BlockType
from tibet_cortex.audit import AuditTrail, AuditEntry
from tibet_cortex.airlock import Airlock, AirlockSession
from tibet_cortex.token import TibetToken, Provenance, Eromheen, content_hash, generate_keypair
from tibet_cortex.store import CortexStore, SearchResult, SearchHit

__all__ = [
    "JisClaim", "JisPolicy", "JisGate", "JisVerdict", "JisDenialReason",
    "Envelope", "EnvelopeBlock", "BlockType",
    "AuditTrail", "AuditEntry",
    "Airlock", "AirlockSession",
    "TibetToken", "Provenance", "Eromheen", "content_hash", "generate_keypair",
    "CortexStore", "SearchResult", "SearchHit",
]
