'''
This is the main program
'''

import journal


def print_header():
    '''
    This prints the header of the program
    '''
    print('---------------------------')
    print('       JOURNAL APP')
    print('---------------------------')


def run_event_loop():
    '''
    This gets the desired option from the user, do the respective method and then save
    the data

    Options:
        l - List the entries of the journal.
        a - Adds an entry to the journal.
        x - Exit and save the journal.
    '''
    print('What do you want to do with your journal?')
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries \n [A]dd an entry \n E[x]it: \n')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('Finished')
    journal.save(journal_name,journal_data)


def list_entries(data):
    '''
    This list the entries of the current journal

    :param data: The current journal data
    '''
    print('This is your journal entries:')
    entries = reversed(data)
    for index,entry in enumerate(entries):
        print('[{0}] {1}'.format(index+1,entry))


def add_entry(data):
    '''
    This adds an entry to the current journal

    :param data: The current journal data
    '''
    text = input('Type your entry, <enter> to exit: ')
    if text != '':
        data.append(text)

if __name__ == '__main__':
    print_header()
    run_event_loop()
