import pandas as pd

def read_excel(file_path):
    """Reads an Excel file and returns a DataFrame."""
    df = pd.read_excel(file_path)
    return df

def process_and_save_files(df):
    """Processes the Excel data and creates .md files based on the first and second column values."""
    for index, row in df.iterrows():
        file_name = f"{row[0]}.md"  # First column as file name
        content = str(row[1])  # Second column as content
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
    print(f"{len(df)} files created successfully.")

# Example usage
if __name__ == "__main__":
    input_file = "data.xlsx"
    
    # Read the Excel file
    data = read_excel(input_file)
    
    # Process and create files
    process_and_save_files(data)
