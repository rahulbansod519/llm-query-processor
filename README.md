
# LLM-Powered Query Processor

This project is a Python-based application that uses Google Generative AI to process user queries related to company performance metrics and convert them into structured JSON format. The application can handle variations in user queries, implement error handling, and support additional date formats or relative date ranges.

## Features

- **Entity Extraction**: Extracts entities like company names (e.g., Amazon, Flipkart) from user queries.
- **Parameter Identification**: Identifies parameters like GMV, revenue, profit, etc.
- **Date Parsing**: Supports multiple date formats and relative date ranges, converting them to ISO 8601 format.
- **Contextual Understanding**: Handles variations in spelling, abbreviations, and interprets queries based on recent conversation history.

## Prerequisites

- Python 3.7+
- An API key for Google Generative AI

## Installation

1. **Clone the repository**:
   git clone https://github.com/rahulbansod519/llm-query-processor.git
   cd llm-query-processor
   

2. **Install required dependencies**:
  
   pip install google-generativeai
   

3. **Set up the API key**:
   - Replace the placeholder \`Your_API_Key_Here\` in the code with your actual API key from Google Generative AI.

## Usage

1. **Run the application**:
   \`\`\`bash
   python main.py
   \`\`\`

2. **Interact with the application**:
   - Enter queries related to company performance metrics.
   - Example queries:
     - "Get profit for March"
     - "What were the sales last month?"
     - "Analyze performance between April 5 and June 15"

3. **Exit the application**:
   - Type \`exit\` to stop the program.

## Code Structure

- \`main.py\`: The main script containing the query processing logic.
- \`README.md\`: Documentation and setup instructions for the project.

## How It Works

1. The application accepts a user query and uses the Google Generative AI model to extract relevant information.
2. The extracted information is parsed into a structured JSON format with keys such as \`entity\`, \`parameter\`, \`startDate\`, and \`endDate\`.
3. If the query lacks specific dates, default values are assigned.
4. The conversation history is maintained to provide context for subsequent queries.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

.
