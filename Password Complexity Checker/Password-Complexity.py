import re

def assess_password_strength(password, length_weight=2, uppercase_weight=1, lowercase_weight=1, number_weight=1, special_char_weight=2):
    
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += length_weight
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        score += uppercase_weight
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        score += lowercase_weight
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if re.search(r'[0-9]', password):
        score += number_weight
    else:
        feedback.append("Password should include at least one number.")
        
    if re.search(r'[\W_]', password):
        score += special_char_weight
    else:
        feedback.append("Password should include at least one special character.")
    
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    elif score >= 6:
        strength = "Very Strong"
    
    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

password = input("Enter the Password :")
length_weight = 3
uppercase_weight = 2
lowercase_weight = 1
number_weight = 2
special_char_weight = 3

result = assess_password_strength(password, length_weight, uppercase_weight, lowercase_weight, number_weight, special_char_weight)
print("Password Strength:", result["strength"])
print("Score:", result["score"])
print("Feedback:", result["feedback"])
