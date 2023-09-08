# Sparse Arrays

def matchingStrings(stringList, queries):
    # Write your code here
    query_count = {}
    for query in queries:
        query_count[query] = 0
    
    for string in stringList:
        if string in query_count:
            query_count[string] += 1
    result = [query_count[query] for query in queries]
    return result