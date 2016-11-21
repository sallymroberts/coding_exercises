import json
from math import ceil

def read_answers(answer_file):
    """ Read answers from file and accumulate user score and answer data
        Arguments:
        answer_file [String] json format, each line identifies whether
                             a user's answer to a question is correct

        Returns: [Tuple] containing 2 elements:
            user_scores [List] contains tuples of score, user id
            answers     [Dict] 
                key:   [String] question
                value: [Dict] Users grouped by correct/incorrect answers:
                    2 keys: [String] "correct users" and "incorrect users"
                    values: [List] id's of users 
    """
    # Create answer list from answer file
    answers_file = open(answer_file)
    answers_text = answers_file.read()
    answers_file.close()
    answer_list = json.loads(answers_text)

    # Initialize values
    sv_user_id = None
    user_scores = []
    answers = {}

    # Accumulate user score and answer data needed to calculate item discrimination
    for answer in answer_list:
        # Process change of user id
        if answer['user_id'] != sv_user_id:
            # Calculate and store score of previous user
            if sv_user_id is not None:
                score = set_user_score(sv_user_id, correct_count, ans_count)
                user_scores.append((score, sv_user_id))
        
            # Setup new user
            sv_user_id = answer['user_id']
            ans_count = 0
            correct_count = 0

        # For current user, accumulate counts of all answers and correct answers
        ans_count += 1
        if answer['correct'] is True:
            correct_count += 1

        # For each question, build user id lists for correct, incorrect answers
        question = (answer['question'])
        correct = (answer['correct'])
        
        answers[question] = answers.get(question, {"correct users": [], "incorrect users": []})
        if correct:
            answers[question]["correct users"].append(sv_user_id)
        else:
            answers[question]["incorrect users"].append(sv_user_id)
        
    # Calculate and store score of last user
    score = set_user_score(sv_user_id, correct_count, ans_count)
    user_scores.append((score, sv_user_id))
 
    return (user_scores, answers)

def set_user_score(user_id, correct_count, ans_count):
    """ Set user score for all questions answered (ignore unanswered questions)
        Arguments:
        user_id       [Integer]
        correct_count [Integer] count of user's correct answers
        ans_count     [Integer] count of all of user's answers

        Returns:
        score [Float] User's percent of correct answers
    """  
    if correct_count == 0:
        score = 0
    else:
        score = 100 * (correct_count / ans_count)
    return score

def get_cohorts(user_scores):
    """ Get top and bottom cohorts from user scores
        Arguments:
        user_scores [List] contains tuples of score, user id

        Note: Divide all users into 3 equal cohorts based on scores.
              If not evenly divisible by 3, make top and bottom cohorts equal 
              in size because these are used for calculating item discrimination. 
              Handle identical scores across cohort boundaries 
              by including id in sort to provide predictable results.
        Returns:
        [Tuple] with 2 elements:
                top_cohort    [Set] user id's with scores in top third
                bottom_cohort [Set] user id's with scores in bottom third
    """
    user_count = len(user_scores)
    cohort_size = ceil(user_count / 3)
    sorted_scores = sorted(user_scores)
    top_cohort = set()
    bottom_cohort = set()

    # Add users to bottom and top cohorts
    for score, user in sorted_scores[0:cohort_size]:
        bottom_cohort.add(user)

    for score, user in sorted_scores[user_count - (cohort_size):]:
        top_cohort.add(user)
    
    return (top_cohort, bottom_cohort)

def get_fraction_correct(correct_user_ids, incorrect_user_ids, cohort):
    """ Get fraction of correct answers for 1 question for a given cohort
        Arguments:
        correct_user_ids   [List] id's of users getting correct answer
        incorrect_user_ids [List] id's of users getting incorrect answer
        cohort             [Set] id's of users in a cohort

        Returns:
        cohort_fraction_correct [Float] Fraction of correct answers for cohort
    """
    cohort_users_correct_count = 0
    cohort_users_answer_count = 0

    for id in correct_user_ids:
        if id in cohort:
            cohort_users_answer_count += 1
            cohort_users_correct_count +=1

    for id in incorrect_user_ids:
        if id in cohort:
            cohort_users_answer_count += 1
    
    cohort_fraction_correct = cohort_users_correct_count / cohort_users_answer_count
    return cohort_fraction_correct

def main(answer_file):

    """ Calculate and print item discrimination for each question
        Arguments:
        answer_file [String] json format, each line identifies whether
                             a user's answer to a question is correct
        
        Item discrimination measures the difference between the fraction of
        students who got correct answers in the top and bottom cohorts 
        Item discrimination values range from -1.0 to 1.0:
            Values above 0.3 are generally good questions
            Values between 0.0 and 0.3 are mediocre
            Values under 0.0 usually have errors in their grading

        Returns: no return statement, so returns None
    """
    # Build data for calculations from answer file
    user_scores, answers = read_answers(answer_file)
    # Get user id's of top and bottom third of students, based on scores
    top_cohort, bottom_cohort = get_cohorts(user_scores)

    answers_sorted = sorted(answers.keys())
    
    # Calculate and print item discrimination for each question
    print("Question                       Item Discrimination")
    print("*" * 50)

    for question in answers_sorted:
        correct_user_ids = answers[question]["correct users"]
        incorrect_user_ids = answers[question]["incorrect users"]
        
        top_fraction_correct = get_fraction_correct(correct_user_ids, incorrect_user_ids, top_cohort)
        bottom_fraction_correct = get_fraction_correct(correct_user_ids, incorrect_user_ids, bottom_cohort)
        item_discrimination = top_fraction_correct - bottom_fraction_correct
       
        print("{0:45} {1:>4.1f}".format(question, item_discrimination))
        
main('answers.json')