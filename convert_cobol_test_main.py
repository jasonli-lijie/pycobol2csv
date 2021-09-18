""" Convert COBOL ebcdic Binary File to CSV file. The CSV file is ready to be imported into database
based on python ebcdic library
Input: copybook + data file
CSV Convertion Configuration: csv_config.json
"""
# for copybook
import re

import sys
import argparse
import csv
import math
from array import array
import json
from pycobol2csv import convert_cobol_file

##### Main Route
if __name__ == "__main__":
    """Main function for COBOL file
    Args:
        copybook - copybook file
        data - ebcdic data file
        config - config json file, optional
    Returns:
        Exit code about Job status - success(0) or fail(-1)
    """
    parser = argparse.ArgumentParser(description="COBOL file conversion tool")
    parser.add_argument("--copybook", required=True, help="path to copybook file")
    parser.add_argument("--data", required=True, help="path to ebcdic data file")
    parser.add_argument("--output", required=True, help="path to output csv file")
    parser.add_argument(
        "--config", default="csv_config.json", help="[Optional] path to csv config file"
    )
    parser.add_argument(
        "--codepage", default="cp1140", help="[Optional] code page, default to cp1140"
    )

    args = parser.parse_args()
    print(args)
    convert_cobol_file(
        args.copybook, args.data, args.output, args.config, args.codepage
    )
