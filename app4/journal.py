'''
This is the journal module.
'''


import os


def load(name):
    '''
    This method loads a existing journal

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    '''
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    '''
    This method save the current journal

    :param name: this the base name of the journal.
    :param journal_data: this the journal data.
    '''
    filename = get_full_pathname(name)
    print('.....Saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write('{0}\n'.format(entry))


def get_full_pathname(name):
    '''
    This method get the full pathname of the current journal

    :param name: this is the base name of the journal.
    :return: the complete path of the journal.
    '''
    fullname = os.path.abspath(os.path.join('.','journals',name + '.jrl'))
    return fullname
