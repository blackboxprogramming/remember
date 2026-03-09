from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from lucidia.contradiction_log import ContradictionLog


class ContradictionLogTest(TestCase):
    def test_append_and_read_all(self) -> None:
        with TemporaryDirectory() as tmp:
            log_path = Path(tmp) / "logs" / "contradictions.jsonl"
            log = ContradictionLog(str(log_path))

            with patch("lucidia.contradiction_log.time.time", side_effect=[1000.0, 1001.5]):
                log.append("prompt-one", "reply-one")
                log.append("prompt-two", "reply-two")

            entries = log.read_all()
            self.assertEqual(len(entries), 2)
            self.assertEqual(entries[0].prompt, "prompt-one")
            self.assertEqual(entries[1].reply, "reply-two")
            self.assertEqual(entries[0].timestamp, 1000.0)
            self.assertEqual(entries[1].timestamp, 1001.5)

    def test_summary_and_latest(self) -> None:
        with TemporaryDirectory() as tmp:
            log = ContradictionLog(str(Path(tmp) / "nested" / "log.jsonl"))

            with patch("lucidia.contradiction_log.time.time", side_effect=[42.0, 84.0]):
                log.append("a", "b")
                log.append("c", "d")

            summary = log.summary()
            self.assertEqual(summary["count"], 2)
            self.assertEqual(summary["oldest_ts"], 42.0)
            self.assertEqual(summary["newest_ts"], 84.0)

            latest = log.latest()
            assert latest is not None
            self.assertEqual(latest.prompt, "c")
            self.assertEqual(latest.reply, "d")

