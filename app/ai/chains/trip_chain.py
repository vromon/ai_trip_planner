# from fastapi import FastAPI, HTTPException
from app.ai.client import get_llm
from app.ai.vectorstore import get_vectorstore
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from app.ai.prompts.system_prompt import itinerary_prompt
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm = get_llm()

vectorstore = get_vectorstore()

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt = ChatPromptTemplate.from_messages([
    ("system", itinerary_prompt),
    ("human", "{input}")
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain=(
    {
    "context":retriever |format_docs, "input":RunnablePassthrough()
    }
    |prompt
    
    |llm
    
    |StrOutputParser()
    )

def invoke_chain(user_query:str)->str:
        response = rag_chain.invoke(user_query)
        return response
    





         

        
    

      


        

# @app.post("/generate-itinerary/")
# async def generate_trip_itinerary(request: ChatRequest):
    # try:
    #     # Run the single pipeline
    #     response = rag_chain.invoke({"input": request.user_input})
        
    #     return {
    #         "itinerary": response["answer"],
    #         "sourced_spots": [doc.metadata.get("text_content") for doc in response["context"]]
    #     }
        
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Itinerary generation failed: {str(e)}")


