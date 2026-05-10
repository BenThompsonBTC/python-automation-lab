from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from automation_lab.system_health import collect_system_health


def main() -> None:
    summary = collect_system_health()
    print("System health summary")
    print(f"OS: {summary.operating_system}")
    print(f"Python: {summary.python_version}")
    print(f"Machine: {summary.machine}")


if __name__ == "__main__":
    main()

