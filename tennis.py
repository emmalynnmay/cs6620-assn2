# conda env config vars set -n base OPENAI_API_KEY=$OPENAI_API_KEY
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

questions = [
    "Your opponent hits a ball short to your forehand. How do you respond?\n",
    "Your opponent hits the ball deep to your backhand with a lot of topspin. How do you respond?\n"
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
                "content": ("Pretend you are a coach who is teaching tennis strategy to a student."
                "You will ask the student about a scenerio that may arise during a tennis match."
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
