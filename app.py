from qa import ask_repo

question = input("Ask about the repository: ")

result = ask_repo(question)

print("\nAnswer:\n")
print(result["answer"])

print("\nSources:")

for source in result["sources"]:
    print(f"- {source}")