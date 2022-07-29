import os
def search(file, folder):
    assert os.path.isdir(folder)
    current_path, directories, files = os.walk(folder).__next__()
    if file in files:
        return os.path.join(folder, file)
    elif directories == '':
        return None
    else:
        for new_directory in directories:
            result = search(folder = os.path.join(folder, new_directory), file = file)
            if result:
                return result
        return None