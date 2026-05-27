"""JIS access-control gate — the README Quick Start examples, as runnable tests.

tibet-cortex is a JIS (multi-dimensional access-control) + zero-trust
knowledge-processing framework. JisGate.evaluate() decides whether a claim
(actor + clearance + role + department + geo) satisfies a policy — the
pre-access decision point, not a tool-call gate.

These tests reproduce the README examples verbatim so the documentation is
verifiable: pip install tibet-cortex && pytest.
"""
from tibet_cortex import JisClaim, JisPolicy, JisGate, JisDenialReason


def _ma_policy() -> JisPolicy:
    """The README's M&A document policy."""
    return JisPolicy(
        min_clearance=3,
        allowed_roles=["partner"],
        allowed_departments=["strategy"],
        allowed_geos=["NL", "DE", "FR"],
    )


def test_partner_is_allowed():
    """README example 1: partner with clearance 3, strategy, EU -> allowed."""
    claim = JisClaim(
        actor="partner@mckinsey.com",
        clearance=3,
        role="partner",
        department="strategy",
        geo=["NL", "DE"],
    )
    verdict = JisGate.evaluate(claim, _ma_policy())
    assert verdict.allowed is True
    assert verdict.denials == []


def test_intern_is_denied_with_reasons():
    """README example 2: intern, clearance 1 -> denied with multiple reasons."""
    intern = JisClaim(actor="intern@mckinsey.com", clearance=1, role="intern")
    verdict = JisGate.evaluate(intern, _ma_policy())
    assert verdict.allowed is False
    reasons = {d.reason for d in verdict.denials}
    assert JisDenialReason.CLEARANCE_TOO_LOW in reasons


def test_is_allowed_convenience_matches_evaluate():
    """JisGate.is_allowed() agrees with evaluate().allowed."""
    claim = JisClaim(actor="p@x.com", clearance=3, role="partner",
                     department="strategy", geo=["NL"])
    policy = _ma_policy()
    assert JisGate.is_allowed(claim, policy) == JisGate.evaluate(claim, policy).allowed


def test_public_policy_allows_anyone():
    """A public policy admits a minimal claim."""
    verdict = JisGate.evaluate(JisClaim(actor="anon", clearance=0, role="guest"),
                               JisPolicy.public())
    assert verdict.allowed is True
