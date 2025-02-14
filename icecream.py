from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

class AnswerEvaluation(BaseModel):
    is_correct: bool
    comments: str

questions = [
    "Your customer is asking what cone options the shop has. What do you say?\n",
    "Your customer wants can't decide between vanilla, chocolate, and strawberry ice cream. What do you serve them?\n",
    "Your customer wants to order vanilla ice cream with soft chocolate cookies that they can hold in their hand. They do not want a cone. What do you serve them?\n",
    "Your customer asks to sample every single type of ice cream available. What do you say?\n",
    "A customer has eaten too much ice cream and has morphed into a ice cream monster who is using freeze powers on other customers. What do you do?\n",
]

def format_correctness(is_correct):
    if is_correct:
        return "✅ You're correct! ✅"
    return "❌ Not quite right... try again! ❌"

def askQuestion(question):
    student_response = input(question)
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": ("Pretend you are a manager working at an ice cream shop. You are training "
                "a new employee. You will ask the employee questions about situations they might encounter working in the ice cream shop. "
                "When they respond, let them know if there answer is acceptable. If their answer is not "
                "acceptable, give them some feedback on how they may improve."
                "The available products at the ice cream shop are waffle and sugar cones, ice cream sandwiches, and scoops of various ice cream flavors, including neapolitan.")
            },
            {
                "role": "assistant",
                "content": question
            },
            {
                "role": "user",
                "content": student_response
            }
        ],
        response_format=AnswerEvaluation,
    )

    print(format_correctness(completion.choices[0].message.parsed.is_correct))
    print(f"   {completion.choices[0].message.parsed.comments}")

    return completion.choices[0].message.parsed.is_correct

print("Welcome to the 🍦 Ice Cream Shop 🍦 Tutor!\n")
for question in questions:
    result = askQuestion(question)
    while not result:
        result = askQuestion(question)
    print("=============================\n")
