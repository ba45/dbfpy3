import argparse
import csv

from dbfpy3.dbf import Dbf


def process(input_filename: str, output_filename: str):
    with open(output_filename, encoding="utf-8", mode="w") as output_file, \
            Dbf(input_filename) as dbf:
        csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(dbf.fieldNames)
        csv_writer.writerow(dbf.fieldNames)
        n = len(dbf.fieldNames)
        for rec in dbf:
            assert len(rec.fieldData) == n
            print(rec.fieldData)
            csv_writer.writerow(rec.fieldData)
    assert dbf.closed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str, required=True, help="Source .dbf file")
    parser.add_argument('-o', '--output-file', type=str, required=True, help="Target .csv file")
    args = parser.parse_args()

    process(args.input_file, args.output_file)
