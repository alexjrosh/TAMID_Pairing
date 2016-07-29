import app_consumer


pm_app = app_consumer.consume_app('PM.xlsx')
company_app = app_consumer.consume_app('company.xlsx')

cost_matrix = app_consumer.create_cost_matrix(company_app, pm_app)

print repr(cost_matrix)