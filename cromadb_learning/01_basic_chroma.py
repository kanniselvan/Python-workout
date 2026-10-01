import chromadb;
import json;

#client= chromadb.Client()
client= chromadb.PersistentClient()


collection = client.create_collection(name = 'employee')

collection.add(
    documents=[
        "David is the father of Sarah and Michael.",
        "Sarah is the mother of Emily.",
        "Michael is the uncle of Emily and father of James.",
        "Jessica is married to David and is the mother of Sarah and Michael.",
        "Emily and James are cousins."
    ],
     metadatas=[
        {"generation": "1", "gender": "male"},    # David
        {"generation": "2", "gender": "female"},  # Sarah
        {"generation": "2", "gender": "male"},    # Michael
        {"generation": "1", "gender": "female"},  # Jessica
        {"generation": "3", "relation": "cousins"} # Emily & James
    ],
    ids=["f1", "f2", "f3", "f4", "f5"]
)

result=collection.query(
    query_texts = ["Who is Emily cousins"],
    n_results=1
)

pritty_json=json.dumps(result,indent=2)

print(pritty_json)