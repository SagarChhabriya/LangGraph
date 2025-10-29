# Langchain vs Langgraph


## Langchain

Langchain is an open-source library designed to simplify the process of building LLM based applications. It provides modular building blocks that let you create sophisticated LLM-based workflows with ease. 

Langchain consists of multiple components

1. Model components gives us a unified inferface to interact with various LLM providers.
2. Prompts components help you engineer prompts
3. Retrievers components help you fetch relevant documents form a vector store

But the biggest offering of langchain is chains.


What we can do with langchain

1. Simple conversational workflows like Chatbots, Text Summarizers
2. Multistep workflows
3. RAG applications
4. Basic Level agents



### Challengs
1. Control Flow Complexity
    - In langchain we need to handle control flow manully
2. State Handling
    - There is no such feature for state handling in langchain. We need to implement by ourselves.
3. Event Driven Execution
    - Workflow: Sequential/Event Driven Exeuction. Langchain handles sequential workflows
4. Fault Tolerance
    - In case of long running workflows that spans to weeks/months. We'll use persistence layer to handle this.
5. Human in the loop
    - HITL in Langgraph is first class citizen. Langchain doesn't support by default.
6. Nest Workflow
    - Subgraphs in langgraph. It helps build multiagent workflows. But its a challenge in langchain
7. Obersvability
    - Monitoring: We'll be using langsmith and it can be integrated with both langchain and langgraph. Langsmith only monitors langchain code but glue code that results in partial obersvability in case of langchain.



### Langgraph
Langgraph is built on top of langchain and it doesn't replace it. We'll still use Langchain components like:

- ChatOpenAI(LLMs)
- PrmoptTemplate
- Retrievers
- DocumentLoaders
- Tools, etc


- Alternatives to Langgraph:  Crew AI, AutoGen, Openai-SDK, Google ADK
