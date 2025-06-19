questions = [
    {
        "question": "Question 1: What’s the main advantage of custom tool behavior functions?",
        "answer": "They allow precise control over how an agent interacts with tools.",
        "example": "You can prioritize tools based on context dynamically."
    },
    {
        "question": "Question 2: Which method is used to execute an agent asynchronously?",
        "answer": "run_async()",
        "example": "Useful in event loops like asyncio apps."
    },
    {
        "question": "Question 3: What’s the purpose of RunContextWrapper?",
        "answer": "It adds extra metadata and behavior to the run context.",
        "example": "Used to monitor or modify the run environment."
    },
    {
        "question": "Question 4: What does Runner.run_sync() do?",
        "answer": "Executes the agent synchronously.",
        "example": "Ideal for blocking or sequential workflows."
    },
    {
        "question": "Question 5: What does extra='forbid' do in a Pydantic model config?",
        "answer": "Disallows unexpected extra fields.",
        "example": "Raises validation error if unexpected fields are passed."
    },
    {
        "question": "Question 6: What's the main advantage of strict schemas over non-strict?",
        "answer": "They enforce data types and structures strictly.",
        "example": "Reduces risk of invalid data entering the model."
    },
    {
        "question": "Question 7: What happens when you combine StopAtTools with multiple tool names?",
        "answer": "The agent stops once any of the specified tools are used.",
        "example": "Use StopAtTools([\"search\", \"summarize\"]) to stop on first of either."
    },
    {
        "question": "Question 8: What is the purpose of context in the OpenAI Agents SDK?",
        "answer": "It passes runtime state and environment data to the agent.",
        "example": "Context can include user input, memory, or tool outputs."
    },
    {
        "question": "Question 9: What's the key consideration when choosing between different tool_use_behavior modes?",
        "answer": "Performance vs. control trade-off.",
        "example": "Use stop_on_first_tool for speed, or run_llm_again for control."
    },
    {
        "question": "Question 10: What information does handoff_description provide?",
        "answer": "It explains the reason and data when handing off to another system or agent.",
        "example": "Useful in human-in-the-loop workflows."
    },
    {
        "question": "Question 11: What does ToolsToFinalOutputResult.is_final_output indicate?",
        "answer": "Indicates whether the tool produced the final answer.",
        "example": "Used to determine agent's stopping point."
    },
    {
        "question": "Question 12: What’s the difference between hosted tools and function tools in terms of tool_use_behavior?",
        "answer": "Hosted tools run remotely; function tools run locally.",
        "example": "Use hosted tools for APIs, function tools for custom logic."
    },
    {
        "question": "Question 13: How do you convert an agent into a tool for other agents?",
        "answer": "Wrap it using the as_tool() method.",
        "example": "agent_tool = agent.as_tool()"
    },
    {
        "question": "Question 14: What method returns all tools available to an agent?",
        "answer": "get_tools()",
        "example": "Call agent.get_tools() to list them."
    },
    {
        "question": "Question 15: What is the first parameter of every function tool?",
        "answer": "The context object.",
        "example": "def my_tool(context, ...):"
    },
    {
        "question": "Question 16: What is the purpose of the get_system_prompt() method?",
        "answer": "To provide initial instructions or role for the agent.",
        "example": "Used to customize system-level behavior."
    },
    {
        "question": "Question 17: What’s the difference between InputGuardrail and OutputGuardrail?",
        "answer": "InputGuardrail validates inputs; OutputGuardrail checks outputs.",
        "example": "Use both to protect against invalid data."
    },
    {
        "question": "Question 18: What is the primary purpose of the instructions parameter in an Agent?",
        "answer": "To guide the agent’s behavior and tone.",
        "example": "instructions=\"Answer concisely and politely.\""
    },
    {
        "question": "Question 19: What does the reset_tool_choice parameter control?",
        "answer": "Whether to reset tool selection between steps.",
        "example": "Set to True to allow reevaluation each turn."
    },
    {
        "question": "Question 20: What happens if a function tool raises an exception?",
        "answer": "The agent receives an error message and may retry.",
        "example": "Handle exceptions with try/except in tools."
    },
    {
        "question": "Question 21: What does the clone() method do?",
        "answer": "Creates a copy of the agent or runner.",
        "example": "Useful when branching logic or sessions."
    },
    {
        "question": "Question 22: What is ToolsToFinalOutputFunction in the OpenAI Agents SDK?",
        "answer": "A callable that defines how tool results become final answers.",
        "example": "Customize it to change how answers are finalized."
    },
    {
        "question": "Question 23: What is the return type of Runner.run()?",
        "answer": "RunResult",
        "example": "Includes final output, steps, and tool use."
    },
    {
        "question": "Question 24: What happens if a custom tool behavior function returns is_final_output=False?",
        "answer": "The agent continues to the next step.",
        "example": "Use when more tools need to be used."
    },
    {
        "question": "Question 25: When would you use StopAtTools instead of stop_on_first_tool?",
        "answer": "When stopping depends on specific tools only.",
        "example": "More control vs. global stop behavior."
    },
    {
        "question": "Question 26: What is the default value for tool_use_behavior in an Agent?",
        "answer": "run_llm_again",
        "example": "It runs the LLM again after each tool result."
    },
    {
        "question": "Question 27: What’s the key difference between run_llm_again and stop_on_first_tool in terms of performance?",
        "answer": "stop_on_first_tool is faster; run_llm_again is more flexible.",
        "example": "Use run_llm_again for multi-tool reasoning."
    },
    {
        "question": "Question 28: Which Pydantic v2 decorator is used for field validation?",
        "answer": "@field_validator",
        "example": "Use to validate a single field's value."
    },
    {
        "question": "Question 29: What is the purpose of model_settings in an Agent?",
        "answer": "To customize schema validation and behavior.",
        "example": "Control strictness, defaults, etc."
    },
    {
        "question": "Question 30: How do you enable non-strict mode for flexible schemas?",
        "answer": "Set strict=False in model config.",
        "example": "Allows extra fields and loose types."
    },
    {
        "question": "Question 31: What does the handoff_description parameter do?",
        "answer": "Explains the handoff context when stopping agent execution.",
        "example": "Displayed in UI or logs."
    },
    {
        "question": "Question 32: How do you implement schema evolution while maintaining backward compatibility?",
        "answer": "Use versioned models and optional fields.",
        "example": "Avoid breaking changes in updates."
    },
    {
        "question": "Question 33: Can dynamic instructions be async functions?",
        "answer": "Yes, they can return a string asynchronously.",
        "example": "Useful for fetching user-specific data."
    },
    {
        "question": "Question 34: What happens when tool_use_behavior is set to 'stop_on_first_tool'?",
        "answer": "Agent stops after the first tool is used.",
        "example": "Best for fast single-step tasks."
    },
    {
        "question": "Question 35: What’s the difference between mutable and immutable context patterns?",
        "answer": "Mutable allows changes during runs; immutable does not.",
        "example": "Choose based on state-tracking needs."
    },
    {
        "question": "Question 36: What causes the error 'additionalProperties should not be set for object types'?",
        "answer": "Occurs when extra fields are not allowed in schema.",
        "example": "Fix with extra='allow' in config."
    },
    {
        "question": "Question 37: When should you use non-strict schemas over strict schemas?",
        "answer": "When flexibility is more important than validation.",
        "example": "Early prototyping or external APIs."
    },
    {
        "question": "Question 38: In a custom tool behavior function, what parameters does it receive?",
        "answer": "Usually context, tool result, and agent state.",
        "example": "def behavior(ctx, result, state): ..."
    },
    {
        "question": "Question 39: What does Runner.run_streamed() return?",
        "answer": "A generator that yields events in real time.",
        "example": "Useful for live UI feedback."
    },
    {
        "question": "Question 40: How do you create dynamic instructions that change based on context?",
        "answer": "Provide a function to the instructions parameter.",
        "example": "def dynamic_instructions(ctx): return \"Hi!\""
    }
    
]

