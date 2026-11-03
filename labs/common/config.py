"""Shared settings for all labs: reads labs/.env, picks the model, builds the API client."""
import os
from pathlib import Path

LABS_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = LABS_DIR / "data"


def _load_dotenv(path: Path) -> None:
    """Tiny .env reader (KEY=VALUE lines, # comments) so we don't need python-dotenv."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        # A variable already set in the shell wins over the file
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


_load_dotenv(LABS_DIR / ".env")

# Haiku keeps lab cost low. Set CCAR_MODEL in .env to try another model.
MODEL = os.environ.get("CCAR_MODEL", "claude-haiku-5-5")
# Haiku 5.5 thinks by default and thinking counts toward max_tokens, so leave room.
MAX_TOKENS = 8000


def get_client():
    """Messages API client. Imported lazily so fake_db works without the SDK installed."""
    import anthropic

    return anthropic.Anthropic()
