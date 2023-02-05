FILE_PATH = "o.lua"

class Scotch:
    def __init__(self, current_line=1, lines=[]):
        self.current_line = current_line
        self.lines = lines

    def write_app(self):
        c = str(input(f"[{self.current_line}]: "))

        if c.lower() != "stop":
            with open(f"{FILE_PATH}", "w") as f:
                self.lines.append(c + "\n")
                f.write("")
                f.writelines(self.lines)
                f.close()

                current_line += 1
                self.write_up()
        else:
            self.lines.clear()
            self.current_line = 1 # Probably unneeded to be honest.
            return

if __name__ == "__main__":
    app = Scotch()
    app.write_app()