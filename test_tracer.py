
from tracer_callback import GraphTracerCallbackHandler
from langchain_core.callbacks.manager import CallbackManager
from langchain_core.runnables import RunnableLambda

tracer = GraphTracerCallbackHandler()

def process(data):
    return {"result": data["input"] + " processed"}

chain = RunnableLambda(process)

chain.invoke(
    {"input": "Hello LangGraph"},
    config={"callbacks": [tracer]}
)

tracer.save("trace.json")

print("Trace generated successfully!")
print(tracer.export_trace())
