def build_qa():
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.chains import RetrievalQA
    from langchain_community.llms import HuggingFacePipeline
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

    # Load Docs
    loader = PyPDFLoader("docs/myfile.pdf")
    docs = loader.load()

    # Embeddings
    embed = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # FAISS
    db = FAISS.from_documents(docs, embed)
    retriever = db.as_retriever()

    # LLM
    model_name = "google/flan-t5-base"
    tok = AutoTokenizer.from_pretrained(model_name)
    mod = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    pipe = pipeline("text2text-generation", model=mod, tokenizer=tok)
    llm = HuggingFacePipeline(pipeline=pipe)

    # QA chain
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
import streamlit as st

st.title("📚 RAG QA Chatbot")

qa = build_qa()

question = st.text_input("Ask something from the document:")

if st.button("Ask"):
    if question:
        ans = qa.invoke(question)["result"]
        st.write("### ✅ Answer:")
        st.write(ans)
