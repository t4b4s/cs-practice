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
