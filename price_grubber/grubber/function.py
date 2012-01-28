# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from price_grubber.models import *
from datetime import datetime
import urllib

def download_page(url):
    '''
    Download page and return BeautifulSoup object for parse.
    '''
    page = urllib.urlopen(url)
    return BeautifulSoup(''.join(page))



def insert_product(cost, company_name, chromaticity, paper_weight, format_name, circulation, print_time):
    """
    Insert 1 product to the DB
    """

    product = Product(cost = cost)

    try:
        product.company = Company.objects.get(name = company_name)
    except:
        product.company = Company.objects.create(name = company_name)

    try:
        product.chromaticity = Chromaticity.objects.get(chromaticity = chromaticity)
    except:
        product.chromaticity = Chromaticity.objects.create(chromaticity = chromaticity)

    try:
        product.paper_weight = PaperWeight.objects.get(paper_weight = paper_weight)
    except:
        product.paper_weight = PaperWeight.objects.create(paper_weight = paper_weight)

    try:
        product.format = Format.objects.get(description = format_name)
    except:
        product.format = Format.objects.create(description = format_name)

    try:
        product.circulation = Circulation.objects.get(circulation = circulation)
    except:
        product.circulation = Circulation.objects.create(circulation = circulation)

    try:
        product.print_time = PrintTime.objects.get(print_time = print_time)
    except:
        product.print_time = PrintTime.objects.create(print_time = print_time)

    product.grub_time = datetime.now()

    product.save()

def only_numbers(string):
    # Function returns only numbers from string if string include it.
    # Site: fastprint.info
    int_element = False
    for element in string.split('\t'):
        try:
            int_element = int(element)
        except:
            pass
    return int_element

def get_data_fastprint(typography = 'http://www.fastprint.info/sbornik/'):
    # Get data from fastprint.info and return list of tables-data.
    # Every new table in own list element of lists.

    page = download_page(typography)
    source_tables = page.findAll(id='table_order')
    tables = []
    for table in source_tables:
        dat = [map(str, row.findAll("td")) for row in table.findAll("tr")]

        rows = []
        for table_rows in dat:
            rows.append(map(only_numbers, table_rows))

        tables.append(rows)
    return tables

def get_data_gruppaM():
    #Get data from gmprint.ru and return list of tables-data.
    #Every new table in own list element of lists.

    # urls for different time interval
    tables_url_list = [
        'http://www.gmprint.ru/products/combined/2day/',
        'http://www.gmprint.ru/products/combined/1day/',
        'http://www.gmprint.ru/products/combined/6hours/'
    ]

    two_days_tables = [
        'highlight-table',
        'highlight-table2',
        'highlight-table3',
    ]

    tables = []

    for highlight_table in two_days_tables:
        page = download_page(tables_url_list[0])
        t = page.find(id=highlight_table)
        dat = [ row.findAll(name = "td") for row in t.findAll("tr") ]
        table = []
        for row in dat:
            row_for_result = []
            for el in row:
                try:
                    a = int(str(el.string).replace(' ', '').replace('\xa0', '').replace('\xc2', '').replace('&nbsp;',''))
                    row_for_result.append(a)
                except:
                    pass
            table.append(row_for_result)
        tables.append(table)


    one_day_tables = [
        'highlight-table',
        'highlight-table2',
        'highlight-table3',
    ]

    for highlight_table in one_day_tables:
        page = download_page(tables_url_list[1])
        t = page.find(id=highlight_table)
        dat = [ row.findAll(name = "td") for row in t.findAll("tr") ]
        table = []
        for row in dat:
            row_for_result = []
            for el in row:
                try:
                    a = int(str(el.string).replace(' ', '').replace('\xa0', '').replace('\xc2', ''))
                    row_for_result.append(a)
                except:
                    pass
            table.append(row_for_result)
        tables.append(table)

    six_hours_tables = [
            'highlight-table',
            'highlight-table2',
            'highlight-table3',
        ]

    for highlight_table in six_hours_tables:
        page = download_page(tables_url_list[2])
        t = page.find(id=highlight_table)
        dat = [ row.findAll(name = "td") for row in t.findAll("tr") ]
        table = []
        for row in dat:
            row_for_result = []
            for el in row:
                i = 1

                try:
                    a = int(str(el.string).replace(' ', '').replace('\xa0', '').replace('\xc2', ''))
                    row_for_result.append(a)
                except:
                    pass

            table.append(row_for_result)

        tables.append(table)

    return tables

def get_data_colorit(typography = 'http://tcolorit.ru/sbornye-tirazhi.html'):
    page = download_page(typography)
    source_tables = page.findAll('table')

    tables = []

    for table in source_tables:
        dat = [row.findAll("td") for row in table.findAll("tr")]

        new_tab = []
        for tab in dat:
            for row in tab:
                new_row = []
                for el in row:
                    new_row.append(str(el.string).replace(' ',''))
                new_tab.append(new_row)

        all_data_from_tables = []
        for row in new_tab:
            for elm in row:
                try:
                    elm = int(elm)
                except:
                    elm = ''
                all_data_from_tables.append(elm)

        all_data_from_tables2 = []
        for elem in all_data_from_tables:
            if elem is not '':
                all_data_from_tables2.append(elem)

        tables.append(all_data_from_tables2)

    return tables

def get_data_tetra(typography = 'http://www.tetraprint.ru/bukletsandlists.html'):
    page = download_page(typography)
    source_tables = page.findAll(True, {'class': 'price'})
    tables = []

    for table in source_tables:
        dat = [row.findAll("td") for row in table.findAll("tr")]

        new_tab = []
        for tab in dat:
            for row in tab:
                new_row = []
                for el in row:
                    new_row.append(str(el.string).replace(' ',''))
                new_tab.append(new_row)

        all_data_from_tables = []
        for row in new_tab:
            for elm in row:
                try:
                    elm = int(elm)
                except:
                    elm = ''
                all_data_from_tables.append(elm)

        all_data_from_tables2 = []
        for elem in all_data_from_tables:
            if elem is not '':
                all_data_from_tables2.append(elem)

        tables.append(all_data_from_tables2)

    return tables

