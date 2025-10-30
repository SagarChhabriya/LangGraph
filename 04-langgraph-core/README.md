# Langgraph

- Langgraph is an orchestration framework for building integlligent, stateful, and multi-step LLM workflows.
- It enables advanced features like parallelism, loops, branching, memory, and resumability; making it ideal for agentic and production-grade AI applications.
- It models your logic as a graph of nodes (tasks) and edges (routing) instead of a linear chain. 


## LLM Workflows

1. LLM workflows are a step by step process using which we can build complex LLM application.
2. Each step in a workflow performs a distinct task; such as prompting, reasoning, tool calling, memory access, or decision making.
3. Workflows can be linear, parallel, branched, or looped, allowing for complex behaviors like retries, multi-agent communication, or tool-augmented reasoning. 
4. Common workflows:
    - Prompt Chaining
    - Routing
    - Parallelization
    - Orchestrator workers
        - Its similar to the parallelization. In orchestrator worker the nature of task is dynamic it can vary but in the parallelization its predefined.
    - Evaluator Optimizer



### Graphs, Nodes, and Edges

The system generates an essay topic, collects the student's submission, and evaluates it in parallel on depth of analysis, language quality, and clarity of thought. Based on the combined score, it either gives feedback for improvement or approves the essay.


1. Generate Topic: System generates a relevant UPSC style essay topic and presents it to the student.
2. Collect Essay: Students writes and submits the essay based on the generated topic.
3. Evaluate Essay (Parallel Evaluation Block): Run three evaluation tasks in parallel
    - EvaluateDepth: Analyzes depth of analysis, argument strength, and critical thinking.
    - EvaluateLanguage: Checks grammar, vocabulary, fluency, and tone.
    - EvaluateClarity: Assesses coherence, logical flow, and clarity of thoughts
4. AggregateResults: Combines the three scores and generates a total score(e.g., out of 15)
5. Conditional Routing: Based on total score:
    - If score meets threshold -> go to ShotSuccess
    - If score is below threshold -> go to GiveFeedback
6. GiveFeedback: Provides targeted suggestions for improvment in weak areas.
7. Collect Revision
    - Subject resubmits the revised essay
    - Loop back to EvaluateEssay
8. ShowSuccess: Congratulate the student and ends the flow.


![alt text](assets/04.1-flow.png)


- Graph: Flow
- Node: Unit Task (behind the scence its a python function)
- Edge: What's next in the flow. Edge is like the trigger.
    - Sequential
    - Parallel
    - Conditional
    - Feedback/Loop


### State
In Langgraph, state is the shared memory that flows through the workflow. It holds all the data being passed between nodes as your graph runs. It can be implemented using TypedDict/Pydantic and its mutable.


### Reducers
Reducers in Langgraph defines how updates from nodes are applied to the shared state. Each key in the state can have its own reducer, which determines whether new data replaces, merges, or adds to the existing value.



## Langgraph Execution Model

1. Graph Definition
- We define
    - The state schema
    - Nodes (functions that perform tasks)
    - Edges (which node to connect which)

2. Compilation
- We call .compile() on the StateGraph
- This checks the graph structure and perpares it for execution

3. Invocation
- You run the graph with .invoke(initial_state)
- Langgraph sends the intial state as a message to the entry node(s).

4. Super Step Begin
- Execution proceedes in rounds i.e., layer by layer.

5. Message Passing and Node activation
- The messages are passed to downstream nodes via edges.
- Nodes that receive messages become active for the next round.

6. Halting Condition
- Execution Stops when
    - No nodes are active
    - No messages are in transit