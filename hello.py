"""GitHub push test - a minimal Python module."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet())
    print(greet("GitHub"))


if __name__ == "__main__":
    main()
