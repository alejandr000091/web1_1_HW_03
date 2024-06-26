
from pathlib import Path
import shutil
import sys
from time import time

def sort_files(location_sort_folder: Path, location_new_folder: Path):
    for element in location_sort_folder.iterdir():
        # print(element.name)   # Виведе у циклі імена всіх папок та файлів
        if element.is_dir():
            # print(f"is dir = {element}")
            sort_files(element, location_new_folder)
        if element.is_file():
            withou_ex_name = element.name.split(".")
            ex_name = withou_ex_name[1] #name of extension
            # print(ex_name)
            new_path = location_new_folder.joinpath(ex_name)
            if not location_new_folder.exists():
                location_new_folder.mkdir()
            # print(new_path)
            new_path_and_file = new_path.joinpath(element.name)
            if not new_path.exists():
                new_path.mkdir()
            shutil.copyfile(element, new_path_and_file)
            # print(f"is file = {element}, has an extension {element.suffix}, and name is {element.name}, and folder should be {ex_name}")
    


if __name__ == '__main__':
    start_time = time()
    location_sort_folder = Path('P:\\sort')
    # location_sort_folder = Path(sys.argv[1]) #P:\sort
    location_new_folder = Path('P:\\sort_copy')
    # location_new_folder = Path(sys.argv[2]) #P:\sort_copy

    #for run input in cmd:
    #py n_sort.py P:\sort P:\sort_copy
    try:
        sort_files(location_sort_folder, location_new_folder)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds \n")
    except:
        print("folder doesn't exist")