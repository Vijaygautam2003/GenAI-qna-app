import gradio as gr
from utils import upload_csv
from models import generate_answer
from graph import plot_graph

df=None
# Function to process the uploaded CSV file
def process_csv(file):
    global df
    result, preview, df = upload_csv(file)
    if df is None:
        return result, None, None
    return result,preview,df.head()

# Function to generate a graph based on selected columns and graph type
def generate_plot(x_column, y_column, graph_type):
    if df is None:
        return "⚠ No CSV file uploaded. Please upload a file first.", None
    return plot_graph(df, x_column, y_column, graph_type)

# Function to answer user queries about the dataset
def answer_question(query):
    if df is None:
        return "Please upload a CSV file first."
    return generate_answer(query, df)

# Interface for CSV file upload and preview
csv_interface = gr.Interface(
    fn=process_csv,
    inputs=gr.File(label="Upload your CSV 📂"),
    outputs=[
        gr.Markdown(label="File Status"),
        gr.Dataframe(label="Column Info", wrap=True),
        gr.Dataframe(label="Data Preview", wrap=True)
    ],
    title="📂 CSV Analyzer: Upload & Explore Instantly",
    description="✅ Upload your CSV file to get a quick summary! View column details, missing values, and a preview of your dataset.",
    theme="default"
)

# Interface for generating graphs from the dataset
graph_interface = gr.Interface(
    fn=generate_plot,
    inputs=[gr.Textbox(label="X-axis Column"), gr.Textbox(label="Y-axis Column"), gr.Radio(["Bar", "Line", "Scatter"], label="Graph Type")],
    outputs="image",
    title="📊 Data Visualizer: Create Stunning Graphs",
    description="Enter column names and select a chart type to bring your data to life. Generate bar, line, or scatter plots with ease!"
)

# Interface for asking AI-powered questions about the dataset
query_interface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(placeholder="Ask a question about your data..."),
    outputs="text",
    title="🤖 Smart Data Q&A: Ask Anything!",
    description="Let AI analyze your data! Ask any question about your uploaded CSV, and get instant answers based on your dataset."
)

# Combining all interfaces into a tabbed UI
gr.TabbedInterface([csv_interface, graph_interface, query_interface], ["Upload CSV", "Generate Graph", "Ask Questions"]).launch(share=True)