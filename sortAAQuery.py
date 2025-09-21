import json

def sort_queries_by_depart_date(json_file):
    # Load JSON data
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ensure "queries" exists and is a list
    if "queries" in data and isinstance(data["queries"], list):
        data["queries"].sort(
            key=lambda q: q.get("DepartDate", ["9999-12-31"])[0]
        )

    # Overwrite original file
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    path = "AASearchQuery.json"
    sort_queries_by_depart_date(path)
    print(f"Sorted queries saved back to {path}")
