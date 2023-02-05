import util

file_path = "o.lua"

current_line = 1
lines = []

class Scotch:
    def write_app(self):
        global current_line
        c = str(input(f"[{current_line}]: "))

        if c.lower() == "stop":
            lines.clear()
            current_line = 1
            return
        elif c.lower() == "revert":
            util.get_previous(lines)
            with open(f"{file_path}", "w") as f:
                f.write("")
                f.writelines(lines)
                f.close()

                current_line -= 1
                self.write_app()
        else:
            with open(f"{file_path}", "w") as f:
                lines.append(c + "\n")
                f.write("")
                f.writelines(lines)
                f.close()

                current_line += 1
                self.write_app()

if __name__ == "__main__":
    app = Scotch()
    app.write_app()