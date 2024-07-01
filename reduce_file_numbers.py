import os
import shutil

def get_files_sorted_by_mtime(folder_path):
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=lambda x: os.path.getmtime(x))
    return files

def select_files_to_keep(files, m):
    if m < 2:
        raise ValueError("The number of files to keep must be at least 2.")
    
    # Always keep the first and last file
    keep_files = [files[0], files[-1]]
    
    if m > 2:
        step = (len(files) - 1) / (m - 1)
        for i in range(1, m - 1):
            keep_files.append(files[int(round(i * step))])
    
    return sorted(keep_files, key=lambda x: os.path.getmtime(x))

def cleanup_folder(folder_path, keep_files):
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path) and file_path not in keep_files:
            os.remove(file_path)

def reduce_file_numbers(folder_path, num_to_keep):
    m=num_to_keep
    files = get_files_sorted_by_mtime(folder_path)
    keep_files = select_files_to_keep(files, m)
    cleanup_folder(folder_path, keep_files)

if __name__ == "__main__":
    folder_path = '/Users/karlzipser/Desktop/21Jun24_19h01m09s copy/tac/stats'  # Change this to your folder path
    m = 15  # Change this to the number of files you want to keep
    reduce_file_numbers(folder_path, m)
