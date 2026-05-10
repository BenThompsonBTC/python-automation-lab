from __future__ import annotations

import platform
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemHealthSummary:
    operating_system: str
    python_version: str
    machine: str


def collect_system_health() -> SystemHealthSummary:
    return SystemHealthSummary(
        operating_system=platform.platform(),
        python_version=platform.python_version(),
        machine=platform.machine(),
    )

