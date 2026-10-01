import chromadb;
import json;

client=chromadb.Client()

collection=client.create_collection(name = 'question')

collection.add(
    documents=["Spring Boot provides dependency injection.",
               "Kubernetes manages containerized workloads.",
                "Kafka provides event streaming.",
                "Azure Kubernetes Service provides managed Kubernetes.",
                "SQL indexes can improve database query performance."
               ],
    ids=["1","2","3","4","5"],
    metadatas=[ {"tech":"Spring Boot","catagory":"java"},
                {"tech":"Kubernetes","catagory":"cloud"},
                 {"tech":"Kafka","catagory":"message"},
                  {"tech":"Azure","catagory":"cloud"},
                   {"tech":"SQL","catagory":"database"},
               ]
)

result = collection.query(
    query_texts=["Which technology is used for event streaming?","which language in database related?"],
    n_results=2
)
pritty_result=json.dumps(result,indent=2)

print(pritty_result)