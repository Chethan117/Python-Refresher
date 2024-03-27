import os
import re
import shutil

def process_directory_for_sas_files(directory):
    """
    Process a directory to find and return .sas files with their highest versions,
    and any HandoverDoc files.
    """
    sas_files = {}
    handover_docs = []
    
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if file.endswith('.sas'):
            base_name = re.sub(r'V\d+', '', file, flags=re.IGNORECASE).lower()
            version = re.findall(r'V(\d+)', file, flags=re.IGNORECASE)
            version = int(version[0]) if version else 0
            if base_name not in sas_files or sas_files[base_name][1] < version:
                sas_files[base_name] = (full_path, version)
        elif "handoverdoc" in file.lower() and file.endswith('.docx'):
            handover_docs.append(full_path)
    
    return sas_files, handover_docs

def retain_highest_version_sas_and_handoverdoc(main_directory):
    for main_subdir_name in next(os.walk(main_directory))[1]:
        main_subdir_path = os.path.join(main_directory, main_subdir_name)
        # Initially check for .sas and HandoverDoc files in the main subdirectory.
        sas_files, handover_docs = process_directory_for_sas_files(main_subdir_path)

        # If no .sas files are found, check in subdirectories.
        if not sas_files:
            for root, dirs, files in os.walk(main_subdir_path):
                subdir_sas_files, subdir_handover_docs = process_directory_for_sas_files(root)
                sas_files.update(subdir_sas_files)
                handover_docs.extend(subdir_handover_docs)

        # Retain identified files and remove others.
        retain_files = [file_info[0] for file_info in sas_files.values()] + handover_docs
        for root, dirs, files in os.walk(main_subdir_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path not in retain_files:
                    os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if not os.listdir(dir_path):
                    shutil.rmtree(dir_path, ignore_errors=True)

# Example usage
main_directory = 'path/to/main_directory'
retain_highest_version_sas_and_handoverdoc(main_directory)
