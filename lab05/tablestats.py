def read_rows(lines):
    rows=[]
    header=None
    for line in lines:
        line=line.strip()
        if not line: continue
        fields = [f.strip() for f in line.split(",")]
        if header is None:
            header=fields
            continue
        if len(fields) != len(header):
            continue

        row = dict(zip(header,fields))
        rows.append(row)
        
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind is not None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row.get("тип") == kind:
            value = row.get("минуты", "").replace(",", ".")
            try:
                total += float(value)
            except ValueError:
                continue
    return round(total, 1)


def to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
    
