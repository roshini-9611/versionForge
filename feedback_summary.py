from collections import Counter
import re

def count_total_feedback(feedback_list):
    """
    Returns the total number of feedback entries.
    """
    return len(feedback_list)


def keyword_summary(feedback_list, top_n=5):
    """
    Returns the top N most common words in all feedback entries.
    This helps summarize the general tone of the feedback.
    """
    words = []
    for feedback in feedback_list:
        words.extend(re.findall(r'\b\w+\b', feedback.lower()))

    stopwords = {"the", "is", "was", "and", "it", "to", "a", "an", "of", "for", "in", "on", "with", "this"}
    filtered_words = [word for word in words if word not in stopwords]

    return Counter(filtered_words).most_common(top_n)


# Example usage:
if __name__ == "__main__":
    sample_feedback = [
        "The session was interactive and fun",
        "I liked the way concepts were explained",
        "It was informative and helpful",
        "Great explanation of topics",
        "Very clear and useful session"
    ]
    
    print("Total feedback entries:", count_total_feedback(sample_feedback))
    print("Top keywords:", keyword_summary(sample_feedback))
