import util
import os
import print_out_help

file_path = "o.lua"

current_line = 1
lines = []

class Scotch:
    def write_app(self):
        global current_line
        global file_path

        c = str(input(f"[{current_line}]: "))

        if c.lower() == "stop":
            lines.clear()
            current_line = 1
            return
        elif c.lower() == "revert":
            util.set_previous(lines)
            with open(f"{file_path}", "w") as f:
                f.write("")
                f.writelines(lines)
                f.close()

                current_line -= 1
                self.write_app()
        elif c.lower() == "set_file_type_path":
            new_file_path = str(input("New file path: "))
            if os.path.exists(new_file_path):
                file_path = new_file_path
                self.write_app()
            else:
                print("Unable to open file path. Going back to previous command.")
                self.write_app()
        elif c.lower() == "edit_line":
            t_line = int(input("Go to line: "))
            try:
                if lines[t_line - 1] != None:
                    edited_str = str(input("New Content: "))
                    lines[t_line - 1] = edited_str 
                    with open(f"{file_path}", "w") as f:
                        f.write("")
                        f.writelines(lines)
                        f.close()

                        self.write_app()
            except:
                print("Line does not exist on the list. Going back to previous command.")
                self.write_app()
        elif c.lower() == "help":
            print_out_help.print_out_help()
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