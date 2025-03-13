# CSV Analyzer & Visualizer

## 📌 Overview
This project provides an interactive web application for analyzing and visualizing CSV data. It enables users to:
- Upload and explore CSV files.
- Generate various types of graphs based on selected columns.
- Ask AI-powered questions about the dataset.

The application is built using **Gradio** for the user interface and **Matplotlib** for data visualization. It also integrates **Ollama** for AI-driven data queries.

## 🚀 Features
- **CSV Upload & Preview**: Upload a CSV file and get a summary, including missing values and column data types.
- **Graph Generation**: Generate Bar, Line, and Scatter plots using selected columns.
- **AI-Powered Q&A**: Ask questions about the dataset and receive insights powered by an LLM model.

## 🛠️ Installation
### Prerequisites
Ensure you have Python installed. Install the required dependencies using:
```sh
pip install -r requirements.txt
```

### Installing Ollama & Llama 3 Model
Ollama is required to run the AI-powered Q&A feature. Follow these steps to install it:

#### 1️⃣ **Download and Install Ollama**

For Windows, download and install Ollama from [Ollama's official site](https://ollama.ai/).

#### 2️⃣ **Download Llama 3 Model**
After installing Ollama, run the following command to download the `llama3:8b` model:
```sh
ollama pull llama3:8b
```


## 📂 Project Structure
```
📦 csv-analyzer
├── app.py          # Main application file
├── utils.py        # CSV file processing utilities
├── graph.py        # Functions for data visualization
├── models.py       # AI-based question-answering logic (LLM integration)
└── README.md       # Project documentation
└── requirments.txt # Dependencies
└── data            # Sample CSV files (for testing)
```


## 🎯 Usage
Run the application with:
```sh
python app.py
```
The interface will launch in your browser.

## 📌 Functionality Breakdown
### 1️⃣ **CSV Upload & Preview** (`utils.py`)
- **`upload_csv(file)`**: Processes the CSV file and returns column details, missing values, and a data preview.

### 2️⃣ **Data Visualization** (`graph.py`)
- **`plot_graph(df, x_column, y_column, graph_type)`**: Generates bar, line, or scatter plots from selected columns.

### 3️⃣ **AI-Powered Querying** (`models.py`)
- **`generate_answer(question, df)`**: Uses an LLM to answer user queries based on the dataset.

### 4️⃣ **Application Logic** (`app.py`)
- **`process_csv(file)`**: Handles CSV upload and processing.
- **`generate_plot(x_column, y_column, graph_type)`**: Calls `plot_graph` to create graphs.
- **`answer_question(query)`**: Calls `generate_answer` for AI-driven responses.

## 🎨 UI Components
- **CSV Upload & Preview** 📂
- **Graph Generator** 📊
- **AI-Powered Data Q&A** 🤖

## 🔗 Credits
Built using:
- [Gradio](https://gradio.app/)
- [Matplotlib](https://matplotlib.org/)
- [Ollama](https://ollama.ai/)
- [Pandas](https://pandas.pydata.org/)

## 📜 License
This project is open-source. Feel free to modify and improve!
