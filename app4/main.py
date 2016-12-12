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
    journal_name = input('Inform the name of the file <Enter to default>:\n')
    if journal_name.strip() == '':
        journal_name = 'default'
    journal_data = journal.load(journal_name)
    recentdata = []
    print('\nWhat do you want to do with your journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('\n[L]ist entries \n [A]dd an entry \n E[x]it: \n')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data,recentdata)
        elif cmd == 'a':
            add_entry(journal_data,recentdata)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('Finished')
    journal.save(journal_name,journal_data)


def list_entries(data,recentdata):
    '''
    This list the entries of the current journal

    :param data: The current journal data
    '''
    print('\nThis is your entire journal entries:')
    entries = reversed(data)
    for index,entry in enumerate(entries):
        print('[{0}] {1}'.format(index+1,entry))

    print('\nThis is your recent made journal entries:')
    entries = reversed(recentdata)
    for index,entry in enumerate(entries):
        print('[{0}] {1}'.format(index+1,entry))


def add_entry(data,recentdata):
    '''
    This adds an entry to the current journal

    :param data: The current journal data
    '''
    text = input('Type your entry, <enter> to exit: ')
    if text != '':
        data.append(text)
        recentdata.append(text)

if __name__ == '__main__':
    print_header()
    run_event_loop()
