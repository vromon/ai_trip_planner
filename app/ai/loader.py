from langchain_community.document_loaders.csv_loader import CSVLoader
def get_csv_loader(csv:str,metadata:list)->CSVLoader:
    return CSVLoader(
    file_path=csv,
    metadata_columns=metadata
)