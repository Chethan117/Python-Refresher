import os
import re
import shutil

def find_sas_files_and_versions(directory):
    """Find .sas files in a directory, including versions."""
    sas_files = {}
    for file in os.listdir(directory):
        if file.endswith('.sas'):
            base_name = re.sub(r'V\d+', '', file, flags=re.IGNORECASE).lower()
            version = re.findall(r'V(\d+)', file, flags=re.IGNORECASE)
            version = int(version[0]) if version else 0
            full_path = os.path.join(directory, file)
            if base_name not in sas_files or sas_files[base_name][1] < version:
                sas_files[base_name] = (full_path, version)
    return sas_files

def retain_highest_version_sas_and_handoverdoc(main_directory):
    for main_subdir in next(os.walk(main_directory))[1]:
        main_subdir_path = os.path.join(main_directory, main_subdir)
        sas_files = find_sas_files_and_versions(main_subdir_path)
        
        # If no .sas files in the main subdirectory, check its subdirectories
        if not sas_files:
            for root, dirs, files in os.walk(main_subdir_path, topdown=True):
                sas_files.update(find_sas_files_and_versions(root))
        
        highest_version_files = [file_info[0] for file_info in sas_files.values()]
        handover_docs = [os.path.join(main_subdir_path, file) for file in os.listdir(main_subdir_path) if "handoverdoc" in file.lower() and file.endswith('.docx')]

        # Delete files not in the retention list and all subdirectories
        for root, dirs, files in os.walk(main_subdir_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in highest_version_files and file_path not in handover_docs:
                    os.remove(file_path)

            # This change deletes all subdirectories after processing files
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path, ignore_errors=True)

# Example usage
main_directory = 'path/to/main_directory'
retain_highest_version_sas_and_handoverdoc(main_directory)
