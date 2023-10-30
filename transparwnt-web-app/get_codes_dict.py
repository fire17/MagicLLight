import csv
from lang_data import data_csv
from io import StringIO
from pprint import pprint as pprint

def load_csv_string_to_dict(data_csv=data_csv, primary_key=None):
    data_dict = {}
    
    # Create a file-like object from the CSV string
    csv_string_io = StringIO(data_csv)

    reader = csv.DictReader(csv_string_io)
    fieldnames = reader.fieldnames

    # Use the first column as the primary key if not specified
    if primary_key is None:
        primary_key = fieldnames[0]

    for row in reader:
        key_value = row[primary_key]
        data_dict[key_value] = {primary_key:key_value,**{key: value for key, value in row.items() if key != ""}}

    return data_dict

# Usage example:

result = load_csv_string_to_dict(data_csv)
#pprint(result)

#print(":::")
#pprint([result[k] for k in result if "english_name" in result[k] and "Hebrew" in result[k]["english_name"]])
