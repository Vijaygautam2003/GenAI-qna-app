import pandas as pd

# CSV Processing
def upload_csv(file):
    """Uploads CSV and validates it with better UI elements."""
    
    if file is None:
        return "⚠ No file uploaded.", None, None

    try:
        df = pd.read_csv(file)

        # Check if CSV is empty
        if df.empty:
            return "⚠ The uploaded CSV file is empty.", None, None

        # Check missing values
        missing_values = df.isnull().sum().sum()
        column_info = df.dtypes.reset_index()
        column_info.columns = ["Column Name", "Data Type"]

        # Prepare markdown output for better readability
        result = f"✅ **File loaded successfully!**\n\n"
        result += f"🔍 **Missing Values:** `{missing_values}`\n\n"
        result += f"📊 **Column Information:**"

        # Display structured column info & data preview
        return result, column_info, df.head()  

    except Exception as e:
        return f"❌ **Error loading file:** `{str(e)}`", None, None