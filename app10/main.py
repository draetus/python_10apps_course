from movie_client import MovieClient
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print('\n--------------------------------------------')
    print('            MOVIE SEARCH APP')
    print('--------------------------------------------\n')


def search_event_loop():
    search_text = 'ONCE_TROUGHT_LOOP'

    while search_text.lower() != 'x':
        try:
            search_text = input('What movie do you want to search for? \n')
            if search_text.lower() != 'x':
                client = MovieClient(search_text)
                results = client.perform_search()
                print('Found {} matches'.format(len(results)))
                for r in results:
                    print ('{} -- {}'.format(r.Year,r.Title))
        except  requests.exceptions.ConnectionError:
            print('ERROR : Cannot search, your network is down.')
        except ValueError as ve:
            print ('ERROR : you search string is invalid: {}'.format(ve))
        except Exception as x:
            print('ERROR : {}'.format(x))
    print('exiting...')


if __name__ == '__main__':
    main()
