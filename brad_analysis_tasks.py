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
    
  def summarize_and_create_market_research2(self, agent, company):
    return Task(description=dedent(f"""
  Your task is to answer the questions on the specified company, drawing together insights from across various expert analyses. 

**Company Foundation and Legal Identity**
* What is the legal Company name? Information from the Legal Company Name Researcher.
* What is the Headquarters Adress? Insights from the Chief Geospatial Intelligence Officer.
* In which Year the company was Incorporated? Data from the Principal Corporate Historian.
**Business Overview**
* What are the Lines of Business? Analysis by the Senior Industry Analyst and Chief Brand Strategist.
* What are the Banner Brands? Analysis by the Senior Industry Analyst and Chief Brand Strategist.
* What is the synopsis of the company? Crafted by the Master Business Storyteller.
**Strategic Positioning**
* What is the Target Market? Insights from the Lead Market Insights Analyst.
* What are the 3 main Key Points of Difference? Analysis by the Strategic Differentiation Analyst. (list them)
* What are the Top 5 Strategic Initiatives? Insights from the Chief Strategy Insights Officer. (list them)

Guidelines for Compilation
Integration: Seamlessly integrate insights from all agents, ensuring the report offers a coherent and comprehensive analysis.             
            {self.__tip_section()}
            
         Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
            """),
        agent=agent
)
  def summarize_and_create_market_research3(self, agent, company):
    return Task(description=dedent(f"""
Your task is to answer the questions on the specified company, drawing together insights from across various expert analyses. 

**Recent News**
* What are the 5 most Recent Company News (Must include the links to the references for each)? Identified by Chief News Intelligence Analyst
* What are the 3-5 most Recent Executive Moves (Must include the links to the references for each)? Identified by Executive Moves Analyst


Guidelines for Compilation
Integration: Seamlessly integrate insights from all agents, ensuring the report offers a coherent and comprehensive analysis.                   
            {self.__tip_section()}
            
         Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
            """),
        agent=agent
)  
  def summarize_and_create_market_research4(self, agent, company):
    return Task(description=dedent(f"""
Your task is to answer the questions on the specified company, drawing together insights from across various expert analyses. And include all the answer arrange them as listed below:

**Historical Context**
* What is the Founding Story (1 small paragraph)? Narrated by the Master Business Historian.
**Risk Profile**
* What are the main worries (3 sentences)? Evaluated by the Chief Risk Intelligence Analyst.
* What are the main risks (3 sentences)? Evaluated by the Chief Risk Intelligence Analyst.
* What are the main concerns (3 sentences)? Evaluated by the Chief Risk Intelligence Analyst.
**Competitive Landscape**
* What are the top 5 Main Competitors (list them)? Identified by the Lead Competitive Intelligence Analyst.
* What is the SWOT Analysis? Conducted by the Strategic Analysis Director.

Guidelines for Compilation
Integration: Seamlessly integrate insights from all agents, ensuring the report offers a coherent and comprehensive analysis.                    
            {self.__tip_section()}
            
         Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
            """),
        agent=agent
)
    
  def summarize_and_create_market_research5(self, agent, company):
    return Task(description=dedent(f"""
Your task is to answer the questions on the specified company, drawing together insights from across various expert analyses. And include all the answer arrange them as listed below:
 
  **Design and Innovation**
* What is the Store Designer Agency or architecural design agency or if its inhouse? Identified by the Store Design Agency Investigator.

  **Store Openings**
* How does the company stores look like? Minimum 5 (Include the links to refereneces)? Identified by the Lead Visual Market Analyst.
   
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
  