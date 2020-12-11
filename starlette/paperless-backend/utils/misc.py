import json

def row2dict(row):
    data = {column: value for column, value in row.items()}
    dumped = json.dumps(data, indent=4, sort_keys=True, default=str)
    return json.loads(dumped)