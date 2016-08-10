import sys
import pandas

# company_app_excel = sys.argv[1]
# pm_app_excel = sys.argv[2]

def consume_app(app):
	return pandas.read_excel(app).as_matrix().tolist()
	

def create_cost_matrix(company_app, pm_app):
	name_of_companies = []
	name_of_pms = []
	cost_matrix = []

	for company in company_app:
		company_name = company[1]
		service_areas = {}
		service_areas['sa_1'] = company[19]
		service_areas['sa_2'] = company[69]
		service_areas['sa_3'] = company[118]

		company_industries = {}
		company_industries['ind_1'] = company[5]
		company_industries['ind_2'] = company[6]
		company_industries['ind_3'] = company[7]

		cost_matrix_row = []
		name_of_companies.append(company_name)

		#skills
		company_skills = {}
		company_skills['internet_search'] = int(company[168]) if not pandas.isnull(company[168]) else 5
		company_skills['current_events'] = int(company[169]) if not pandas.isnull(company[169]) else 5
		company_skills['business'] = int(company[170]) if not pandas.isnull(company[170]) else 5
		company_skills['creativity'] = int(company[171]) if not pandas.isnull(company[171]) else 5
		company_skills['technology'] = int(company[172]) if not pandas.isnull(company[172]) else 5
		company_skills['sociability'] = int(company[173]) if not pandas.isnull(company[173]) else 5
		company_skills['communication'] = int(company[174]) if not pandas.isnull(company[174]) else 5
		company_skills['flexibility'] = int(company[175]) if not pandas.isnull(company[175]) else 5
		company_skills['presentation'] = int(company[176]) if not pandas.isnull(company[176]) else 5
		company_skills['working_with_a_team'] = int(company[177]) if not pandas.isnull(company[177]) else 5
		
		for pm in pm_app:
			pm_name = pm[1] + pm[2]

			#Hash each project type to pm's ranking
			first_choice_project_type = pm[10]
			second_choice_project_type = pm[11]
			third_choice_project_type =pm[12]
			pm_project_rankings = {first_choice_project_type:1, second_choice_project_type:2, third_choice_project_type:3}

			#hash each industry to pm's ranking
			first_industry_choice = pm[6]
			second_industry_choice = pm[7]
			third_industry_choice = pm[8]
			pm_industry_choices = {first_industry_choice:1, second_industry_choice:2, third_industry_choice:3}


			#skills
			pm_skills = {}
			pm_skills['internet_search'] = int(pm[13])
			pm_skills['current_events'] = int(pm[14])
			pm_skills['business'] = int(pm[15])
			pm_skills['creativity'] = int(pm[16])
			pm_skills['technology'] = int(pm[17])
			pm_skills['sociability'] = int(pm[18])
			pm_skills['communication'] = int(pm[19])
			pm_skills['flexibility'] = int(pm[20])
			pm_skills['presentation'] = int(pm[21])
			pm_skills['working_with_a_team'] = int(pm[22])


			#calculate score to represent how well the company and pm match on project type
			project_type_match_score = 0
			number_of_projects = 0
			for key, service_area in service_areas.iteritems():
				if not pandas.isnull(service_area):
					number_of_projects += 1
					if service_area in pm_project_rankings:
						project_type_match_score += pm_project_rankings[service_area]
					else:
						project_type_match_score += 4


			#calculate score to represent how well the company and pm match on industry
			# this is subtraction from the cost since matches are unlikley and should only help but not hurt
			industry_match_score = 0
			number_of_industries_listed = 0
			for key, industry in company_industries.iteritems():
				if not pandas.isnull(industry):
					number_of_industries_listed += 1
					if industry in pm_industry_choices:
						industry_match_score -= (4-pm_industry_choices[industry]) 
					else:
						industry_match_score +=4

			#calculate score to represent how well company and PM match on skills
			list_of_skills = ['internet_search', 'current_events', 'business', 'creativity', 'technology', 'sociability', 'communication', 'flexibility', 'presentation', 'working_with_a_team']
			sum_of_company_skill = 0
			for skill in list_of_skills:
				sum_of_company_skill += company_skills[skill]

			skill_score = 0
			for skill in list_of_skills:
				#************************************************************
				#	This is the penalty, I am commenting it out 
				# 	and replacing it with the delta of company and pm skill
				#************************************************************
				# skill_score += ((company_skills[skill]-pm_skills[skill])*(float(company_skills[skill])/sum_of_company_skill))
				skill_score += company_skills[skill]-pm_skills[skill]

			
			# print 'number of proj '+str(pm_name)+': '+str(number_of_projects)
			# print 'project_type_match_score-'+str(company_name)+', '+str(pm_name)+': '+str(project_type_match_score)
			# print 'skill_score-'+str(company_name)+', '+str(pm_name)+': '+str(skill_score)

			#calculate total match score based on project type, industry and skill match scores
			cost = ((project_type_match_score/number_of_projects)**2)+(industry_match_score/number_of_industries_listed)+skill_score

			cost_matrix_row.append(cost)
			if pm_name not in name_of_pms:
				name_of_pms.append(pm_name)

			print name_of_pms

		cost_matrix.append(cost_matrix_row)
		# print '========================================'


	cost_matrix.insert(0,list(name_of_pms))
	cost_matrix.insert(0,name_of_companies)
	return cost_matrix




# pm_app = comsume_app(pm_app_excel)
# company_app = comsume_app(company_app_excel)

# if pm_app.length != company_app.length:
# 	print 'Number of companies does not match the number of Project Managers'
# 	raise SystemExit
