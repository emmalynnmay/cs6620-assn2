# CS 6620 LLM Tutor

Emma Lynn May

## Usage

Set up the virtual environment

`python3 -m venv my_env`

Activate the virtual environment

`source my_env/bin/activate`

Install dependencies

`pip3 install -r requirements.txt`

Deactivate the virtual environment (when you're done running the program)

`deactivate`

### Add your Open AI API key

Copy the file .env.example and rename it to .env. Replace `YourAPIKeyHere` with your OpenAI API key.

## Running the tutor

Run the tutor

`python3 tennis.py`

## Prompt Engineering Process

### Expert Model
One of my questions is `Your customer wants can't decide between vanilla, chocolate, and strawberry ice cream. What do you serve them?`. The correct answer to this question is to offer neapolitan ice cream. Initially the tutor responded like this:

```
When a customer can't decide, it's helpful to offer them a taste of each flavor. This way, they can make a more informed decision based on their preference. You can simply offer, "Would you like to try a sample of each to help you decide?"
```

While this is a reasonable response, it wasn't the answer I wanted the tutor to come up with. I added a description of the products
available at the ice cream shop to the tutor's initial instructions: `The available products at the ice cream shop are waffle and sugar cones, ice cream sandwiches, and scoops of various ice cream flavors, including neapolitan.` This caused the tutor to come up with a better response:

```
Since they're deciding between vanilla, chocolate, and strawberry, you could suggest a scoop of Neapolitan ice cream, as it contains all three flavors. This way, they can enjoy a taste of each flavor.
```

Since this tutor is meant to be tailored to this specific, fictional ice cream shop, it makes sense that the tutor wouldn't know everything right off the bat, since not everything is a general subject-matter fact. Giving the tutor some more context helps improve its expert model.

### Pedagogical Model
This tutor can provide immediate, customized feedback which is helpful for the learner. This is a very important contributor to learning, as we've discussed in class. The tutor could be modified to support interleaved practice, a moderately effective learning technique, by returning to missed questions after looking at other questions for a minute, instead of focusing on just one question until it's correct (especially since the tutor basically gives you the answer after you get it wrong the first time). The Pedagogical Model could also be modified to more closely resemble a traditional intelligent tutoring system by adding the ability to ask for hints and implementing some scaffolding.
