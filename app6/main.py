import os
import platform
import cat_service
import subprocess


def print_header():
    print('-----------------------------')
    print('       CAT FACTORY')
    print('-----------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download the cats...')
    cat_count = 8
    for i in range(1,cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Download cat - ' + name)
        cat_service.get_cat(folder,name)
    print('Done')


def display_cats(folder):
    if platform.system() == 'Dwarwin':
        subprocess.call(['open', folder])
        print('Displaying cats in ' + platform.system())
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
        print('Displaying cats in ' + platform.system())
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
        print('Displaying cats in ' + platform.system())
    else:
        print("We don't support your OS: " + platform.system())


if __name__ == '__main__':
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)
