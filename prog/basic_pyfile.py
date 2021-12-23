import os


cwd = os.getcwd()


def example_function(parameter_a, parameter_b):
    """
    Example comment, what does this function do?
    Names param_a as "Files" and param_b as "Folders" in a dictionary
    :param parameter_a: type and info about param, list folders
    :param parameter_b: type and info about param, list files
    :return: Dictionary:  number of files and dirs
    """

    return {"Files":parameter_a, "Folders":parameter_b}

def basic():
    """
    main for basic_pyfile
    lists current files and directories, searches 1 sublevel
    :return: None
    """
    local=cwd
    dir_local_paths = os.listdir()

    dirs = []
    files = []
    for d in dir_local_paths:
        if os.path.isdir(d):
            dirs.append(d)
        else:
            files.append(d)
    for dir in dirs:
        subdir_files = os.listdir(os.path.join(local, dir))
        for file in subdir_files:
            if os.path.isdir(file):
                dirs.append("/".join([dir, file]))
            else:
                files.append("/".join([dir, file]))

    index_lists = example_function(files, dirs)

    for name in index_lists.keys():
        print(name+":")
        for fidx, file in enumerate(index_lists[name]):
            print(fidx, file)


if __name__ == '__main__':
    basic()
