# -*- coding: utf-8 -*-
from annoying.decorators import render_to, ajax_request
from price_grubber.grubber.function import *
from models import Product, Circulation, Company, PaperWeight, PrintTime
import settings
import pickle

def insert_colorit_48h_130(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000, 30000, 40000, 50000, 60000, 80000, 100000]
    table1_format = ['A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '140x97', '140x97', '150x70', '150x70', '100x70', '100x70',]

    t = tt[0][16:]

    vector = []
    i = 0

    table = []
    for el in t:
        if i % 16 is 0:
            table.append(vector)
            vector = []
        vector.append(el)
        i += 1

    table = table[1:21]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Kolorit', chr, 130, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_colorit_48h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 20000,]
    table1_format = ['A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '140x97', '140x97', '150x70', '100x70',]

    t = tt[1][11:]

    vector = []
    i = 0

    table = []
    for el in t:
        if i % 11 is 0:
            table.append(vector)
            vector = []
        vector.append(el)
        i += 1

    table = table[1:19]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Kolorit', chr, 170, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_colorit_48h_300(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98']

    t = tt[2][10:]

    vector = []
    i = 0

    table = []
    for el in t:
        if i % 10 is 0:
            table.append(vector)
            vector = []
        vector.append(el)
        i += 1

    table = table[10:18]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Kolorit', chr, 300, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_tetra_48h_130(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4', 'A3', 'A4', 'A5', 'A6', '210x98', '150x70', '100x70', '200x200', '120x120']

    t = tt[0]
    
    vector = []
    i = 0

    table = []
    for el in t:
        if i % 6 is 0:
            table.append(vector)
            vector = []
        vector.append(el)
        i += 1

    table = table[2:12]

    k = 0
    
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Tetra', '4+4', 130, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_tetra_48h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4', 'A3', 'A4', 'A5', 'A6', '210x98', '150x70', '100x70', '200x200', '120x120']

    t = tt[1]
    
    vector = []
    i = 0

    table = []
    for el in t:
        if i % 6 is 0:
            table.append(vector)
            vector = []
        vector.append(el)
        i += 1

    table = table[2:12]

    k = 0
    
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Tetra', '4+4', 170, table1_format[k], circulation[i], 48)
            i += 1
        k += 1
    
