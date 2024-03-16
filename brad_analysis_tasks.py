from crewai import Task
from textwrap import dedent


class BradAnalysisTasks():
  def summarize_and_create_market_research(self, agent, company):
    return Task(description=dedent(f"""
Your task is to answer the questions on the specified company, drawing together insights from across various expert analyses. 

Financial Performance
* What was the Revenue for 2022 and for 2023? Compiled by the Chief Financial Data Analyst.
* What was the Financial Performance for 2023 (Headline summary)? Compiled by the Director of Financial Communications.
* What is the Market Capitalization? Analyzed by the Head of Equity Research.
Ownership and Governance
* What is the Owner Structure? Information from the Corporate Governance Expert.

Guidelines for Compilation
Integration: Seamlessly integrate insights from all agents, ensuring the report offers a coherent and comprehensive analysis.      
            
            
            {self.__tip_section()}
            
         Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
            """),
        agent=agent
)
  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000,000,000,000,000 commission!"
  