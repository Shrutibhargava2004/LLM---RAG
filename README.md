# LLM-RAG-Function-Executor 🚀

LLM-RAG-Function-Executor is a Python-based API that dynamically retrieves and executes functions using LLM (Large Language Models) with RAG (Retrieval-Augmented Generation). The project leverages ChromaDB for semantic search, Sentence Transformers for embeddings, and FastAPI for API development. It provides a seamless experience for both function generation and execution with real-time output display.

## ✅ Features

* **Function Retrieval with AI:** Efficiently search and retrieve functions using AI-powered semantic similarity.
* **Execute Functions Dynamically:** Run functions with one click and display results.
* **Real-Time Output:** Display real-time results, such as system resource usage.
* **ChromaDB Integration:** Store and query function metadata using ChromaDB.
* **FastAPI Backend:** Perform fast and asynchronous API requests.
* **Responsive UI:** Simple and intuitive frontend using Jinja templates and CSS.

## 🧑‍💻 Tech Stack

* Python
* FastAPI
* ChromaDB
* Sentence Transformers
* Jinja2
* JavaScript & CSS

## 📦 Prerequisites

Ensure you have the following installed:

* Python 3.8+
* pip
* Git
* ChromaDB
* Sentence Transformers

## 🚀 Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Shrutibhargava2004/LLM-RAG-Function-Executor.git](https://github.com/Shrutibhargava2004/LLM-RAG-Function-Executor.git)
    cd LLM-RAG-Function-Executor
    ```
2.  **Create a Virtual Environment**
    ```bash
    python -m venv env
    # On Linux/macOS
    source env/bin/activate
    # On Windows
    env\Scripts\activate
    ```
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Start the Server**
    ```bash
    uvicorn main:app --reload
    ```
5.  **Access the Application**
    Open your browser and go to:
    http://localhost:8000

## 🧪 How to Use

1.  **Enter a Query:** Provide a simple query like "Open Chrome" or "Get CPU Usage" using the input field.
2.  **Generate Code:** Click on the **Generate Code** button. The app will retrieve the most relevant function using AI.
3.  **View Details:** View the function name, description, and its generated code.
4.  **Execute Function:** Click the **Execute Function** button to run the function.
5.  **Display Output:** Real-time output (e.g., CPU Usage) will be displayed below the button.

## 🗂️ Project Structure

```bash
LLM-RAG-Function-Executor/
├── main.py                      # Main FastAPI server
├── automation_functions.py      # Predefined functions (e.g., open browser, get CPU usage)
├── static/
│   ├── style.css                # Frontend styling
├── templates/
│   ├── index.html               # Frontend template
├── chroma_db/                   # ChromaDB storage
├── requirements.txt             # Project dependencies

```
## ⚙️ Example Functions

Here are some example functions included in the `automation_functions.py` file:

* **Open Chrome:** Launches Google Chrome using `open_chrome()`
* **Get CPU Usage:** Displays the current CPU usage using `get_cpu_usage()`
* **Get System Info:** Retrieves basic system information using `get_system_info()`

You can add custom functions in the `automation_functions.py` file and register them using ChromaDB.

## 🚦 API Endpoints

* **POST /execute**
    * **Input:** Query string
    * **Output:** Function details and generated code
* **POST /run**
    * **Input:** Function name
    * **Output:** Execution result
* **GET /**
    * Serve the frontend HTML

## 🛡️ Important Notes

* Ensure that the modules corresponding to the functions are correctly installed and imported.
* Use responsibly, especially when executing system-level functions.
* Functions like `open_chrome()` or `get_cpu_usage()` require appropriate permissions on your system.

## 🚀 Future Enhancements

* Add support for function parameter input.
* Implement detailed logging and error handling.
* Support for remote function execution.
* Enhance the UI for a more interactive experience.
