def print_out_help(lines: list):
    print(f"""
    Commands:
        stop - closes Scotch_CMD.
        revert - reverts the previous change.
        set_file_type_path - inputs a new file path.
        edit_line - prompts the user to change the current line.
        spec-usage - using this command will show the current spec usage of Scotch.
        config - Not added.
        ------------------------------------------------
        Lines: {str(len(lines))}
    """)