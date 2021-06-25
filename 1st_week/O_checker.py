# 내 코드

def checker(word):
    temp = []
    for j in range(len(word)):
        if j==len(word)-1:
            if word[j] in temp:
                return 0
            else:
                return 1
        else:
            if word[j] == word[j+1]:
                continue
            if word[j] not in temp:
                temp.append(word[j])
            elif word[j] in temp:
                return 0


tcase = int(input())
count = 0

for i in range(tcase):
    word = input()
    count += checker(word)
print(count)

#==========================================================

# 숏코딩

# N=int(input())
# answer=0

# for i in range(N):
#     word = input()
#     for j in range(len(word)):
#         if j!=len(word)-1:
#             if word[j]==word[j+1]:
#                 pass
#             elif word[j] in word[j+1:]:
#                 break
#         else:
#             answer+=1
# print(answer)