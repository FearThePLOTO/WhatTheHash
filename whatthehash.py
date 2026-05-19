"""
WhatTheHash - Hash Identifier Tool
Identifies common hash types from their string representation
"""

import re
import sys
import argparse

BANNER = """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║          ██╗    ██╗ █████╗ ██╗  ██╗███████╗            ║
║          ██║    ██║██╔══██╗██║  ██║██╔════╝            ║
║          ██║ █╗ ██║███████║███████║███████╗            ║
║          ██║███╗██║██╔══██║██╔══██║╚════██║            ║
║          ╚███╔███╝ ██║  ██║██║  ██║███████║            ║
║           ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝            ║
║                                                        ║
║            WHAT THE HASH - Hash Identifier             ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""

HASHES = {
    "CRC32": r"^[a-f0-9]{8}$",
    "MD4": r"^[a-f0-9]{32}$",
    "MD5": r"^[a-f0-9]{32}$",
    "NTLM": r"^[a-f0-9]{32}$",
    "RipeMD-128": r"^[a-f0-9]{32}$",
    "Haval-128": r"^[a-f0-9]{32}$",
    "Tiger-128": r"^[a-f0-9]{32}$",
    "MySQL323": r"^[a-f0-9]{16}$",
    "DES (Unix)": r"^[a-zA-Z0-9./]{13}$",
    "SHA1": r"^[a-f0-9]{40}$",
    "RipeMD-160": r"^[a-f0-9]{40}$",
    "Tiger-160": r"^[a-f0-9]{40}$",
    "Haval-160": r"^[a-f0-9]{40}$",
    "MySQL5": r"^\*[a-f0-9]{40}$",
    "SHA224": r"^[a-f0-9]{56}$",
    "Haval-192": r"^[a-f0-9]{48}$",
    "Tiger-192": r"^[a-f0-9]{48}$",
    "SHA256": r"^[a-f0-9]{64}$",
    "Haval-224": r"^[a-f0-9]{56}$",
    "SHA384": r"^[a-f0-9]{96}$",
    "SHA512": r"^[a-f0-9]{128}$",
    "Whirlpool": r"^[a-f0-9]{128}$",
    "GOST": r"^[a-f0-9]{64}$",
    "Bcrypt": r"^\$2[aby]\$\d{2}\$[a-zA-Z0-9./]{53}$",
    "MD5crypt": r"^\$1\$[a-zA-Z0-9./]{1,8}\$[a-zA-Z0-9./]{22}$",
    "SHA256crypt": r"^\$5\$[a-zA-Z0-9./]{1,16}\$[a-zA-Z0-9./]{43}$",
    "SHA512crypt": r"^\$6\$[a-zA-Z0-9./]{1,16}\$[a-zA-Z0-9./]{86}$",
    "BSDi Extended DES": r"^_[a-zA-Z0-9./]{19}$",
    "Scrypt": r"^\$7\$[a-zA-Z0-9./]+$",
    "Argon2": r"^\$argon2[id]{1}\$v=\d+\$m=\d+,t=\d+,p=\d+\$[a-zA-Z0-9+/]+\$[a-zA-Z0-9+/]+$",
    "PBKDF2": r"^\$pbkdf2[-_a-zA-Z0-9]{0,}\$[a-zA-Z0-9]+\$[a-zA-Z0-9+/]+$",
}


def identify_hash(za_hash):
    za_hash = za_hash.lower().strip()
    matches = []

    for name, pattern in HASHES.items():
        if re.match(pattern, za_hash):
            matches.append(name)

    return matches


def print_banner():
    print(BANNER)


def format_result(za_hash, matches):
    print(f"\n{'=' * 60}")
    print(f"Hash Input: {za_hash[:60]}{'...' if len(za_hash) > 60 else ''}")
    print(f"Hash Length: {len(za_hash)} characters")
    print(f"{'=' * 60}\n")

    if not matches:
        print("No matching hash types found!")
        return

    print(f"Possible hash types:")
    for name in matches:
        print(f"  - {name}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="whatthehash",
        description="Identify common hash types from their string representation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  whatthehash -s 5d41402abc4b2a76b9719d911017c592
  whatthehash --hash 356a192b7913b04c54574d18c28d46e6395428ab
        """,
    )

    parser.add_argument("-s", "--string", type=str, help="The hash string to identify")
    parser.add_argument(
        "--hash",
        type=str,
        dest="hash_string",
        help="Alternative flag for hash input (same as -s)",
    )

    parser.add_argument(
        "--no-banner", action="store_true", help="Don't print the banner"
    )

    args = parser.parse_args()

    if not args.no_banner:
        print_banner()

    hash_input = args.string or args.hash_string

    if not hash_input:
        parser.print_help()
        sys.exit(1)

    matches = identify_hash(hash_input)
    format_result(hash_input, matches)


if __name__ == "__main__":
    main()
