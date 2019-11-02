#!/usr/bin/python3
import sys

# built-in regexp lib
import re
import requests
from bs4 import BeautifulSoup

SCHEDULE_URL = 'http://www.ifmo.ru/ru/schedule/0/{}/raspisanie_zanyatiy.htm'


def parse_schedule(group):
    response = requests.get(SCHEDULE_URL.format(group))  # .format() fill placeholders in string with variables contents
    html = response.text

    bs = BeautifulSoup(html, features='lxml')  # import parsing lib with lxml library for faster parsing
    content_block = bs.find('article', class_='content_block')
    if 'Расписание не найдено' in str(content_block):
        print(f'Cannot parse group {group} - schedule not found!')
        return

    rasp_tabl_days = content_block.find_all('div', class_='rasp_tabl_day')
    
    s = '{"Monday": {'
    i = 0
    classes = rasp_tabl_days[0].find('table').find_all('tr')[:-1]

    for row in classes:
        if i != (len(classes) - 1):
            s = s + '"class ' + str(i) + '": ' + '{"lesson": ' +  '"' + str(row.find('td', class_='lesson').find('dd').text) +  '"' + "," + '"time": ' +  '"' + str(row.find('td', class_='time').find('span').text) +  '"' +"," + '"room": ' +   '"' + str(row.find('td', class_='room').find('dd').text) +  '"' + "," + '"teacher": ' + '"' +str(row.find('td', class_='lesson').find('dt').text) +'"'+ "}, "
        else: s = s + '"class ' + str(i) + '": ' + '{"lesson": ' +  '"' + str(row.find('td', class_='lesson').find('dd').text) +  '"' + "," + '"time": ' +  '"' + str(row.find('td', class_='time').find('span').text) +  '"' +"," + '"room": ' +   '"' + str(row.find('td', class_='room').find('dd').text) +  '"' + "," + '"teacher": ' + '"' +str(row.find('td', class_='lesson').find('dt').text) +'"' + "}}}"
        i += 1
    f = open('data.txt', "w")
    f.write(s)
    f.close

if __name__ == "__main__":
    # Called as program, not just imported

    # Check if we called with arguments
    if len(sys.argv) < 2:
        print('Usage: sync.py <group 1> <group 2> ... <group N>')

    # sys.argv[1:] means that we took a _slice_ from sys.argv - from element with index 1 to end of array
    for group in sys.argv[1:]:
        result = re.match(r'\w\d{4}', group)
        if not result:
            print(f'Cannot parse group {group}, maybe you make mistake?')
            sys.exit(0)

    # If all groups are correct, we can start parsing
    for group in sys.argv[1:]:
        parse_schedule(group)
