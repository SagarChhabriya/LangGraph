# Agentic AI

Agentic AI is a type of AI that can take up a task or goal from a user and then work toward completing it on its own, with minimal human guidance. It plans, takes action, adapts to changes, and seeks help only when necessary.

## Key Characteristics

1. Autonomous
2. Goal Oriented
3. Planning
4. Reasoning
5. Adaptability
6. Context Awareness



### 1. Autonomy
Autonomy refers to the AI system's ability to make decisions and take actions on its own to achieve a given goal, without needing step-by-step human instruction.

1. Our AI recruiter is autonomous
2. It's proactive
3. Autonomy in multiple facets
    - Execution
    - Decision Making
    - Tool Usage
4. Autonomy can be controlled
    - Permission Scope: Limit what tools or actions the agent can perform independently. (Can screen candidates, but needs approval before rejecting anyone).
    - Human-in-the-loop (HITL): Insert Checkpoints where human approval is required before continuing. (Can I post this JD?).
    - Override Controls: Allow users to stop, pause, or change the agent's behavior at any time. (Pause screening command to halt resume processing)
    - Gaurdrails/Policies: Define hard rules or ethical boundaries the agent must follow. (Never schedule interviews on weekends)

5. Autonomy can be dangerous
    - The application autonomously sends out job offers with incorrect salaries or terms.
    - The application shortlists candidate by age or nationality, violating anti-discrimnation laws.
    - The applications spending extra on linkedIn ads


### 2. Goal Oriented
Being goal-oriented means that the AI system operates with a persistent objective in mind and continuously directs its actions to achieve that objective, rather than just responding to isolated prompts. 

1. Goals acts as a compass for autonomy
2. Goals can come with constraints
3. Goals are stored in core memory
4. Goals can be altered


### 3. Planning
Planning is the agent's ability to break down a high-level goal into a structured sequence of actions or subgoals and decide the best path to achieve the desired outcome. 

- Step 1: Generating multiple candidate plans
    - Plan A: Post JD on LinkedIn, GitHub Jobs, AngelList
    - Plan B: Use internal referrals and hiring agencies

- Step 2: Evaluate Each Plan 
    - Efficiency: Which is faster?
    - Tool Availability
    - Cost: Does it require premium tool?
    - Risk: Will it fail if we got no applicants?
    - Alignment with constraints

- Step 3: Select the best plan with the help of:
    - Human in the loop input
    - A pre-programmed policy

### 4. Reasoning
Reasoning is the congnitive process through which an agentic ai system interprets information, draws conclusions and make decisions; both while planning ahead and executing actions in real time.

**Reasoning During Planning**

1. Goal Decomposition: Break down abstract goals into concrete steps
2. Tool Selection: Decide which tool will be needed for which steps
3. Resource estimation: Esitmate time, dependencies, risks


**Reasoning During Execution**

1. Decision Making: Choosing between options (3 candidate match -> Schedule 2 best, reject 1)
2. HITL handling: Knowing when to pause and ask for help (Unsure about salary range) 
3. Error Handling: Interpreting tool/API failures and recovering



### 5. Adaptability
Adaptability is the agent's ability to understand, retain, and utilize relevant information, from the ongoing task, past interactions, user perferences, and environmental cues to make better decisions throughout a multi-step process.

**Types of Context**

1. The original goal
    - Progress till now + Interaction History 
    - Environment State
    - Tool Responses
    - User specific perferences
    - Policy for gaurdrails
2. Context awareness is implmeneted through memory
3. Short term memory: Current Session
4. Long term memory: System prompt/Gaurdrails

## Components of Agentic AI

1. Brain: LLM
2. Orchestrator
3. Tools
4. Memory
5. Supervisor

### 1. Brain

- Goal Interpretation: Understands user instructions and translates them into objectives
- Planning: Breaks down high-level goals into subgoals and ordered steps.
- Reasoning: Makes decisions, resolves ambiguity, and evaluates trade-offs
- Tool Selection: Chooses which tool(s) to use at a given step.
- Communication: Generates natural language outputs for human or other agents.

### 2. Orchestrator

- Task Sequencing: Deterimines the order of actions 
- Conditional Routing: Directing flow based on context (e.g., if failure, or retry or escalate)
- Retry Logic: Handles failed tool calls or reasoning attempts with backoff
- Looping & Iteration: Repeats steps (e.g., keep checking job app until 10 applications are received)
- Delegation: Decides whether to hand off work to tools, LLM, or human


### 3. Tools

- External Actions: Perform API calls (e.g., post a job, send an email, trigger onboarding)
- Knowledge base access: Retrieve factual or domain-specific information using RAG or search tools to ground responses.

### 4. Memory

- Short-Term-Memory: Maintains the active session's context; recent user messages, tool calls, and immediate decisions
- Long-Term-Memory: Persists high-level goals, past interactions, user perferences, and decisions across sessions.
- State Tracking: Monitors progress: what's completed; what's pending (e.g., JD post, Offer sent)


### 4. Supervisor

- Request Approval (HITL): Agent checks with human before high-risk actions (e.g., sending offers)
- Gaurdrails Enforcement: Blocks unsafe or non-compliant behavior
- Edge Case Escalation: Alerts human when uncertainty/conflict arises