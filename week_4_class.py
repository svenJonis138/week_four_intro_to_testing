# can you see the bug in this program?

def is_correct_answer(user_answer, correct_answer):
    """ Check if user's answer is the same as the correct
    answer, ignoring case """
    return user_answer.lower() == correct_answer.lower()


def main():
    question = 'How many senators in the US senate?'
    answer = 100

    print(question)
    user_answer = input('What is your answer? ')

    if is_correct_answer(user_answer, answer):
        print('Correct!')
    else:
        print(f'Sorry, the answer is {answer}')


if __name__ == '__main__':
    main()