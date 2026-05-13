from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

extracted_data = load_pdf_files(r"C:\Users\DELL\Documents\Projects\Medical-Chatbot\Medical-Chatbot\data")
filter_data = filter_to_minimal_docs(extracted_data)
texts_chunk=text_split(minimal_docs)

embedding = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


index_name = "medi-bot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    # Only upload documents if index was just created
    docsearch = PineconeVectorStore.from_documents(
        documents=texts_chunk,
        embedding=embedding,
        index_name=index_name
    )
else:
    # Index already exists, just connect to it
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embedding
    )
    