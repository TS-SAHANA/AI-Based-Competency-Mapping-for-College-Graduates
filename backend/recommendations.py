def recommend_learning(gap_skills):
    courses = {
        "sql": [
            "SQL for Data Science (Coursera)",
            "The Complete SQL Bootcamp (Udemy)",
            "Intro to SQL (Khan Academy)"
        ],
        "python": [
            "Python Basics (Codecademy)",
            "Complete Python Bootcamp (Udemy)",
            "Python for Everybody (Coursera)"
        ],
        "statistics": [
            "Intro to Stats (Khan Academy)",
            "Statistics with R (Coursera)",
            "Basic Statistics (edX)"
        ],
        "excel": [
            "Excel Essentials (LinkedIn Learning)",
            "Excel Skills for Business (Coursera)",
            "Microsoft Excel - Excel from Beginner to Advanced (Udemy)"
        ],
        "powerbi": [
            "Power BI Projects (Udemy)",
            "Getting Started with Power BI (LinkedIn Learning)",
            "Microsoft Power BI - A Complete Introduction (Udemy)"
        ],
        "java": [
            "Java Programming Masterclass (Udemy)",
            "Java Fundamentals (Pluralsight)",
            "Object Oriented Programming in Java (Coursera)"
        ],
        "dbms": [
            "Database Management System - NPTEL",
            "Intro to Databases (Stanford Online)",
            "Database Systems Concepts (edX)"
        ],
        "ds_algo": [
            "DSA Crash Course - GeeksforGeeks",
            "Algorithms Specialization (Coursera)",
            "Data Structures and Algorithms (Udemy)"
        ],
        "oop": [
            "OOP Principles in Python - Coursera",
            "Java Object Oriented Programming (Udemy)",
            "Object Oriented Programming with C++ (edX)"
        ],
        "figma": [
            "Figma UI/UX Course (YouTube)",
            "Learn Figma: User Interface Design Essentials (Udemy)",
            "Introduction to Figma (Coursera)"
        ],
        "design_thinking": [
            "Design Thinking for Beginners",
            "Design Thinking and Innovation (Coursera)",
            "Human-Centered Design (IDEO U)"
        ],
        "html_css": [
            "HTML/CSS Bootcamp - freeCodeCamp",
            "Build Responsive Real World Websites with HTML5 and CSS3 (Udemy)",
            "CSS Basics (MDN Web Docs)"
        ],
    }

    recommendations = []
    for skill in gap_skills:
        recs = courses.get(skill, ["Search online for latest resources"])
        recommendations.append({
            "skill": skill,
            "resources": recs
        })

    return recommendations
