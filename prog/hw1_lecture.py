import os
import matplotlib.pyplot as plt
import pandas as pd
import random
import string
from numpy.random import default_rng
import datetime


def run():
    """
    'main' function for hw1 lecture

    creates some data then saves it in a folder
    """

    # User enters low, high, n integer
    print("Creating random data.")

    while(True):
        low = input("Please enter lowest possible value as integer:\n")
        low_int = confirm_integer(low)
        if low_int:
            break
        else:
            continue
    while(True):
        high = input("Please enter highest possible value as integer:\n")
        high_int = confirm_integer(high)
        if high_int:
            break
        else:
            continue
    while(True):
        n = input("Please enter number of values to create:\n")
        n_int = confirm_integer(n)
        if n_int:
            break
        else:
            continue

    random_df = make_random_df(low_int, high_int, n_int)

    # make output dir
    local_dir = os.getcwd()

    output_dir = os.path.join(local_dir, "Random_Files")  # complete path to new folder
    try:
        os.mkdir(output_dir)  # make folder
    except FileExistsError:
        pass  # Do nothing if folder exists

    output_df_os_mod_examples(random_df, output_dir)


def confirm_integer(input_val):
    """
    Converts input val to integer, returns False if exception
    :param input_val:
    :return: integer or False
    """
    try:
        convert_int = int(input_val)
    except Exception as e:
        print("invalid integer")
        return False
    return convert_int


def make_random_df(lower_int, upper_int, number_idx):
    """
    Creates Random DataFrame from bounds [lower_int, upper_int].
    Creates 5 column DataFrame [Integers, Floads, Random Ascii (Ul#), Random Ascii (l), Random Ascii (U#)] number_idx rows
    :param lower_int: lower bounds for random integers
    :param upper_int: upper bounds for random integers
    :param number_idx: number of random_df index
    :return: rand_df: Pandas Dataframe (5 cols) number_idx rows
    """
    # create n random data
    rng = default_rng()
    ints = rng.integers(low=lower_int, high=upper_int, size=number_idx)
    floats = ints * rng.random()  # multiply integers by random float [0,1]

    # create some characters
    rand_upper_lower_digit = random.choices(string.ascii_letters + string.digits, k=number_idx)
    rand_lower = random.choices(string.ascii_lowercase, k=number_idx)
    rand_upper_digit = random.choices(string.ascii_uppercase + string.digits, k=number_idx)

    # make dataframe
    rand_df_dict = {
        "Integers": ints,
        "Floats": floats,
        "Random Ascii (Ul#)": rand_upper_lower_digit,
        "Random Ascii (l)": rand_lower,
        "Random Ascii (U#)": rand_upper_digit
    }
    rand_df = pd.DataFrame.from_dict(rand_df_dict, orient='columns')
    return rand_df


def output_df_os_mod_examples(random_df, output_dir):
    """
    Output dataframe in many file types.
    Examples of os and os.path
    :param random_df: pandasDataFrame cols:[Integers, Floads, Random Ascii (Ul#), Random Ascii (l), Random Ascii (U#)]
    :param output_dir: path of output folder, exists==True
    :return: None
    """
    cwd = os.getcwd()

    files = os.listdir()

    print("Files inside %s" % output_dir)
    save_idx = None
    for file_idx, file in enumerate(files):
        print(file_idx, file)
        save_idx = file_idx

    # output
    # from current directory, must join path
    print("Saving dataframes")
    now = datetime.datetime.now().strftime("%Y%m%d_%H_%M_S")  # time(now) YearMoDa_Hr_Mn_Sc
    out_name = "_".join([now,"RandomDataFrame"])  # string join
    html_outpath = os.path.join(output_dir, out_name+".html") # path join
    excel_outpath = os.path.join(output_dir, out_name+".xlsx")
    csv_outpath = os.path.join(output_dir, out_name+".csv")

    random_df.to_html(html_outpath)
    random_df.to_excel(excel_outpath)
    random_df.to_csv(csv_outpath)

    # change dir to output dir
    os.chdir(output_dir)

    print("plotting image files")
    plot_imagefiles(random_df)

    print("New files:")
    new_file_list = os.listdir()
    new_image_files = diff_lists(files, new_file_list)
    for new_file in new_image_files:
        save_idx += 1
        print(save_idx, new_file)

    #return to original dir b4 exit
    os.chdir(cwd)
    return


def plot_imagefiles(rand_df):
    """
    Plots image files from random df
    :param rand_df: pandasDataFrame cols:[Integers, Floats, Random Ascii (Ul#), Random Ascii (l), Random Ascii (U#)]
    :return: None
    """
    now = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")  # time(now) YearMoDa_Hr_Mn_Sc

    lines_fig, lines_ax = plt.subplots(figsize=(15, 10))

    lines = rand_df.loc[:, ["Integers", "Floats"]]
    lines['Integers'].value_counts().sort_index().plot(kind='line', ax=lines_ax)
    lines['Floats'].value_counts().sort_index().plot(kind='line', ax=lines_ax)
    plt.legend()
    lines_fig.savefig(now + "_RandomLines.png")
    plt.close()

    letters_fig, letters_ax = plt.subplots(figsize=(15, 10))

    rand_strings = rand_df.loc[:, ["Random Ascii (Ul#)", "Random Ascii (l)", "Random Ascii (U#)"]]
    pd.value_counts(rand_strings.values.flatten()).sort_values().plot(kind='bar')
    plt.legend()
    letters_fig.savefig(now + "_RandomLetters.jpg")
    plt.close()

    return


def diff_lists(li1, li2):
    """
    Compares li1 to li2, returns union
    :param li1: List
    :param li2: List
    :return: Union List
    """
    return list(list(set(li1)-set(li2))+ list(set(li2)-set(li1)))


if __name__ == '__main__':
    print("Running hw1_lecture.py as main")
    run()