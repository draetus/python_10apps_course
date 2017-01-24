import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond,temp,tempUnit,loc')


def print_header():
    print('---------------------------------')
    print('          WEATHER APP')
    print('---------------------------------')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html,'html.parser')
    loc = soup.find(id='location').find('h1').text
    condition = soup.find(id='curCond').find(class_='wx-value').text
    temperature_value = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-value').text
    temperature_unit = soup.find(id='curTemp').find(class_='wx-data').find(class_='wx-unit').text
    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temperature_value = cleanup_text(temperature_value)
    temperature_unit = cleanup_text(temperature_unit)
    report = WeatherReport(cond=condition,temp=temperature_value,tempUnit=temperature_unit,loc=loc)
    return report


def find_city_and_state_from_location(loc):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__' :
    print_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print('The temperature in {} is {} {} and {}'.format(report.loc,report.temp,report.tempUnit,report.cond))
