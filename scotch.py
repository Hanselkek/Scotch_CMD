FILE_PATH = "o.lua"

current_line = 1
lines = []

def write_up():
    global current_line

    c = str(input(f"[{current_line}]: "))

    if c.lower() != "stop":
        with open(f"{FILE_PATH}", "w") as f:
            lines.append(c + "\n")
            f.write("")
            f.writelines(lines)
            f.close()

            current_line += 1
            write_up()
    else:
        lines.clear()
        current_line = 1 # Probably uneeded to be honest.
        return

write_up()