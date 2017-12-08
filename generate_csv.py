import random
import argparse
import csv
from faker import Faker


def integer_csv(rows, schema, delimiter):
    random.seed(10)
    fake = Faker('it_IT')
    generators = []
    
    a = ['active','deactive']
    for column in schema:
        if column == 'int':
            generators.append(lambda: random.randint(0, 100))
        elif column == 'str':
            generators.append(lambda: fake.name())
        elif column == 'float':
            generators.append(lambda: random.random())
        elif column == 'status':
        	generators.append(lambda: a[random.randint(0,1)])
    

    with open('test.csv','wb') as csvfile:    
         writer = csv.writer(csvfile, delimiter=delimiter)
    # Gives the header name row into csv
         #writer.writerow([g for g in schema])
         writer.writerow(['Device Id','Device Name','Name','Status'])		
    #Data add in csv file     	
         for x in xrange(rows):
             writer.writerow([g() for g in generators])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a large CSV file.',
        epilog='''"Space is big. You just won't believe how vastly,
        hugely, mind-bogglingly big it is."''')
    parser.add_argument('rows', type=int,
                        help='number of rows to generate')
    parser.add_argument('--delimiter', type=str, default=',', required=False,
                        help='the CSV delimiter')
    parser.add_argument('schema', type=str, nargs='+',
                        choices=['int', 'str', 'float','status'],
                        help='list of column types to generate')

    args = parser.parse_args()
    integer_csv(args.rows, args.schema, args.delimiter)
