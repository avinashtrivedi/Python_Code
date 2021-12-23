import os
from hw1_lecture import run

def hw_main():
    """
    Main function for HW1.  Add  any new (added) function calls to this method.
    :return: None
    """

    print("HW1 main function")

    # add lines to this function before it ends at the return below
    # create your own functions and use them to accomplish your goals!

    print("Creating random data files")
    # Goal 1)
    # Create a for loop that calls run() 5 times
    # add print text to the loop, to clarify to the user current loop #

    print("Finding Random Files")
    # Goal 2)
    # use the os module to list all files in the "/Random_Files/" folder
    # be sure to carefully record paths to files
    # print the # of files

    print("Sorting by file type")
    # Goal 3)
    # sort files found in the "Random_Files" folder by file type (.csv, .html, .xlsx, .png, .jpg)
    # collect paths to all files of a specific type grouped in a data structure
    # for example: a numpy array containing paths to all .csv or a list containing all paths to .png, etc.

    print("Making Sorted Directories")
    # Goal 4)
    # create directories for each file type at the same level as "Random_Files" folder
    # (inside this script's working directory)
    # Be sure to make this script re-usable and protect os.mkdir() with try/except (See  hw1_lecture.py, lines 47-51)

    print("Sorting Random_Files")
    # Goal 5)
    # Move the sorted files into the new directories (all .csv in the CSV directory and so on)
    # This can be done as a copy then delete the original, or move

    print("Removing old directory")
    # Goal 6)
    # delete the Random_Files directory

    print("HW1 Script Complete!")

    return





if __name__ == '__main__':
    print("Starting HW1 Script")
    hw_main()