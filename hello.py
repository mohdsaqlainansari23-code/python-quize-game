# project: ask Question and Answer 

qa_pairs = []

for i in range(3):
   Question = input("Enter Question ")
   Answer = input("Answer ")
   qa_pairs.append([Question , Answer])

score = 0
for pairs in qa_pairs:
   user_answer = input(pairs[0] + " ")

   if user_answer.strip().lower() == pairs[1].strip().lower():
     print("correct")
     score = score + 1


   else:
    print("incorrect. the answer is:", pairs[1])

print("Your score:", score, "out of", len(qa_pairs))
