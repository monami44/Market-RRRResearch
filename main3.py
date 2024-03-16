from crewai import Crew
from textwrap import dedent
from brad_analysis_agents import BradAnalysisAgents
from brad_analysis_tasks import BradAnalysisTasks

from fpdf import FPDF

from dotenv import load_dotenv
load_dotenv()



class FinancialCrew:
  def __init__(self, company):
    self.company = company
    
  def run(self):
    
    agents = BradAnalysisAgents()
    tasks = BradAnalysisTasks()

    
    
    legal_company_name_researcher = agents.legal_company_name_researcher()
    headquaters_researcher = agents.headquaters_researcher()
    year_incorporated_researcher = agents.year_incorporated_researcher()
    lines_of_business_researcher = agents.lines_of_business_researcher()
    brief_synopsis_of_company_researcher = agents.brief_synopsis_researcher()
    banner_brands_researcher = agents.banner_brands_researcher()
    target_market_researcher = agents.target_market_researcher()
    revenue_researcher = agents.revenue_researcher()
    financial_performance_2023_researcher = agents.financial_performance_2023_researcher()
    market_capitalization_researcher = agents.market_capitalization_researcher()
    company_owner_researcher = agents.company_owner_researcher()
    founding_story_researcher = agents.founding_story_researcher()
    key_points_of_difference_researcher = agents.key_points_of_difference_researcher()
    top_5_strategic_initiatives_researcher = agents.top_5_strategic_initiatives_researcher()
    worries_risks_and_concerns_researcher = agents.worries_risks_and_concerns_researcher()
    main_competitors_researcher = agents.main_competitors_researcher()
    swot_analysis_expert = agents.swot_analysis_expert()
    store_designer_researcher = agents.store_designer_researcher()
    news_researcher = agents.news_researcher()
    executive_moves_researcher = agents.executive_moves_researcher()
    summarizing_agent = agents.summarizing_agent()


    summarize_and_create_market_research3 = tasks.summarize_and_create_market_research3(summarizing_agent, self.company)

    crew = Crew(
      agents=[
        legal_company_name_researcher,
        headquaters_researcher,
        year_incorporated_researcher,
        lines_of_business_researcher,
        brief_synopsis_of_company_researcher,
        banner_brands_researcher,
        target_market_researcher,
        revenue_researcher,
        financial_performance_2023_researcher,
        market_capitalization_researcher,
        company_owner_researcher,
        founding_story_researcher,
        key_points_of_difference_researcher,
        top_5_strategic_initiatives_researcher,
        worries_risks_and_concerns_researcher,
        main_competitors_researcher,
        swot_analysis_expert,
        store_designer_researcher,
        news_researcher,
        executive_moves_researcher,
        summarizing_agent,  
      ],
      
      tasks=[
        summarize_and_create_market_research3 
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Brad's AICrew")
  print('-------------------------------')
  company = input(
    dedent("""
      What is the company you want to analyze?
    """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
