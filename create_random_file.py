import os
import argparse


def create_random_file(filename: str, size_mb: int):
    size_bytes = size_mb * 1024 * 1024

    with open(filename, "wb") as f:
        f.write(os.urandom(size_bytes))


def main():
    parser = argparse.ArgumentParser(description="Create a file of random bytes.")
    parser.add_argument("-s", "--size", type=int, help="Size of the file in MB")
    parser.add_argument(
        "-o",
        "--output",
        default="random_file.bin",
        help="Output filename (default: random_file.bin)",
    )

    args = parser.parse_args()

    create_random_file(args.output, args.size)

    file_size = os.path.getsize(args.output)
    print(f"File '{args.output}' created.")
    print(f"File size: {file_size / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    main()
