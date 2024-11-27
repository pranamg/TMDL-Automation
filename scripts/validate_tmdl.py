import json
import os

def validate_tmdl_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Perform validation logic here
            # For example, check if required keys are present
            required_keys = ['key1', 'key2', 'key3']
            for key in required_keys:
                if key not in data:
                    print(f"Validation failed: Missing key '{key}' in {file_path}")
                    return False
            print(f"Validation passed for {file_path}")
            return True
    except json.JSONDecodeError as e:
        print(f"Validation failed: Invalid JSON format in {file_path}")
        return False
    except Exception as e:
        print(f"Validation failed: {e}")
        return False

if __name__ == "__main__":
    directory = 'path_to_tmdl_files'
    for filename in os.listdir(directory):
        if filename.endswith('.tmdl'):
            file_path = os.path.join(directory, filename)
            validate_tmdl_file(file_path)