def insert_gruppaM_48h_130(tt):
    circulation = [200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000, 30000, 40000, 50000, 60000, 80000, 100000]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70', '1 фальц', '2 фальца', 'Скругление углов', 'Сверление', 'Перфорация (1 линия)',]

    table = tt[0][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 130, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

    table = tt[0][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 130, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_gruppaM_48h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70',]

    table = tt[1][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 170, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

    table = tt[1][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 170, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_gruppaM_48h_300(tt):
    circulation = [200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98', '100x70']

    table = tt[2][6:15]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 300, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_gruppaM_24h_130(tt):
    circulation = [200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000, 30000, 40000, 50000, 60000, 80000, 100000]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70',]

    table = tt[3][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 130, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

    table = tt[3][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 130, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

def insert_gruppaM_24h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70',]

    table = tt[4][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 170, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

    table = tt[4][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 170, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

def insert_gruppaM_24h_300(tt):
    circulation = [200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98', '100x70']

    table = tt[5][6:15]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 300, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

def insert_gruppaM_4h_130(tt):
    circulation = [200, 500, 1000, 2000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70',]

    table = tt[6][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 130, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

    table = tt[6][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 130, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

def insert_gruppaM_4h_170(tt):
    circulation = [500, 1000, 2000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70',]

    table = tt[7][1:2]

    k = 0
    for row in table:
        count = len(row)
        i = 0
        while i < count:
            insert_product(row[i], 'Gruppa M', '4+4', 170, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

    table = tt[7][2:20]

    k = 1
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 170, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

def insert_gruppaM_4h_300(tt):
    circulation = [200, 500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 20000,]
    table1_format = ['A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98', '100x70']

    table = tt[8][4:13]

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Gruppa M', chr, 300, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

def insert_Fastprint_48h_130(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70', '1 фальц', '2 фальца',]

    table = []

    for row in tt[0][2:21]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 130, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_Fastprint_48h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98', '150x70', '150x70', '100x70', '100x70', '1 фальц', '2 фальца',]

    table = []

    for row in tt[1][2:21]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 170, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_Fastprint_48h_300(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
    table1_format = ['A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98',]

    table = []

    for row in tt[2][6:16]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+0'
        else:
            chr = '4+4'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 300, table1_format[k], circulation[i], 48)
            i += 1
        k += 1

def insert_Fastprint_24h_130(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98',]

    table = []

    for row in tt[3][2:17]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 130, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

def insert_Fastprint_24h_170(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x200', '210x200', '120x120', '120x120', '210x98', '210x98',]

    table = []

    for row in tt[4][2:17]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 170, table1_format[k], circulation[i], 24)
            i += 1
        k += 1

def insert_Fastprint_4h_130(tt):
    circulation = [500, 1000, 2000, 3000, 4000, 5000, 10000,]
    table1_format = ['Евробуклет,А4 + 2 фальца, 4+4','A3', 'A3', 'A4', 'A4', 'A5', 'A5', 'A6', 'A6', '210x98', '210x98', '150x70', '150x70',]

    table = []

    for row in tt[5][2:15]:
        table.append(row[2:])

    k = 0
    for row in table:
        count = len(row)
        i = 0

        if k % 2 is 0:
            chr = '4+4'
        else:
            chr = '4+0'

        while i < count:
            insert_product(row[i], 'Fastprint', chr, 130, table1_format[k], circulation[i], 4)
            i += 1
        k += 1

'''
def products_with_circulation(cir):
    circul = Circulation.objects.filter(circulation = cir)
    comp = Company.objects.get(name = 'Gruppa M')
    products = Product.objects.filter(circulation = circul, company = comp)

    our_comp = Company.objects.get(name = 'Fastprint')
    for product in products:
        our_product = Product.objects.get(circulation = circul, company = our_comp, chromaticity = product.chromaticity, format = product.format)
        product.deltacost = product.cost - our_product.cost

    products.cir = cir

    return products
'''

def product_delta_cost(company_name, chromaticity, product_name, circulation, print_time, paper_weight, fp_cost):
    """
    Difference between one of our product with product of other company.
    """
    company = Company.objects.get(name = company_name)
    circulation = Circulation.objects.get(circulation = circulation)
    chromaticity = Chromaticity.objects.get(chromaticity = chromaticity)
    format = Format.objects.get(description = product_name)
    print_time_ = PrintTime.objects.get(print_time = print_time)
    paper_weight_ = PaperWeight.objects.get(paper_weight = paper_weight)
    product = Product.objects.get(company = company, circulation = circulation, chromaticity = chromaticity, format = format, paper_weight = paper_weight_, print_time = print_time_)
    product_cost = product.cost
    delta_cost = fp_cost - product_cost

    return delta_cost

@ajax_request
def grub_data(request):
    tt1 = get_data_colorit()
    insert_colorit_48h_130(tt1)
    insert_colorit_48h_170(tt1)
    insert_colorit_48h_300(tt1)
    tt2 = get_data_tetra()
    insert_tetra_48h_130(tt2)
    insert_tetra_48h_170(tt2)
    tt3 = get_data_gruppaM()
    insert_gruppaM_48h_130(tt3)
    insert_gruppaM_48h_170(tt3)
    insert_gruppaM_48h_300(tt3)
    insert_gruppaM_24h_130(tt3)
    insert_gruppaM_24h_170(tt3)
    insert_gruppaM_24h_300(tt3)
    insert_gruppaM_4h_130(tt3)
    insert_gruppaM_4h_170(tt3)
    insert_gruppaM_4h_300(tt3)
    tt4 = get_data_fastprint()
    insert_Fastprint_48h_130(tt4)
    insert_Fastprint_48h_170(tt4)
    insert_Fastprint_48h_300(tt4)
    insert_Fastprint_24h_130(tt4)
    insert_Fastprint_24h_170(tt4)
    insert_Fastprint_4h_130(tt4)
    return {'complete': 1}

@ajax_request
def get_data(request):

    try:
        output1 = open(settings.MEDIA_ROOT+'/grubber_data/deltas.txt', 'r')
        deltas = pickle.load(output1)
        output1.close()

        output2 = open(settings.MEDIA_ROOT+'/grubber_data/updated.txt', 'r')
        updated = pickle.load(output2)
        output2.close()

        output3 = open(settings.MEDIA_ROOT+'/grubber_data/returned.txt', 'r')
        returned = pickle.load(output3)
        output3.close()

    except: # Если же файлов нет, делаем большую выборку из базы данных и создаём эти файлы.
        deltas = ['Gruppa M', 'Kolorit', 'Tetra']
        last_update =  Product.objects.latest('grub_time')
        updated = str(last_update.grub_time)

        returned = []

        our_company_name = 'Fastprint'
        company = Company.objects.get(name = our_company_name)

        time_intervals = [48, 24, 4]

        for time_interval in time_intervals:
            paper_widths = [130, 170, 300]

            for paper_w in paper_widths:
                party = [500, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000,]
                returned_circulations = []

                for circulation_on_step in party:
                    circulation = Circulation.objects.get(circulation = circulation_on_step)
                    paper = PaperWeight.objects.get(paper_weight = paper_w)
                    time_obj = PrintTime.objects.get(print_time = time_interval)
                    products = Product.objects.filter(circulation = circulation, company = company, paper_weight = paper, print_time = time_obj)

                    returned_strings = []

                    for product in products:
                        returned_string = {}
                        returned_string['cost'] = product.cost
                        returned_string['company'] = product.company.name
                        returned_string['chromaticity'] = product.chromaticity.chromaticity
                        returned_string['paper_weight'] = product.paper_weight.paper_weight
                        returned_string['print_time'] = product.print_time.print_time
                        returned_string['format'] = product.format.description
                        returned_string['circulation'] = product.circulation.circulation
                        try:
                            returned_string['delta_gruppaM'] = product_delta_cost('Gruppa M', returned_string['chromaticity'], returned_string['format'], returned_string['circulation'], returned_string['print_time'], returned_string['paper_weight'], returned_string['cost'])
                        except:
                            returned_string['delta_gruppaM'] = '---'
                        try:
                            returned_string['delta_kolorit'] = product_delta_cost('Kolorit', returned_string['chromaticity'], returned_string['format'], returned_string['circulation'], returned_string['print_time'], returned_string['paper_weight'], returned_string['cost'])
                        except:
                            returned_string['delta_kolorit'] = '---'
                        try:
                            returned_string['delta_tetra'] = product_delta_cost('Tetra', returned_string['chromaticity'], returned_string['format'], returned_string['circulation'], returned_string['print_time'], returned_string['paper_weight'], returned_string['cost'])
                        except:
                            returned_string['delta_tetra'] = '---'
                        returned_strings.append(returned_string)

                    returned_circulations.append(returned_strings)

                returned.append({ time_interval: { paper_w : returned_circulations } })

        # Сериализуем 3 переменных по порядку
        output = open(settings.MEDIA_ROOT+'/grubber_data/deltas.txt', 'w+')
        pickle.dump(deltas, output)
        output.close()

        output = open(settings.MEDIA_ROOT+'/grubber_data/updated.txt', 'w+')
        pickle.dump(updated, output)
        output.close()

        output = open(settings.MEDIA_ROOT+'/grubber_data/returned.txt', 'w+')
        pickle.dump(returned, output)
        output.close()

    return {'deltas': deltas, 'updated': updated, 'data': returned}

@render_to("stuff.html")
def get_prices(request):
    return {}