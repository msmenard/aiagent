import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    
    try:

        wd_abs = os.path.realpath(working_directory)
        target = os.path.realpath(os.path.join(wd_abs, file_path))

        if not target.startswith(wd_abs + os.sep) and target != wd_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        

        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string = f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"
    

# print(get_file_content("calculator", "main.py"))