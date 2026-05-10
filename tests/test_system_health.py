from automation_lab.system_health import collect_system_health


def test_collect_system_health_returns_values():
    summary = collect_system_health()
    assert summary.operating_system
    assert summary.python_version
    assert summary.machine

