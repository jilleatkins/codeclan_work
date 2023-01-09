def latest(scores):
    latest_score = all_scores.pop
    return latest_score


def personal_best(scores):
    personal_best = scores.max
    return personal_best

def personal_top_three(scores):
    scores.sort(reverse = True)
    personal_top_three = scores[0:3]
    return personal_top_three

def descending_scores(scores):
    scores.sort(reverse = True)
    descending_scores = scores
    return scores

def top_three_scores_where_tied(scores):
    scores.sort(reverse = True)
    test_top_three_scores_where_tied = scores[0:3]
    return test_top_three_scores_where_tied

def top_three_scores_where_fewer_than_three(scores):
    scores.sort(reverse = True)
    test_top_three_scores_where_fewer_than_three = scores[0:2]
    none_score = "None"
    return top_three_scores_where_fewer_than_three + none_score   