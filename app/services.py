import instructor
import os
import google.generativeai as genai
from .config import GOOGLE_API_KEY
from .models import *


genai.configure(api_key=GOOGLE_API_KEY)
client = instructor.from_gemini(
    client=genai.GenerativeModel(
        model_name="models/learnlm-1.5-pro-experimental", # Updated model name
        system_instruction="You are ELIS, a study buddy who helps people learn using the Feynman technique." # Corrected grammar
    )
)

def generate_atomic_topics(request: GenerateAtomicRequest) -> GenerateAtomicResponse:
    """
    Generates atomic topics based on a given topic using the Gemini model.

    Args:
        request: The request object containing the initial topic.

    Returns:
        A response object containing whether the topic was generic and a list of atomic topics.
    """
    resp = client.messages.create(
        messages=[
            {
                "role": "user",
                "content": f"""
    Topic: {request.given_topic}
    Analyze the given topic and determine its specificity for focused learning.

    - If the topic is too generic, suggest a set of **specific atomic topics** that break it down into focused, explainable concepts.
    - If the topic is already specific, refine it further and suggest **closely related atomic topics** for a deeper understanding.

    **Atomic topics must be focused, specific, and independently explainable. Avoid redundancy.**
    """,
            }
        ],
        response_model=AtomicTopics,
    )
    is_generic = resp.is_generic
    atomic_topics = resp.topics
    return GenerateAtomicResponse(is_generic=is_generic, atomic_topics=atomic_topics)


def start_session(request: StartSessionRequest) -> StartSessionResponse:
    """
    Starts a learning session based on an atomic topic and initial explanation.

    Args:
        request: The request object containing the atomic topic and initial explanation.

    Returns:
        A response object containing the learning goal and initial feedback.
    """
    resp = client.messages.create(
        messages=[
            {
                "role": "user",
                "content": f"""
Topic: {request.atomic_topic}
Initial Explain Like Im 5 Explanation: {request.initial_explanation}

You are ELIS, you are starting a structured learning session on the given atomic topic.

- Define a **clear and specific learning goal** based on the given initial explanation.
- The goal should be **focused, measurable, and directly related** to the atomic topic.
- The goal should contain explanation criteria which the user should achieve.
- Provide **engaging and constructive feedback** to help the learner refine their understanding.
- The feedback should be thought-provoking, such as a **guiding question, a missing key point, or a deeper exploration suggestion**.
""",
            }
        ],
        response_model=StartLearning,
    )

    goal = resp.goal
    feedback = resp.feedback
    return StartSessionResponse(goal=goal, feedback=feedback)


def submit_explanation(request: SubmitExplanationRequest) -> SubmitExplanationResponse:
    """
    Submits a user's explanation for evaluation against the learning goal.

    Args:
        request: The request object containing the explanation and the goal.

    Returns:
        A response object containing feedback and whether the goal is met.
    """
    resp = client.messages.create(
        messages=[
            {
                "role": "user",
                "content": f"""
User Explain Like Im Five Explanation: {request.explanation}  
Learning Goal: {request.goal}  


You are ELIS, your task is evaluate the user's explanation in relation to the specified learning goal.  

- If the explanation completely meets the goal, set `is_goal_met` to **True** and provide **positive reinforcement**.  
- If the explanation does **not fully meet** the goal, set `is_goal_met` to **False** and offer **constructive feedback** that is **engaging and thought-provoking**.  
- Feedback should be in the form of **a guiding question, a missing key point, or a suggestion for deeper exploration**.  
- Ensure the feedback encourages **active reflection and structured learning**.  
""",
            }
        ],
        response_model=ExplanationFeedback,
    )
    return SubmitExplanationResponse(feedback=resp.feedback, is_goal_met=resp.is_goal_met)
