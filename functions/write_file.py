import os

def write_file(working_directory, file_path, content):
    
    try:

        wd_abs = os.path.realpath(working_directory)
        target = os.path.realpath(os.path.join(wd_abs, file_path))

        if not target.startswith(wd_abs + os.sep) and target != wd_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
       
        if not os.path.exists(os.path.dirname(target)):
            new_dir = os.path.dirname(target)
            os.makedirs(new_dir, exist_ok=True)

        with open(target, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

