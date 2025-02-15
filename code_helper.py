# %%
from langchain_community.llms import Ollama
import sys

# Initialize Ollama with the Llama model
llm = Ollama(model="codellama")  # Change to your model name if needed

def determine_task(user_request, code):
    """
    Uses Llama via LangChain to determine which task (DOCUMENT, OPTIMIZE, DEBUG) to perform.
    """
    prompt = f"""
    You are an AI assistant for coding tasks. Based on the user request and the given code snippet, choose one task. Think twice before you select one task.
    - DOCUMENT: If the user wants docstrings or documentation.
    - OPTIMIZE: If the user wants performance or readability improvements. 
    - DEBUG: If the user asks to find and fix errors.

    User Request: "{user_request}"
    Code snippet: "{code[:500]}"  # Limit snippet length

    Respond with only one word: DOCUMENT, OPTIMIZE, or DEBUG.
    """

    task = llm.invoke(prompt).strip().upper()
    print(task)
    return task if task in ["DOCUMENT", "OPTIMIZE", "DEBUG"] else "Sorry didn't quite understand the request. Could you be more specific?" # Default fallback

def document_code(source_code):
    """
    Generates docstrings for functions/classes missing documentation.
    """
    prompt = f"""
    Add detailed Python docstrings to all functions and classes in the following code:
    
    {source_code}
    
    Return the modified code with docstrings.
    """
    return llm.invoke(prompt)

def optimize_code(source_code):
    """
    Optimizes the given Python code for clarity, readability, and performance.
    """
    prompt = f"""
    Improve the efficiency and readability of the following Python code:

    {source_code}

    Return the optimized version of the code.
    """
    return llm.invoke(prompt)

def debug_code(source_code):
    """
    Finds bugs and provides a debugging report.
    """
    prompt = f"""
    Analyze the following Python code and identify any bugs or errors.
    Suggest fixes and improvements.
    
    {source_code}

    Provide a debugging report with explanations.
    """
    return llm.invoke(prompt)

def determine_task(user_request, code):
    """
    Dummy implementation: Decides the task based on keywords in the user request.
    In production, this would use your LLM to decide between DOCUMENT, OPTIMIZE, or DEBUG.
    """
    req = user_request.lower()
    if "document" in req:
        return "DOCUMENT"
    elif "optimize" in req:
        return "OPTIMIZE"
    elif "debug" in req or "find bugs" in req:
        return "DEBUG"
    else:
        return "DOCUMENT"


def main():
    print("=== AI Code Assistant (LangChain + Ollama) ===")
    user_request = input("Enter your request (e.g., 'document my code', 'optimize my code', 'find bugs'): ")
    filename = input("Enter the filename of the Python code to process: ").strip()
    output_filename = input("Enter the output filename (for the processed code): ").strip()

    try:
        with open(filename, 'r', encoding="utf-8") as f:
            source_code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Decide the task
    chosen_task = determine_task(user_request, source_code)
    print(f"\n[AI Decision] Task chosen: {chosen_task}\n")

    # Execute the chosen task
    if chosen_task == "DOCUMENT":
        result = document_code(source_code)
        print("=== Documentation Result ===")
    elif chosen_task == "OPTIMIZE":
        result = optimize_code(source_code)
        print("=== Optimized Code ===")
    elif chosen_task == "DEBUG":
        result = debug_code(source_code)
        print("=== Debugging Report ===")
    else:
        result = "No valid task selected."

    print("\nResult:\n", result)
    
    # Write the result to the specified output file.
    try:
        with open(output_filename, 'w', encoding="utf-8") as f:
            f.write(result)
        print(f"\nOutput successfully saved to {output_filename}")
    except Exception as e:
        print(f"\nError writing to file: {e}")

if __name__ == "__main__":
    main()

