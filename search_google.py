from googlesearch import search

def google_search(query, num_results=5):
    print(f"\n🔍 Searching Google for: {query}\n")
    
    results = search(query, num_results=num_results)
    
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result}")

# Example
if __name__ == "__main__":
    query = input("Enter your search query: ")
    google_search(query)
