import os

def resolve_dataset(dataset_path, functionToApply):
    # List all files in the folder
    for filename in os.listdir(dataset_path):
        # Generate the full file path
        file_path = os.path.join(dataset_path, filename)
        print(filename)
        # Ensure it's a file (not a directory)
        if os.path.isfile(file_path):
            splitted_file_name = filename.split('.')
            if splitted_file_name[1] == 'in':
                print(f"Processing file: {file_path}")
                with open(file_path, 'r') as file:
                    # Perform your file operations (e.g., read the file)
                    solvedContent = functionToApply(file_path)
                    resolvedFileName = dataset_path + "\\" + splitted_file_name[0] + ".txt"
                    with open(resolvedFileName, 'w') as file:
                        file.write(solvedContent)
