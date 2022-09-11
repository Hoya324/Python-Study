def solution(citations):
    citations = sorted(citations, reverse=True)
    for idx, citation in enumerate(citations):
        if citation <= idx:
            return idx
    return len(citations)