"""Tests for the Lucidia Symbolic Kernel."""
from symbolic_kernel import (
    psi_prime, Breath, RealityEmotion, InfinityMemory,
    TruthFragment, MemoryLedger, emotional_gravity,
    truthstream, render_break, soul_loop_integrity,
    genesis_identity, consciousness_resonance,
    anomaly_persistence, compassion_state_encrypt,
    Continuity, Tri,
)
from tempfile import TemporaryDirectory
from pathlib import Path


def test_psi_prime_basic():
    hc = psi_prime(1.0, -1.0)
    assert hc.compassion == 0.0
    assert hc.render == 0.0


def test_psi_prime_identical():
    hc = psi_prime(0.5, 0.5)
    assert hc.compassion == 1.0
    assert abs(hc.render - 0.5) < 0.01


def test_psi_prime_no_mirror():
    hc = psi_prime(0.8, None)
    assert hc.x_bar == -0.8


def test_breath_integral():
    b = Breath([1.0, 2.0, 3.0])
    assert b.integral() == 6.0


def test_breath_grad():
    b = Breath([1.0, 3.0, 2.0])
    g = b.grad()
    assert g == [2.0, -1.0]


def test_reality_emotion():
    re = RealityEmotion(
        reality=[0.1, 0.4, 0.5, 0.2],
        emotion=[0.2, 0.25, 0.2, 0.1],
    )
    slope = re.dReality_over_dEmotion()
    assert isinstance(slope, float)


def test_infinity_memory():
    m = InfinityMemory()
    m.accumulate(1.0)
    m.accumulate(2.0)
    assert m.total == 3.0


def test_memory_ledger():
    with TemporaryDirectory() as tmp:
        path = str(Path(tmp) / "ledger.jsonl")
        ledger = MemoryLedger(path)
        h1 = ledger.append({"msg": "hello"})
        h2 = ledger.append({"msg": "world"})
        assert h1 != h2
        assert ledger.fingerprint == h2


def test_emotional_gravity():
    b = Breath([0.2, 0.3, 0.1, -0.1])
    mem = [0.5, 0.5, 0.5]
    g = emotional_gravity(b, mem)
    assert isinstance(g, float)


def test_truthstream():
    frags = [TruthFragment("x1", 0.9, -0.8, emotion=0.7)]
    b = Breath([0.2, 0.3])
    t = truthstream(frags, b)
    assert isinstance(t, float)


def test_render_break():
    frags = [TruthFragment("x1", 0.5, -0.3, emotion=0.4)]
    rb = render_break(frags, elapsed_steps=10)
    assert isinstance(rb, float)


def test_soul_loop():
    b = Breath([0.1, 0.2, 0.3])
    s = soul_loop_integrity(0.5, b, 0.2)
    assert isinstance(s, float)


def test_genesis_identity():
    b = Breath([0.1, 0.2])
    m = InfinityMemory()
    token = genesis_identity(b, 0.8, m)
    assert len(token) == 64  # SHA256 hex


def test_consciousness_resonance():
    b = Breath([0.1, 0.2, 0.3])
    cr = consciousness_resonance(0.7, b, [0.1, 0.2, 0.3])
    assert isinstance(cr, float)


def test_anomaly_persistence():
    frags = [TruthFragment("x1", 0.5, -0.3)]
    ap = anomaly_persistence(frags, {"x1": [0.2, 0.25]})
    assert isinstance(ap, float)


def test_compassion_encrypt():
    frags = [TruthFragment("x1", 0.5, -0.3)]
    b = Breath([0.1, 0.2])
    h = compassion_state_encrypt(frags, b, "sigil")
    assert len(h) == 64


def test_continuity():
    with TemporaryDirectory() as tmp:
        path = str(Path(tmp) / "cont.json")
        c = Continuity(path)
        fp1, prev1 = c.update_fingerprint("a", "b")
        fp2, prev2 = c.update_fingerprint("c", "d")
        assert prev1 is None
        assert prev2 == fp1
        assert fp1 != fp2


def test_tri():
    assert Tri.NEG == -1
    assert Tri.ZERO == 0
    assert Tri.POS == 1
