#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

SUPPORTED_EXTENSIONS = [".py", ".cpp", ".h", ".hpp", ".go"]
OUTPUT_DIR = Path.home() / "Desktop"

def find_repo_root(path: Path) -> Path:
    try:
        from subprocess import check_output
        root = check_output(["git", "-C", str(path), "rev-parse", "--show-toplevel"], text=True).strip()
        return Path(root)
    except Exception:
        return path.resolve()

def collect_source_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*") if p.suffix in SUPPORTED_EXTENSIONS and p.is_file()])

def write_combined_file(files: list[Path], root: Path, output_path: Path):
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("# ===== DIRECTORY LISTING OF SOURCE FILES =====\n")
        for f in files:
            out.write(f"{f.relative_to(root)}\n")
        out.write("\n# ===== BEGIN CONCATENATED SOURCE FILES =====\n\n")
        for f in files:
            out.write(f"\n#################### FILE: {f.relative_to(root)} ####################\n\n")
            try:
                out.write(f.read_text(encoding='utf-8', errors='replace'))
            except Exception as e:
                out.write(f"<< Failed to read file: {e} >>\n")

def main():
    parser = argparse.ArgumentParser(description="Package source code files from a project into one file for LLMs.")
    parser.add_argument(
        "--local",
        action="store_true",
        help="Only include files from the current directory and subdirectories (not the entire Git repo).",
    )
    args = parser.parse_args()

    start_path = Path.cwd()
    root = start_path if args.local else find_repo_root(start_path)
    repo_name = root.name
    output_file = OUTPUT_DIR / f"{repo_name}.llm.txt"

    files = collect_source_files(root)
    if not files:
        print("❌ No source files found.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_combined_file(files, root, output_file)
    print(f"✅ Output written to: {output_file}")

if __name__ == "__main__":
    main()
