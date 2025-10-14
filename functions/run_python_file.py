import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    
    try:
        
        wd_abs = os.path.realpath(working_directory)
        target = os.path.realpath(os.path.join(wd_abs, file_path))

        if not target.startswith(wd_abs + os.sep) and target != wd_abs:   
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target):
            return f'Error: File "{file_path}" not found.'
        
        if not target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        called_program = ["python3", file_path] + args
        
        result = subprocess.run(args=called_program, timeout=30, capture_output=True, check=False, cwd=wd_abs, text=True)
        
        parts = []
        if result.stdout:
            parts.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            parts.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")
        if not parts:
            return 'No output produced.'
        
        return "\n".join(parts)


    except Exception as e:
        return f"Error: executing Python file: {e}"
    
