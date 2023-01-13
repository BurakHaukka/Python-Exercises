def judgement():
    judg1 = int(input("Judge 1: "))
    judg2 = int(input("Judge 2: "))
    judg3 = int(input("Judge 3: "))
    judg4 = int(input("Judge 4: "))
    judg5 = int(input("Judge 5: "))
    
    score = [judg1, judg2, judg3, judg4, judg5]
    score.remove(max(score))
    score.remove(min(score))
    final_score = sum(score)
    print(final_score)

judgement()
    