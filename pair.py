import app_consumer
import sys
from munkres import Munkres, print_matrix


company_app = app_consumer.consume_app(sys.argv[1])
pm_app = app_consumer.consume_app(sys.argv[2])

if len(pm_app) != len(company_app):
	print 'Number of companies does not match the number of Project Managers'
	print repr(pm_app)
	print repr(company_app)
	raise SystemExit

cost_matrix = app_consumer.create_cost_matrix(company_app, pm_app)
list_of_companies = cost_matrix[0]
list_of_pms = cost_matrix[1]
cost_matrix = cost_matrix[2:]

# print list_of_companies
# print
# print list_of_pms
# print
# print repr(cost_matrix)

# print_matrix(cost_matrix,msg='Cost Matrix:')
m = Munkres()
inexes_of_pairs = m.compute(cost_matrix)

for row, column in inexes_of_pairs:
	print ('company: {}, PM: {}').format(list_of_companies[row], list_of_pms[column])


