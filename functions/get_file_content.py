import os
from functions.config import MAX_CHARS
from google.genai import types

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
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Prints the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory.",
            ),
        },
    ),
)