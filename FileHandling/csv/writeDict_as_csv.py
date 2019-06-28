# Writing Data from dictionary as csv file
import csv

outDir = r'D:\CODE\sample_csv.txt'

dataset = [ ['1823981,Ana,Martinez'],
    ['1823982,Joann1,Cerda'],
    ['1823983,Joann2,Cerda']
]

with open(outDir, "w") as csv_fout:
	fields = ['CustNo', 'FirstName', 'LastName']
	writer = csv.DictWriter(csv_fout, fieldnames=fields)
	
	writer.writeheader()
	for rec in dataset:
            cust, fname, lname = str(rec).split(',')
            writer.writerow({fields[0]: cust.strip('['),
                            fields[1]: fname, 
                            fields[2]: lname.strip(']') })
