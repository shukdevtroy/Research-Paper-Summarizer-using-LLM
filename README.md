# Research-Paper-Summarizer-using-LLM

This Python tool extracts text from a PDF document, summarizes it, predicts its main topic using OpenAI's GPT model, and saves the results to a text file. It's built using PyMuPDF for PDF text extraction and OpenAI's API for summarization and topic prediction.

## Features

- **Extract Text**: Extracts all text from a PDF file.
- **Summarize**: Summarizes the extracted text.
- **Predict Topic**: Predicts the main topic of the text.
- **Save Results**: Saves the summary and predicted topic to a text file.

## Prerequisites

- Python 3.x
- Libraries: `fitz` (PyMuPDF), `openai`, `python-dotenv`

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/shukdevtroy/Research-Paper-Summarizer-using-LLM.git
    cd Research-Paper-Summarizer-using-LLM
    ```

2. **Install the required Python packages**:

    ```bash
    pip install pymupdf python-dotenv fitz
    ```
    ```bash
    pip install openai==0.28
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory of the project with the following content:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Usage

1. **Place your PDF file in the project directory**.

2. **Run the script**:

    ```bash
    python summarizer.py
    ```

    Replace `your_script_name.py` with the name of the Python file containing the code.

3. **Check the output**:

    The script will output the summary and predicted topic to the console and save them in a text file with the same base name as the PDF.

## Example

Given a PDF file named `A_Wearable_Wireless_Sensor_System_Using_Machine_Learning_Classification_to_Detect_Arrhythmia.pdf`, running the script will create a file named `A_Wearable_Wireless_Sensor_System_Using_Machine_Learning_Classification_to_Detect_Arrhythmia.txt` with the following content:

    ```
    Summary:
    [Summary text here]

    Predicted Main Topic:
    [Predicted topic here]
    ```

## Functions

- **`extract_text_from_pdf(pdf_path)`**: Extracts all text from the given PDF file.
- **`ensure_full_stop(text)`**: Ensures that the text ends with a full stop.
- **`summarize_text(text)`**: Uses OpenAI GPT model to summarize the provided text.
- **`predict_topic(text)`**: Uses OpenAI GPT model to predict the main topic of the provided text.
- **`save_to_file(pdf_path, summary, topic)`**: Saves the summary and predicted topic to a text file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF text extraction.
- [OpenAI](https://openai.com) for the GPT models used for summarization and topic prediction.

---

Feel free to contribute or create issues if you encounter any problems. Happy coding!
