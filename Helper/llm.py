# Import Azure OpenAI
from langchain_openai import AzureOpenAI

# Create an instance of Azure OpenAI
# Replace the deployment name with your own
llm = AzureOpenAI(
    deployment_name="gpt-35-turbo-instruct-0914",
)

# Run the LLM
llm.invoke("Tell me a joke")