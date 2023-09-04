# this code aims to provide a method for converting yomichan dictionaries to mdict format

import json

def identify_entries_with_strings(json_data):
    try:
        data = json.loads(json_data)
        matching_entries = [entry for entry in data if isinstance(entry, list) and len(entry) >= 2 and all(isinstance(item, str) for item in entry[:2])]
        return matching_entries
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

# Example usage:
json_data = '[["護謨","ゴム","n col uk","",15,["Apagador, Borracha"],1054570,"ateji"], ... ]'
matching_entries = identify_entries_with_strings(json_data)
print(matching_entries)
