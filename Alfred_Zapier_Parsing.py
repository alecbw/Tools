
# e.g. firsttext ` some words ` numbers here ` yes'




query = input['query']
q = query.count("`")

OutputKeys = ["Company", "Date", "URL", "Onsite"]
Output = dict()

for n, val in enumerate(query.split('`', q)):
    Output[OutputKeys[n]] = val

print Output
return Output

