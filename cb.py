# from ollama import Client
# import json
# import chromadb
# from langchain_text_splitters import RecursiveCharacterTextSplitter 

# client = chromadb.Client()
# remote_client = Client(host=f"http://localhost:11434")
# collection = client.get_or_create_collection(name="articles_demo")
# text_splitter=RecursiveCharacterTextSplitter(
#     chunk_size=200, chunk_overlap=20
# )

# print("Reading articles.jsonl and generating embeddings...")
# with open("articles.jsonl", "r") as f:
#     for i, line in enumerate(f):
#         article = json.loads(line)
#         content = article["content"]
#         sentences=text_splitter.split_text(content)

#         for each_sentence in sentences:

#             response = remote_client.embed(model="nomic-embed-text", input=f"search_document: {content}")
#             embedding = response["embeddings"][0]

#             collection.add(
#                 ids=[f"article_{i}"],
#                 embeddings=[embedding],
#                 documents=[content],
#                 metadatas=[{"title": article["title"]}],
#         )

# print("Database built successfully!")


# # query = "what are different problems provinces of nepal are facing?"
# query = "are there any predicted hindrance for upcoming election ?"
# query_embed = remote_client.embed(model="nomic-embed-text", input=f"query: {query}")["embeddings"][0]
# results = collection.query(query_embeddings=[query_embed], n_results=1)
# print(f"\nQuestion: {query}")
# print(f'\n Title : {results["metadatas"][0][0]["title"]} \n {results["documents"][0][0]} ')

# from ollama import Client
# import json
# import chromadb
# from langchain_text_splitters import RecursiveCharacterTextSplitter 

# client = chromadb.Client()
# remote_client = Client(host=f"http://localhost:11434")
# collection = client.get_or_create_collection(name="articles_demo")
# text_splitter=RecursiveCharacterTextSplitter(
#     chunk_size=200, chunk_overlap=20
# )
# with open("counter.txt", "r") as f:
#     counter=int(f.read().strip())

# # if not os.path.exists("chroma"):
# print("Reading articles.jsonl and generating embeddings...")
# with open("articles.jsonl", "r") as f:
#     for i, line in enumerate(f):
#         if i<counter:
#             print("skipping article", i)
#             continue
#         count+=1
#         article = json.loads(line)
#         content = article["content"]
#         sentences=text_splitter.split_text(content)

#             for each_sentence in sentences:

#                 response = remote_client.embed(model="nomic-embed-text", input=f"search_document: {content}")
#                 embedding = response["embeddings"][0]

#                 collection.add(
#                     ids=[f"article_{i}"],
#                     embeddings=[embedding],
#                     documents=[each_sentence],
#                     metadatas=[{"title": article["title"]}],
#         )
      
# print("Database built successfully!")
# with open("counter.txt", "w") as f:
#     f.write(str(counter))
# # query = "what are different problems provinces of nepal are facing?"
# query = "are there any predicted hindrance for upcoming election ?"
# query_embed = remote_client.embed(model="nomic-embed-text", input=f"query: {query}")["embeddings"][0]
# results = collection.query(query_embeddings=[query_embed], n_results=1)
# print(f"\nQuestion: {query}")
# print(f'\n Title : {results["metadatas"][0][0]["title"]} \n {results["documents"][0][0]} ')


# from ollama import Client
# import json
# import chromadb
# from langchain_text_splitters import RecursiveCharacterTextSplitter



# client = chromadb.Client()
# remote_client = Client(host="http://localhost:11434")
# collection = client.get_or_create_collection(name="articles_demo")

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=20
# )

# # Safe counter loading
# try:
#     with open("counter.txt", "r", encoding="utf-8") as f:
#         counter = int(f.read().strip())
# except:
#     counter = 0

# print("Reading article.json and generating embeddings...")

# with open("art.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# for i, article in enumerate(data):
#         content = article["summary"]

#         sentences = text_splitter.split_text(content)

#         for each_sentence in sentences:

#             # Embed the sentence (NOT full content)
#             embedding = remote_client.embed(
#                 model="nomic-embed-text",
#                 input=f"search_document: {each_sentence}"
#             )["embeddings"][0]

#             collection.add(
#                 ids=[f"article_{counter}"],
#                 embeddings=[embedding],
#                 documents=[each_sentence],
#                 metadatas=[{"title": article["title"]}],
#             )

#             counter += 1

# print("Database built successfully!")

# # Save counter
# with open("counter.txt", "w", encoding="utf-8") as f:
#     f.write(str(counter))


# # Query
# query = "are there any predicted hindrance for upcoming election ?"

# query_embed = remote_client.embed(
#     model="nomic-embed-text",
#     input=f"query: {query}"
# )["embeddings"][0]

# results = collection.query(query_embeddings=[query_embed], n_results=1)

# print("\nQuestion:", query)
# print("\nTitle:", results["metadatas"][0][0]["title"])
# print(results["documents"][0][0])

# context='\n'.join(results["documents"][0])

# prompt=f"""You are a helpful assistant. Answer the question based on the context provided. Use the information in the context to form your answer. If context does not have enough information just say "I don't know"

# Context: {context}

# Question: {query}

# Answer:"""

# response = remote_client.generate(
#     model="qwen3:4b-q4_K_M",
#     prompt=prompt,
#     options={
#         "temperature": 0.1
#     }
# )
# print(prompt)
# answer = response['response']

# print(answer)



# Chatbot code
from ollama import Client
import json
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

client = Client(host="http://localhost:11434")

client = chromadb.Client()
remote_client = Client(host="http://localhost:11434")
collection = client.get_or_create_collection(name="articles_demo")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

# Safe counter loading
try:
    with open("counter.txt", "r", encoding="utf-8") as f:
        counter = int(f.read().strip())
except:
    counter = 0

print("Reading article.json and generating embeddings...")

with open("art.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i, article in enumerate(data):
        content = article["summary"]

        sentences = text_splitter.split_text(content)

        for each_sentence in sentences:

         
            embedding = remote_client.embed(
                model="nomic-embed-text",
                input=f"search_document: {each_sentence}"
            )["embeddings"][0]

            collection.add(
                ids=[f"article_{counter}"],
                embeddings=[embedding],
                documents=[each_sentence],
                metadatas=[{"title": article["title"]}],
            )

            counter += 1

print("Database built successfully!")

# Save counter
with open("counter.txt", "w", encoding="utf-8") as f:
    f.write(str(counter))


    
# Query
#query = "are there any predicted hindrance for upcoming election ?"

while True:
    print("-------------------------------------------------")
    query = input("🤖How may I help you? \n ")

    if query== "exit":
        break
    
    query_embed = remote_client.embed(
        model="nomic-embed-text",
        input=f"query: {query}"
    )["embeddings"][0]

    results = collection.query(query_embeddings=[query_embed], n_results=1)

    print("\nQuestion:", query)
    print("\nTitle:", results["metadatas"][0][0]["title"])
    print(results["documents"][0][0])

    context='\n'.join(results["documents"][0])

    prompt=f"""You are a helpful assistant. Answer the question based on the context provided. Use the information in the context to form your answer. If context does not have enough information just say "I don't know"

    Context: {context}

    Question: {query}

    Answer:"""

    import ollama

    # prompt = "Are there any predicted hindrances for the upcoming election?"

    response = ollama.generate(
        model="freehuntx/qwen3-coder:14b",
        prompt=prompt,
        options={
            "num_predict": 300,
            "temperature": 0
        }
    )

    print(response["response"])