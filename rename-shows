import os
import shutil

"""Script to rename downloaded shows"""


def rename(path, item_type, show, num_s):
    """Function in charge of renaming the files

    Rename according to Season and Episode in the S0XE0X format"""
    i = 0
    types = {
        "SUB": ".srt",
        "EP1": ".mkv",
        "EP2": ".mp4",
        "EP3": ".avi"
    }

    files = os.listdir(path)  # Get the current file names

    for j in range(0, len(files)):  # Remove the Subtitles folder
        if files[j] == 'Subtitles':
            files.pop(j)

    for item in files:
        i += 1  # Actual renaming loop
        os.rename(os.path.join(path, item),
                  os.path.join(path,
                               (show + ' S' + num_s + 'E' +
                                file_numbering(str(i)) + types[item_type])))

        print(f'\nRenaming file {i}...')

    print(f'\n\n{len(files)} files succesfully renamed\n')


def file_numbering(number):
    """Function to rename episodes according to proper format"""
    if int(number) < 10:
        new_number = '0' + number
        return new_number
    else:
        return number


def file_check(path):
    """This will go through the directory, delete useless files
    and check if there is a subtitles folder."""
    files = os.listdir(path)
    sub_path = 'empty'  # Assigning before to avoid errors
    vid = 'empty'

    i = 0

    for item in files:
        if 'ub' in item:  # to find subtitle folder
            print('\nSubtitle folder found')
            print('1. Delete')
            print('2. Rename')
            choice = input()

            again = True
            while again:
                if choice == '1':
                    files.pop(i)  # Remove from the list then delete folder
                    shutil.rmtree(os.path.join(path, item))
                    again = False
                elif choice == '2':
                    sub_path = os.path.join(path, item)
                    again = False
                else:
                    print('To make a choice enter 1 or 2')
        elif '.mkv' in item:
            vid = 'EP1'
        elif '.mp4' in item:
            vid = 'EP2'
        elif '.avi' in item:
            vid = 'EP3'
        elif '.txt' in item:
            files.pop(i)  # Remove from the list then delete file
            os.remove(os.path.join(path, item))
        elif '.jpg' in item:
            files.pop(i)  # Remove from the list then delete file
            os.remove(os.path.join(path, item))

        i += 1  # To get position in list for .pop method

    return vid, sub_path  # Path of the Subtitles folder and Video type


# Welcome message and instructions for user
print('\n\nWelcome to PyRename\n')
print('Make sure to complete these steps to avoid errors:\n')
print('1. Please rename the source folder to the name of the Show')
print('2. Delete all folders except subtitles folder')
print('3. Delete files that are not images or .txt')
print()  # The show name is used for the path and file naming
input('\nOnce done press Enter...')

# Get the name of the show
show = input('\nEnter show name: ')
# Get the Season number
num_s = input('\nEnter Season number: ')

# Go to the folder
srcfolder = 'D:\Torrents'
path = srcfolder + os.sep + show  # Create the path to the files

print('\nChecking Files...')
identifier = file_check(path)

# Calls to the rename function

if identifier[1] == 'empty':  # If there isn't a subtitles folder
    # Rename the episodes
    rename(path, identifier[0], show, num_s)
elif identifier[1] != 'empty':  # If there is a subtitles folder
    # Rename the episodes
    rename(path, identifier[0], show, num_s)

    # Rename the Subtitles folder and create new path for renaming srt files
    os.rename(identifier[1], os.path.join(path, 'Subtitles'))
    rename((path + os.sep + 'Subtitles'), 'SUB', show, num_s)


print('\nRenaming Complete')
input('Press Enter to close...')
