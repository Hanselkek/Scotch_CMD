FILE_PATH = "o.lua"

current_line = 1
lines = []

class Scotch:
    def write_app(self):
        global current_line
        c = str(input(f"[{current_line}]: "))

        if c.lower() != "stop":
            with open(f"{FILE_PATH}", "w") as f:
                lines.append(c + "\n")
                f.write("")
                f.writelines(lines)
                f.close()

                current_line += 1
                self.write_app()
        else:
            lines.clear()
            current_line = 1 # Probably unneeded to be honest.
            return

if __name__ == "__main__":
    app = Scotch()
    app.write_app()