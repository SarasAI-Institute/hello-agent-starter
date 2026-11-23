"""A tiny greeting application for the first agent setup session."""
import argparse


def greet(name: str) -> str:
    """Greet a trimmed name, defaulting to World for blank input."""
    return f"Hello, {name.strip() or 'World'}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="A small app for your first coding-agent session.")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
