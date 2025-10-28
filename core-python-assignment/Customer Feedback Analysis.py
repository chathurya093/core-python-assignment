def positive_feedback_percentage(ratings):
    if not ratings:
        return 0  
    positive_count = sum(1 for r in ratings if r >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return percentage
ratings_input = input("Enter customer ratings (1-5) separated by spaces: ")
ratings = [int(r) for r in ratings_input.split()]
percentage = positive_feedback_percentage(ratings)

print(f"Positive Feedback: {percentage}%")
