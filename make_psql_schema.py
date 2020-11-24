import argparse

from dbfpy3.dbf import Dbf


def process(input_filename: str):
    schema = []

    # See https://devzone.advantagedatabase.com/dz/webhelp/Advantage9.0/server1/dbf_field_types_and_specifications.htm
    # http://www.dbase.com/KnowledgeBase/int/db7_file_fmt.htm see Storage of dBASE Data Types
    with Dbf(input_filename) as dbf:
        for fieldDef in dbf.fieldDefs:
            type_code = fieldDef.typeCode
            if type_code == "N":
                type = "int"
            elif type_code == "C":
                type = f"varchar({fieldDef.length})"
            elif type_code == "F":
                type = "real"
            elif type_code == "D":
                type = "text"
            else:
                raise NotImplementedError(type_code)
            schema.append(f"{fieldDef.name} {type}")
        print(",\n".join(schema))
    assert dbf.closed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str, required=True, help="Source .dbf file")
    args = parser.parse_args()

    process(args.input_file)
