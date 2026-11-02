system_data = {
    "status": "success",
    "total_users": 3,
    "users": [
        {"id": 1, "name": "Ali", "scores": [85, 90, 88]},
        {"id": 2, "name": "Sara", "scores": [70, 75, 80]},
        {"id": 3, "name": "Usman", "scores": [95, 92, 98]}
    ]
}

# print(system_data["users"][1]["scores"][1])


company_data = {
    "departments": [
        {
            "name": "AI Lab",
            "projects": [
                {"title": "NLP", "budget": 5000},
                {"title": "Vision", "budget": 8000}
            ]
        },
        {
            "name": "Web Dev",
            "projects": [
                {"title": "Portal", "budget": 3000}
            ]
        }
    ]
}

company_data["departments"][1]["projects"][0]["budget"] = 4500

print(company_data["departments"][1]["projects"][0]["budget"] )