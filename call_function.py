from google.genai import types
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

function_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(function_call_part, verbose=False):
    kwargs_dict = {**function_call_part.args, "working_directory": "./calculator"}
    function_name = function_call_part.name
    func_args = function_call_part.args.copy()

    if function_name not in function_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )       

    if verbose == False:
        print(f" - Calling function: {function_name}")
    else:
        print(f" - Calling function: {function_name}({func_args})")
    
    function_result = function_dict[function_name](**kwargs_dict)
    
    return types.Content(
    role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

    

