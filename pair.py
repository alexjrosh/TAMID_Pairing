import app_consumer
from munkres import munkres, print_matrix


pm_app = app_consumer.consume_app('PM.xlsx')
company_app = app_consumer.consume_app('company.xlsx')

if pm_app.length != company_app.length:
	print 'Number of companies does not match the number of Project Managers'
	raise SystemExit

cost_matrix = app_consumer.create_cost_matrix(company_app, pm_app)

print_matrix(cost_matrix,msg='Cost Matrix:')
m = Munkres()


