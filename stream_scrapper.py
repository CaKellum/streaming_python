from bs4 import BeautifulSoup as soup
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlparse


for url in argv[1:]:
    filename = urlparse(url).netloc
    response = None
    response_status = False

    print('Start scrapping '+url)

    try:
        response = urlopen(url)
        response_status = True
    except Exception as error:
        print(str(error)+' '+filename)

    if response_status:
        print('cleaning data for'+ filename)
        write_data = soup(response, features='html.parser').findAll('a', href=True)
        with open('./collected_data/{}.csv'.format(filename),'w') as file:
            for tagged_link in write_data:
                file.write(str(tagged_link.get('href'))+',')
        print('finished with '+filename)
print('Done')
