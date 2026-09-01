"""8.You receive the following dataset containing user email addresses:
emails = ["ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com"]
The dataset contains duplicate records. Develop a data-cleaning solution that produces a collection of unique email
addresses while preserving the original data when necessary. Requirement: Consider the trade-off between
uniqueness, ordering, and performance."""

emails = ["ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", "ahmed@gmail.com", "sara@yahoo.com", "zain@hotmail.com"]

original_data = tuple(emails)
print("Original Data: ",original_data)

unique_emails = []
for email in original_data:
    if email not in unique_emails:
        unique_emails.append(email)

print("Unique emails: ", unique_emails)