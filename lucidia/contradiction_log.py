"""Contradiction log for Lucidia.

This module provides a basic interface to record instances where the system's response
contradicts prior outputs or expected truths. Each log entry includes a timestamp,
the user prompt, and the assistant's reply.
The intent is to build a transparent record for later analysis.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional


@dataclass
class ContradictionEntry:
    timestamp: float
    prompt: str
    reply: str


class ContradictionLog:
    def __init__(self, path: str = "contradiction_log.jsonl") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, prompt: str, reply: str) -> None:
        entry = ContradictionEntry(time.time(), prompt, reply)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(entry)) + "\n")

    def read_all(self) -> List[ContradictionEntry]:
        entries: List[ContradictionEntry] = []
        try:
            with self.path.open("r", encoding="utf-8") as f:
                for line in f:
                    data = json.loads(line.strip())
                    entries.append(ContradictionEntry(**data))
        except FileNotFoundError:
            pass
        return entries

    def to_dicts(self) -> List[dict]:
        """Return log entries as dictionaries for serialization or inspection."""
        return [asdict(entry) for entry in self.read_all()]

    def latest(self) -> Optional[ContradictionEntry]:
        """Return the most recent log entry if available."""
        entries = self.read_all()
        return entries[-1] if entries else None

    def summary(self) -> dict:
        """Provide a small summary about the log contents."""
        entries = self.read_all()
        return {
            "count": len(entries),
            "oldest_ts": entries[0].timestamp if entries else None,
            "newest_ts": entries[-1].timestamp if entries else None,
        }

    def __len__(self) -> int:  # pragma: no cover - simple delegation
        return len(self.read_all())


if __name__ == "__main__":
    # Example usage:
    log = ContradictionLog()
    log.append("Example prompt", "Example contradictory reply")
    for e in log.read_all():
        print(e)
