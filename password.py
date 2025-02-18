import re

def assess_password_strength(password):
    # Criteria checks
    length = len(password) >= 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_number = re.search(r'[0-9]', password)
    has_special_char = re.search(r'[@$!%*?&]', password)

    # Feedback message
    feedback = []

    if not length:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password should include at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password should include at least one lowercase letter.")
    if not has_number:
        feedback.append("Password should include at least one number.")
    if not has_special_char:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, &).")

    # Strength assessment
    if length and has_uppercase and has_lowercase and has_number and has_special_char:
        strength = "Strong"
    elif length and (has_uppercase or has_lowercase) and has_number:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Return the results
    return {
        "password_strength": strength,
        "feedback": feedback
    }

# Example usage
password = input("Enter a password to assess: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['password_strength']}")
if result['feedback']:
    for line in result['feedback']:
        print(line)
else:
    print("Your password is strong!")
