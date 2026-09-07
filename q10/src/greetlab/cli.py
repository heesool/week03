import argparse


def non_whitespace_name(value):
    if not value.strip():
        raise argparse.ArgumentTypeError("name must contain non-whitespace characters")
    return value


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True, type=non_whitespace_name)
    a = p.parse_args()
    print(f"Hello, {a.name}!")

if __name__ == "__main__":
    main()
