# QA---using-the-groq

# AI Question Answering Bot

This project is an AI-powered question answering bot built using Streamlit and the Groq API. The bot uses the `llama-3.3-70b-versatile` model to provide accurate and concise answers to user questions.

## Project Files

- `temp.py`: Contains the main code for the Streamlit application.
- `app.py`: Contains the initialization code for the Groq client.
- `app1.py`: Contains additional functionality and integration with LangChain.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your Groq API key:
      ```env
      GROQ_API_KEY=your_actual_api_key
      ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run temp.py
    ```

2. Open your browser and navigate to the local URL provided by Streamlit (e.g., `http://localhost:8501`).

3. Interact with the AI bot by typing your questions in the input field and clicking the "Get Answer" button.

## Project Structure

- [temp.py](http://_vscodecontentref_/1): Main Streamlit application file.
- [app.py](http://_vscodecontentref_/2): Groq client initialization.
- [app1.py](http://_vscodecontentref_/3): Additional functionality and integration with LangChain.

## Dependencies

- Python 3.10
- Streamlit
- Groq API
- LangChain
- dotenv

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Groq API](https://groq.com/)
- [LangChain](https://langchain.com/)
