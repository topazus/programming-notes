#!/usr/bin/env python

import os
import argparse


def walk_dir(dir_path: str, is_size: bool, is_verbose: bool) -> None:
    info = {
        "files-count": 0,
        "total-size": 0,
        "files": [],
    }
    for root, dirs, files in os.walk(dir_path):
        if is_size & is_verbose:
            info["files-count"] += len(files)
            for f in files:
                path = os.path.join(root, f)
                info["total-size"] += os.path.getsize(path)
                info["files"].append(path)

        elif is_verbose:
            info["files-count"] += len(files)
            for f in files:
                path = os.path.join(root, f)
                info["files"].append(path)
        elif is_size:
            info["files-count"] += len(files)
            for f in files:
                path = os.path.join(root, f)
                info["total-size"] += os.path.getsize(path)
        else:
            info["files-count"] += len(files)

    print(
        f"""in {dir_path} directory:
    {info["files-count"]} files"""
    )
    if is_size:
        print(f'total size: {info["total-size"]} bytes')
    if is_verbose:
        print(f'files: {info["files"]}')


def main():
    parser = argparse.ArgumentParser(description="count files in the given directory")
    parser.add_argument(
        "-s",
        "--size",
        help="count size of all files",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-v", "--verbose", help="show all files", action="store_true", default=False
    )
    parser.add_argument(
        "-d", "--dir", help="path to directory", default=["."], nargs="+"
    )
    args = parser.parse_args()

    for dir_name in args.dir:
        if os.path.isdir(dir_name):
            walk_dir(dir_name, args.size, args.verbose)
        else:
            print(f"{dir_name} is not a directory")


if __name__ == "__main__":
    main()
