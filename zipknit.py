#!/usr/bin/env python3
"""Extract every ZIP file in a folder into one output folder."""

import argparse
import sys
import zipfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="folder containing the .zip files")
    parser.add_argument("output", type=Path, nargs="?", default=Path("output"),
                        help="destination folder (default: ./output)")
    args = parser.parse_args()

    if not args.source.is_dir():
        sys.exit(f"Error: '{args.source}' is not a folder.")

    zip_paths = sorted(args.source.glob("*.zip"))
    if not zip_paths:
        sys.exit(f"No .zip files found in '{args.source}'.")

    output = args.output.resolve()
    print(f"Found {len(zip_paths)} ZIP files in '{args.source}':")
    for path in zip_paths:
        print(f"  - {path.name}")
    print(f"\nOutput folder: {output}")
    if input("Proceed with extraction? [y/N] ").strip().lower() != "y":
        print("Cancelled.")
        return

    output.mkdir(parents=True, exist_ok=True)
    extracted = skipped = 0

    for zip_path in zip_paths:
        print(f"\nExtracting: {zip_path.name}")
        try:
            with zipfile.ZipFile(zip_path) as archive:
                for member in archive.infolist():
                    target = (output / member.filename).resolve()
                    if not target.is_relative_to(output):
                        print(f"  [skip, unsafe path] {member.filename}")
                        skipped += 1
                    elif member.is_dir():
                        target.mkdir(parents=True, exist_ok=True)
                    elif target.exists():
                        print(f"  [skip, already exists] {member.filename}")
                        skipped += 1
                    else:
                        archive.extract(member, output)
                        extracted += 1
        except zipfile.BadZipFile:
            print(f"  WARNING: '{zip_path.name}' is not a valid ZIP, skipped.")

    print("\nExtraction complete.")
    print(f"  Files extracted : {extracted}")
    print(f"  Files skipped   : {skipped}")
    print(f"  Output          : {output}")


if __name__ == "__main__":
    main()
