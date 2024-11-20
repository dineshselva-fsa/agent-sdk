import mesop as me
import mesop.labs as mel
from agents import Agents
from agents.sessions import InMemorySessionService
from google.genai import types
from sequential_marketing import root_agent
import json
import traceback


agent_client = Agents()
session_service = InMemorySessionService()
session = session_service.create()

@me.stateclass
class State:
  agent_response: str = "Response"

def on_load(e: me.LoadEvent):
    me.set_theme_mode("system")

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io", "https://colab.sandbox.google.com"]
    ),
    path="/chat",
    title="Vertex AI Agent Framework - Chat",
    on_load=on_load,
)
def page():
    # mel.chat(transform, title="Chat with Vertex AI Agent Framework", bot_user="Agent")
    state = me.state(State)
    debate_topic = """AI is the future and every company needs to adopt it.
          """
    customer_name = "All State Insurance"
    customer_domain = "Insurance"
    project_description = "Marketing Campaign"
    # me.button(label="Run Research", type="stroked", on_click=lambda e: on_click_agent_run(e, debate_topic))
    me.button(label="Start Debate", type="stroked", on_click=lambda e: on_click_agent_run(e, customer_name, customer_domain, project_description))
    # print (f"Agent Response is {state.agent_response}")
    me.markdown(state.agent_response)

def on_click_agent_run(e, customer_name, customer_domain, project_description):
    try:
      state = me.state(State)
      session_context = session.get_context()
      session_context['customer_name'] = customer_name
      session_context['customer_domain'] = customer_domain
      session_context['project_description'] = project_description
      content = types.Content(role='user', parts=[types.Part.from_text(customer_name), types.Part.from_text(customer_domain), types.Part.from_text(project_description)])
      for event in agent_client.run(
          agent=root_agent,
          session=session,
          session_service=session_service,
          new_message=content,
      ):
        if event.type == 'content':
          root_agent_response = event.content.model_dump_json(indent=2, exclude_none=True)
          root_agent_response_dict = json.loads(root_agent_response)
          state.agent_response += root_agent_response_dict["parts"][0]["text"]
          yield state.agent_response
        else:
          print(f"Event type is {event.type}")
    except Exception as e:
      print(f"An error occurred: {e}")
      # Traceback the error
      traceback.print_exc()
