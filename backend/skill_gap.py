def analyze_skill_gap(student_skills, required_skills):
    gaps = []
    for skill in required_skills:
        # Normalize skill key and level to lowercase for consistent comparison
        level = student_skills.get(skill, "none").lower()
        if level in ["none", "beginner"]:
            gaps.append(skill)
    return gaps


def calculate_readiness_score(student_skills, required_skills):
    # Define a mapping from skill level to score points
    level_points = {
        "none": 0,
        "beginner": 0,
        "intermediate": 1,
        "advanced": 2
    }

    score = 0
    for skill in required_skills:
        level = student_skills.get(skill, "none").lower()  # Normalize case
        score += level_points.get(level, 0)  # Default to 0 if unknown level

    total = len(required_skills) * 2  # Max score possible
    readiness_percentage = (score / total) * 100 if total > 0 else 0

    return round(readiness_percentage)

