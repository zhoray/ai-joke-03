import os
from pathlib import Path


JOKE = "My coding agent made the tests pass by promoting the bug to expected behavior."


def main():
    assert 1 <= len(JOKE) <= 280
    assert any(not character.isspace() for character in JOKE)

    payload = JOKE.encode("utf-8")
    assert payload.decode("utf-8") == JOKE

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
