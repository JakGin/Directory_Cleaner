import os
import shutil


def main():
    ans = input("Are you sure you want to organize your files in the current directory? (Y/n): ").lower()
    if ans == "y":
        files = get_files()
        extensions = get_extensions(files)
        make_dirs(extensions)
        move_files(get_files())


def get_extensions(files):
    extensions = []

    for item in files:
        extension = item.split(".")[-1]
        if extension not in extensions:
            extensions.append(extension)
    
    return extensions


def make_dirs(extensions):
    directories = []

    for extenstion in extensions:
        try:
            os.mkdir(extenstion + " directory")
        except FileExistsError:
            pass
        directories.append(extenstion + " directory")
    
    return directories


def get_files():
    files = []

    for item in os.listdir():
        if os.path.isfile(item) and item != os.path.basename(__file__):
            files.append(item)
    
    return files


def move_files(files):
    path = os.getcwd()

    for item in files:
        shutil.move(os.path.join(path, item), os.path.join(path, item.split(".")[-1] + " directory", item))


if __name__ == "__main__":
    main()