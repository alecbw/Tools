
# firsttext ` some words ` numbers here ` yes'
# input['query']



query = input['query']
q = query.count("`")

OutputKeys = ["Company", "Date", "URL", "Onsite"]
Output = dict()

for n, val in enumerate(query.split('`', q)):
    Output[OutputKeys[n]] = val

return Output

 # = [""] * 4
# query.split('`', q)[q].strip() = map(str, ("Company", "Date", "URL", "Onsite") )

# if q == 0:
#     URL = query
# elif q == 1:
#     Company = query.split('`', 1)[0].strip()
#     URL = query.split('`', 1)[1].strip()
# elif q == 2:
#     Company = query.split('`', 2)[0].strip()
#     Date = query.split('`', 2)[1].strip()
#     URL = query.split('`', 2)[2].strip()
# elif q == 3:
#     Company = query.split('`', 3)[0].strip()
#     Date = query.split('`', 3)[1].strip()
#     URL = query.split('`', 3)[2].strip()
#     OnSite = query.split('`', 3)[3].strip()

# return {
#     'Company': Company,
#     'Date': Date,
#     'URL': URL,
#     'On Site': OnSite,
# }


# sa, sb,sc = map(str, (a,b,c) )
