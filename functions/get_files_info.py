import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    try:
        wd_abs = os.path.realpath(working_directory)
        target = os.path.realpath(os.path.join(wd_abs, directory))
    
        if not target.startswith(wd_abs + os.sep) and target != wd_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(target)
        listed_content_info = []
        for item in contents:
            file_size = os.path.getsize(os.path.join(target, item))
            is_dir = os.path.isdir(os.path.join(target, item))
            item_info = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            listed_content_info.append(item_info)
        return "\n".join(listed_content_info)
            
    except Exception as e:
        return f"Error: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
