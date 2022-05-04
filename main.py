#!/usr/bin/python
from collections import defaultdict
import psycopg2
from config import config
import csv
import json

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        csv_file = str(input('Ingrese la dirección del archivo csv: '))
        # Reading connection parameters
        params = config()

        # Connecting to the PostgreSQL server
        print('Connecting to the PostgreSQL database...\n')
        conn = psycopg2.connect(**params)
		
        # Creating cursors
        cur = conn.cursor()
        cur_1 = conn.cursor()
        cur_2 = conn.cursor()

	# Inserting values from csv_file
        print('Inserting values\n')
        with open(csv_file,'r') as csv_file:
            lines = csv.reader(csv_file)
            # Skipping first line of csv file
            next(lines)

            # Creating list to append all fo those line than has changes or just not have been added
            entries_created = list()
            entries_updated = list()
            entries_skipped = defaultdict(list)

            # Reading lines of the csv file
            for line in lines:
                # Reading table vectores.name and vectores.geom
                isname = cur_1.execute(f"SELECT EXISTS(SELECT * FROM vectores WHERE name='{str(line[0])}')")
                isname_r = cur_1.fetchone()
                isgeom = cur_2.execute(f"SELECT EXISTS(SELECT * FROM vectores WHERE geom='{str(line[1])}')")
                isgeom_r = cur_2.fetchone()

                # Inserting values if neither name value neither geom value exist.
                if (isname_r[0] == False) and (isgeom_r[0] ==False):
                    cur.execute(f"INSERT INTO vectores (name, geom, area, centroid) VALUES ('{str(line[0])}','{str(line[1])}',ST_Area('{str(line[1])}'),ST_Centroid('{str(line[1])}'));")
                    entries_created.append(str(line[0]))

                else:
                    # If name exists, just upload data
                    if (isname_r[0] == True) and ((isgeom_r[0] == False)):
                        cur.execute(f"UPDATE vectores SET geom = '{str(line[1])}', area = ST_Area('{str(line[1])}'), centroid = ST_Centroid('{str(line[1])}') WHERE name = '{str(line[0])}';")
                        entries_updated.append(str(line[0]))

                    # If geom exists, don't update nothing
                    else:
                        entries_skipped['entries_skipped'].append(str(line[0]))
                
            # Creating log file
            with open('log.json','w') as log_file:
                entries_skipped_values = entries_skipped.values()
                for entries_skipped_value in entries_skipped_values:
                    if len(entries_skipped_value) != 0:
                        message = {'ErrorMessage':'The geom value of these name values are duplicated and could produce an error:'}
                        json_file = json.dumps([message,entries_skipped],indent=4)
                        log_file.writelines([json_file])
                    else:
                        pass
                print('Summary')
                # Printing number of entries created
                print(f'{len(entries_created)} input(s) were created sucessfully')
                # Printingnumer of entries updated
                print(f'{len(entries_updated)} input(s) were updated')
                # Printint number of inputs skipped
                for entries_skipped_value in entries_skipped_values:
                    if len(entries_skipped_value) != 0:
                        print(f'{len(entries_skipped_value)} input(s) were skipped\n. Please verify the log.json file.')
                    else:
                        pass

	# Closing the communication with the PostgreSQL and making changes to table
        cur.close()
        cur_2.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.\n')

if __name__ == '__main__':
    connect()