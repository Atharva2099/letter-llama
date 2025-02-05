# Cover Letter Generator

A Streamlit web application that generates customized cover letters using a fine-tuned LLM model through Ollama.

## Features
- Customizable cover letter generation
- User-friendly interface
- Integration with Ollama for local LLM inference
- Dark mode UI
- Download options in multiple formats

## Setup
1. Install required packages:
```bash
pip install streamlit requests
```

2. Install Ollama from https://ollama.ai/

3. Create the custom model in Ollama:
```bash
# Create Modelfile
echo "FROM llama3.2:3b
ADAPTER /path/to/your/model" > Modelfile

# Create custom model
ollama create coverletter-custom -f Modelfile
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage
1. Fill in the job details and your information
2. Adjust generation settings if needed
3. Click "Generate Cover Letter"
4. Review and download the generated cover letter

## Requirements
- Python 3.10+
- Streamlit
- Ollama
- Internet connection for model download