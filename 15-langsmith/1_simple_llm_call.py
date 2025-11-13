from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv()

# Define the prompt template
prompt = PromptTemplate.from_template("{question}")

# Initialize the model using the OpenRouter API base and API key
model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite')

# Create a string output parser
parser = StrOutputParser()

# Create the chain: prompt → model → parser
chain = prompt | model | parser

# Run the chain with a specific question
result = chain.invoke({"question": "What is the capital of Peru?"})

# Print the result
print(result)
