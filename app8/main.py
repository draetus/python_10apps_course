import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                    'file,line,text')


def main():
    print_header()
    folder = get_folder()
    if not folder:
        print("Sorry we can't search for that")
        return
    search_text = get_search_text()
    if not search_text:
        print("Sorry we can't search for that")
        return
    all_matches = search_folders(folder,search_text)
    match_count = 0
    print()
    for item in all_matches:
        match_count += 1
        print('--------MATCh--------')
        print('File : {}'.format(item.file))
        print('Line : {}'.format(item.line))
        print(item.text.strip() + '\n')
    print ('\n Match founds: {}'.format(match_count))


def print_header():
    print('-------------------------')
    print('     FILE SEARCH APP')
    print('-------------------------')


def get_folder():
    folder = input('What folder do you want to search on? ')
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_search_text():
    text = input('What are you searching for? (Single phrases only): ')
    if not text or not text.strip():
        return None
    return text.lower()


def search_folders(folder,search_text):

    items = os.listdir(folder)
    for item in items:

        full_item = os.path.join(folder,item)
        
        if os.path.isdir(full_item):
            yield from search_folders(full_item,search_text)
        else:
            yield from search_file(full_item,search_text)
        

def search_file(item,search_text):

    with open(item, 'r' , encoding='utf-8') as fin:

        line_number = 0
        
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(file=item,line=line_number,text=line)
                yield m



if __name__ == '__main__':
    main()
