import fitz  # PyMuPDF
import openai
import os
from dotenv import load_dotenv 
load_dotenv()

# Retrieve your OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to ensure the summary ends with a full stop
def ensure_full_stop(text):
    text = text.strip()
    if not text.endswith(('.', '!', '?')):
        text += '.'
    return text

# Function to summarize text using OpenAI GPT model
def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=500,
        temperature=0.5
    )
    summary = response.choices[0].message['content'].strip()
    return ensure_full_stop(summary)

# Function to predict the main topic of the text
def predict_topic(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"What is the main topic of the following text?\n\n{text}"}
        ],
        max_tokens=500,
        temperature=0.5
    )
    topic = response.choices[0].message['content'].strip()
    return topic

# Function to save summary and main topic to a text file
def save_to_file(pdf_path, summary, topic):
    # Create a text file with the same name as the PDF
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_file_path = os.path.join(os.path.dirname(pdf_path), f"{base_name}.txt")
    
    with open(txt_file_path, 'w') as file:
        file.write(f"Summary:\n{summary}\n\n")
        file.write(f"Predicted Main Topic:\n{topic}\n")
    
    print(f"Summary and topic saved to: {txt_file_path}")

# Main function
def main(pdf_path):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    if len(text) > 1000:
        # Summarize the text
        summary = summarize_text(text)
        print("Summary:")
        print(summary)
        
        # Predict the main topic
        topic = predict_topic(text)
        print("Predicted main topic:")
        print(topic)
        
        # Save the summary and main topic to a text file
        save_to_file(pdf_path, summary, topic)
    else:
        print("The document is too short for meaningful analysis.")

# Example usage
if __name__ == "__main__":
    pdf_path = 'A Wearable Wireless Sensor System Using Machine Learning Classification to Detect Arrhythmia.pdf'
    main(pdf_path)
