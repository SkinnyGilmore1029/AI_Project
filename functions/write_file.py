import os

def write_file(working_directory,file_path,content):
    # makes sure the file is within the working directory
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        directory_name = os.path.dirname(abs_file_path)
        if directory_name:
            os.makedirs(directory_name, exist_ok=True)
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"