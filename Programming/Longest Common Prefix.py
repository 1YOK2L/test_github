def longest_prefix(strs):
    if not strs:
        print("\"\"")
        return

    output = []

    for i in range(len(strs[0])):
        current_char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != current_char:
                print("\"" + "".join(output) + "\"")
                return
        
        output.append(current_char)

    print("\"" + "".join(output) + "\"")

longest_prefix(["flower", "flow", "flight"])
longest_prefix(["dog", "racecar", "car"])

# def longest_prefix(strs):
#     if not strs:
#         return ""
    
#     prefix = strs[0]
    
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if prefix == "":
#                 return ""
    
#     return prefix

# print(f'"{longest_prefix(["flower", "flow", "flight"])}"')
# print(f'"{longest_prefix(["dog", "racecar", "car"])}"')