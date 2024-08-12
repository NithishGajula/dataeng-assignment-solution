import os

class FileGeneratorError(Exception):
    pass

def generate_fixed_width_file(spec, data, file_path):
    if not spec or not data:
        raise FileGeneratorError("Invalid spec or data provided.")

    offsets = spec['Offsets']
    if len(offsets) != len(spec['ColumnNames']):
        raise FileGeneratorError("Offsets and ColumnNames lengths do not match.")

    encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader'].lower() == "true"

    try:
        with open(file_path, 'w', encoding=encoding) as fw_file:
            if include_header:
                header = ''.join([f"{col_name:<{offset}}" for col_name, offset in zip(spec['ColumnNames'], offsets)])
                fw_file.write(header + "\n")

            for row in data:
                line = ''.join([f"{field:<{offset}}" for field, offset in zip(row, offsets)])
                fw_file.write(line + "\n")
    except IOError as e:
        raise FileGeneratorError(f"Failed to write to file {file_path}: {e}")