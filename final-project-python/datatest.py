





for i in range(len(hard_questions)):
    list = []
    list.append(hard_questions[i]['answerA'])
    list.append(hard_questions[i]['answerB'])
    list.append(hard_questions[i]['answerC'])
    list.append(hard_questions[i]['answerD'])
    hard_questions[i]['answers'] = list
    print(f'{hard_questions[i]},')
