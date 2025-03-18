def generate_periodic_table():
    input_filename = "periodic_table.txt"
    output_filename = "periodic_table.html"

    NUM_COLS = 18

    elements = []
    with open(input_filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                name_part, props_part = line.split("=", 1)
            except ValueError:
                continue
            name = name_part.strip()
            props = {}
            for item in props_part.split(","):
                if ":" in item:
                    key, value = item.split(":", 1)
                    props[key.strip()] = value.strip()
            if (
                "position" in props
                and "number" in props
                and "small" in props
                and "molar" in props
            ):
                try:
                    pos = int(props["position"])
                    num = int(props["number"])
                except ValueError:
                    continue
                element = {
                    "name": name,
                    "position": pos,
                    "number": num,
                    "small": props["small"],
                    "molar": props["molar"],
                    "electron": props.get("electron", ""),
                }
                elements.append(element)

    rows = []
    current_row = [None] * NUM_COLS
    last_pos = -1
    for elem in elements:
        pos = elem["position"]
        if pos <= last_pos:
            rows.append(current_row)
            current_row = [None] * NUM_COLS
        if 0 <= pos < NUM_COLS:
            current_row[pos] = elem
        last_pos = pos
    if any(cell is not None for cell in current_row):
        rows.append(current_row)

    html_lines = []
    html_lines.append("<!DOCTYPE html>")
    html_lines.append("<html lang='en'>")
    html_lines.append("<head>")
    html_lines.append("<meta charset='utf-8'>")
    html_lines.append("<title>Periodic Table</title>")
    html_lines.append("</head>")
    html_lines.append("<body>")
    html_lines.append("<table>")

    for row in rows:
        html_lines.append("<tr>")
        for cell in row:
            if cell is None:
                html_lines.append(
                    '<td style="border: 1px solid black; padding:10px"></td>'
                )
            else:
                box = []
                box.append('<td style="border: 1px solid black; padding:10px">')
                box.append(f"<h4>{cell['name']}</h4>")
                box.append("<ul>")
                box.append(f"<li>No {cell['number']}</li>")
                box.append(f"<li>{cell['small']}</li>")
                box.append(f"<li>{cell['molar']}</li>")
                if cell["electron"]:
                    try:
                        e_value = int(cell["electron"].split()[0])
                        electron_label = "electron" if e_value == 1 else "electrons"
                    except ValueError:
                        electron_label = "electrons"
                    box.append(f"<li>{cell['electron']} {electron_label}</li>")
                box.append("</ul>")
                box.append("</td>")
                html_lines.append("\n".join(box))
        html_lines.append("</tr>")

    html_lines.append("</table>")
    html_lines.append("</body>")
    html_lines.append("</html>")

    with open(output_filename, "w") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    generate_periodic_table()
