import csv
import os

class FileParserError(Exception):
    pass

def parse_fixed_width_to_csv(spec, input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Fixed-width file not found: {input_file_path}")

    offsets = spec['Offsets']
    encoding = spec['FixedWidthEncoding']
    delimiter = ','

    def fixed_width_file_reader(file_path, offsets, encoding):
        with open(file_path, 'r', encoding=encoding) as fw_file:
            for line in fw_file:
                row = []
                position = 0
                for offset in offsets:
                    field = line[position:position + int(offset)].strip()
                    row.append(field)
                    position += int(offset)
                yield row

    try:
        with open(output_file_path, 'w', newline='', encoding=spec['DelimitedEncoding']) as csv_file:
            writer = csv.writer(csv_file, delimiter=delimiter)
            for row in fixed_width_file_reader(input_file_path, offsets, encoding):
                writer.writerow(row)
    except IOError as e:
        raise FileParserError(f"Failed to read/write file: {e}")
