"""Load server configurations into the database."""

from pathlib import Path
import json
import yaml

from db import SessionLocal
from models import Server


def load_file(path: Path) -> dict:
    """Load YAML or JSON server config."""
    if path.suffix.lower() in {".yaml", ".yml"}:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    elif path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported file type: {path}")


def main(directory: str = "servers") -> None:
    session = SessionLocal()
    for path in Path(directory).iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".yaml", ".yml", ".json"}:
            continue
        data = load_file(path)
        server = Server(**data)
        session.add(server)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
