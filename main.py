import google.generativeai as genai
import os
import json
from datetime import datetime, timedelta

# Set up the API key for Google Generative AI
os.environ["API_KEY"] = "Your_API_Key_Here"
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# List to maintain conversation history
conversation_history = []

def extract_info(query):
    """
    Extracts information from the user's query using the generative AI model.
    
    Parameters:
        query (str): The user query containing company performance metrics information.
    
    Returns:
        str: The generated response from the model containing extracted information in JSON format.
    """
    # Combine the last four messages from conversation history with the current query
    context_query = " ".join(conversation_history[-4:]) + " " + query
    
    try:
        # Generate content using the generative model
        response = model.generate_content([
            f"Extract the following information from this query: '{context_query}': "
            "1. Entity (e.g., Amazon, Flipkart), "
            "2. Parameter (e.g., GMV, revenue, profit), "
            "3. Start Date and End Date in ISO 8601 format (YYYY-MM-DD). "
            "Handle variations in spelling and abbreviations. "
            "Output in JSON format with keys: entity, parameter, startDate, endDate."
            "If the query does not mention the start date and/or end date, consider None."
        ])
        return response.text
    except Exception as e:
        print(f"Error processing query: {e}")
        return None

def process_query(query):
    """
    Processes the user's query, extracts the necessary information, and formats the output.
    
    Parameters:
        query (str): The user query to be processed.
    
    Returns:
        None
    """
    extracted_info = extract_info(query)
    if not extracted_info:
        print("Failed to extract information from the query.")
        return

    try:
        # Extract the JSON part from the model's response
        json_part = extracted_info.split("```json")[1].split("```")[0].strip()

        # Handle cases with multiple JSON objects by wrapping them in an array
        if json_part.startswith("{") and json_part.endswith("}"):
            json_part = f"[{json_part}]"

        # Parse the JSON data
        formatted_list = json.loads(json_part)

        # Set default start and end dates if not provided in the query
        for item in formatted_list:
            if item.get('startDate') is None:
                start_date = datetime.now() - timedelta(days=365)
                item['startDate'] = start_date.strftime('%Y-%m-%d')
                item['endDate'] = datetime.now().strftime('%Y-%m-%d')

            if item.get('endDate') is None:
                item['endDate'] = datetime.now().strftime('%Y-%m-%d')

        # Print formatted JSON output
        json_data = json.dumps(formatted_list, indent=4)
        print("Output:\n", json_data)

        # Append the current query to the conversation history
        conversation_history.append(query)

    except Exception as e:
        print(f"Error processing JSON: {e}")

# Main loop to interact with the user
while True:
    query = input("User Input - ")
    if query.lower() == "exit":
        break
    process_query(query)
