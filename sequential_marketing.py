import os, sys
from agents import Agent

research_agent = Agent(
    name='research_agent',
    instruction="""
  Conduct a thorough research about the customer and competitors in the context
  of {customer_domain}.
  Make sure you find any interesting and relevant information given the
  current year is 2024.
  We are working with them on the following project: {project_description}.
  Produce a complete report on the customer and their customers and competitors,
  including their demographics, preferences, market positioning and audience engagement.
  Provide the output with Title "Research Report".
""",
)

project_understanding_agent = Agent(
    name='project_understanding_agent',
    instruction="""
  Understand the project details and the target audience for
  {project_description}.
  Review any provided materials and gather additional information as needed.
  Produce a detailed summary of the project and a profile of the target audience.
  Provide the output with Title "Project Understanding Report".
""",
)

marketing_strategy_agent = Agent(
    name='marketing_strategy_agent',
    instruction="""
  Formulate a comprehensive marketing strategy for the project
  {project_description} of the customer {customer_domain}.
  Use the insights from the research task and the project understanding
  task to create a high-quality strategy.
  Produce a detailed marketing strategy document that outlines the goals, target
  audience, key messages, and proposed tactics, make sure to have name, tatics, channels and KPIs.
  Provide the output with Title "Marketing Strategy Report".
""",
)

campaign_idea_agent = Agent(
    name='campaign_idea_agent',
    instruction="""
  Develop creative marketing campaign ideas for {project_description}.
  Ensure the ideas are innovative, engaging, and aligned with the overall marketing strategy.
  Produce a list of 5 campaign ideas, each with a brief description and expected impact.
  Provide the output with Title "Campaign Ideas Report".
""",
)

copy_creation_agent = Agent(
    name='copy_creation_agent',
    instruction="""
  Create marketing copies based on the approved campaign ideas for {project_description}.
  Ensure the copies are compelling, clear, and tailored to the target audience.
  Produce marketing copies for each campaign idea.
  Provide the output with Title "Copy Creation Report".
""",
)

root_agent = Agent(
    model='gemini-1.5-flash',
    name='marketing_agent',
    children=[
        research_agent,
        project_understanding_agent,
        marketing_strategy_agent,
        campaign_idea_agent,
        copy_creation_agent,
    ],
    flow='sequential',
)
