# def max_of_three(a,b,c):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     elif a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c
# result = max_of_three(4,10,2)
# print(result)

# def average(a,b,c):
#     return(a+b+c)/3
# sum = average(4,10,20)
# print(sum)

# words = input("Enter a word: ")
# def count_characters (word):
#     return len(word)
# chars = count_characters(words)
# print(chars)

with open('unique_words.txt','r') as file:
    content = file.read()
print(content)
words = content.split('\n')
def unique_words(word_list):
   word_count= {}
   for index in word_list:
       if index in word_count:
           word_count[index] += 1
       else:
           word_count[index] = 1
   return word_count
word_counts = unique_words(words)
print(word_counts)