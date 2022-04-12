
import csv

def print_all(dict_csv):
	print("| CarModel| IssueDate|\n")
	for row in dict_csv:
		print("|%9s|%9s|\n"% (row['CarModel'],row['issue-date']))

def filter_file ():
	file_path = str(input('please input file path*\n'))
	car_model = str(input('please input car model\n'))
	issue_date = str(input('please input issue date\n'))
	if issue_date != '' and issue_date.isdigit() == False:
		print('incorrect issue date\n')
		return False
	file = open(file_path,'r',encoding='utf8')
	csvreader = csv.DictReader(file)
	if issue_date == '' and car_model == '':
		print_all(csvreader)
	else :
		print("| CarModel| IssueDate|\n")
		for row in csvreader :
			if (row['CarModel'] == car_model or car_model == '') and (row['issue-date'] == issue_date or issue_date == ''):
				print("|%9s|%9s|\n"% (row['CarModel'],row['issue-date']))
	file.close()

filter_file()