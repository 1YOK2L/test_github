def longest_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix

print(f'"{longest_prefix(["flower", "flow", "flight"])}"')
print(f'"{longest_prefix(["dog", "racecar", "car"])}"')