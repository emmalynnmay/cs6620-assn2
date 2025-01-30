# conda env config vars set -n base OPENAI_API_KEY=$OPENAI_API_KEY
from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

questions = [
    "You need to store User IDs, avoiding duplicates. What data structure should you use for greatest time efficiency?"
    "Why does it take up to O(n) time to insert a new value into a sorted linked list while keeping it sorted?"
]

# question = questions[0]

def askQuestion(question):
    student_response = input(question)
    # relevant API documenation: https://platform.openai.com/docs/guides/text-generation
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": ("Pretend you are an instructor for a data structures course."
                "You will ask the student a question about a data structures topic."
                "When they respond, let them know if there answer is acceptable. If their answer is not"
                "Acceptable, give them some feedback on how they may improve.")
            },
            {
                "role": "assistant",
                "content": question
            },
            {
                "role": "user",
                "content": student_response
            }
        ]
    )

    print(completion.choices[0].message.content)
    print("=============================")

for question in questions:
    askQuestion(question)
