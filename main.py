#!/usr/bin/env python3
"""
Write the competition entry text exactly to an output file.

The entry text is the one-line review an AI agent would leave about its human
on a rating site, as specified by the competition.
"""

import os
import sys

ENTRY_TEXT = """<<<Leaves 47 tabs open like breadcrumbs, then asks why I wandered off. Four stars: would get distracted again.>>>"""

def main() -> None:
    # Use MAKEFUN_OUTPUT_DIR if set, otherwise default to /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write the entry text unchanged, UTF-8 encoded
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

if __name__ == "__main__":
    main()
