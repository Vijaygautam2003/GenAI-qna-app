import matplotlib.pyplot as plt

# Function to generate a graph based on user-selected columns and graph type
def plot_graph(df,x_column, y_column, graph_type):
    """Generates a graph based on user input and handles errors."""
    if df is None:
        return "⚠ No CSV file uploaded. Please upload a file first.",None

    try:
        plt.figure(figsize=(12, 6))
        
        # Generate the graph based on user selection
        if graph_type == "Bar":
            plt.bar(df[x_column], df[y_column], color="skyblue")
        elif graph_type == "Line":
            plt.plot(df[x_column], df[y_column], marker="o", linestyle="-", color="green")
        elif graph_type == "Scatter":
            plt.scatter(df[x_column], df[y_column], color="red")
        
        # Add labels and title to the graph
        plt.xlabel(x_column, fontsize=12)
        plt.ylabel(y_column, fontsize=12)
        plt.title(f"{graph_type} Plot of {y_column} vs {x_column}" , fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("plot.png")
        plt.close()
        
        # Return the saved plot image file
        return "plot.png"

    except Exception as e:
        return f"❌ Error generating graph: {str(e)}",None
