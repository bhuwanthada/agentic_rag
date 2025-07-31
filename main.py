from dotenv import load_dotenv
from uuid import uuid4
from graph.graph import compile_workflow

load_dotenv()


app, memory = compile_workflow()

if __name__ == "__main__":

    thread_id = str(uuid4())
    try:
        loaded_state_values = memory.get_state({"configurable": {"thread_id": thread_id}}).values
        # print(f"DEBUG: Loaded state for {user_id}: {loaded_state_values}")
    except Exception:
        loaded_state_values = {}  # No existing state found for this thread_id

    # The messages list must always start with the previous conversation history
    # and then the new human input.
    messages_from_state = loaded_state_values.get("messages", [])[:]

    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "agent memory?"}, config={"configurable": {"thread_id": thread_id}}))
