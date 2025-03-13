import ollama
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


# Function to generate an answer based on a user query and the dataset
def generate_answer(question,df):
    """Handles errors when querying CSV with LLM."""
    # global global_df
    if df is None:
        return "⚠ No CSV file uploaded. Please upload a file first."
    
    # Check if the question is empty or contains only whitespace
    if not question.strip():
        return "⚠ Question cannot be empty. Please ask something."

    try:
        # Convert the first 10 rows of the dataset to a string for context
        sample_data = df.head(10).to_string()
        # Construct the prompt for the LLM
        prompt = f"Dataset:\n{sample_data}\n\nQuestion: {question}\nAnswer:"
        # Query the LLM model with the generated prompt
        response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
        # Extract and return the model's response
        return response['message']['content']

    except Exception as e:
        return f"❌ Error processing query: {str(e)}"