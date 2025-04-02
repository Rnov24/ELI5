from pydantic import BaseModel, Field
from typing import List

# Instructor Response
class AtomicTopics(BaseModel):
    """Represents a list of atomic topics generated from a broader subject."""
    is_generic: bool = Field(
        ...,
        description="Indicates whether the initial general topic provided was considered too broad or vague for effective breakdown into specific atomic subtopics."
    )
    topics: List[str] = Field(
        ...,
        description="A list of specific, granular concepts derived from the initial topic. This list will always contain multiple atomic subtopics suitable for focused learning. If the initial topic was considered specific (`is_generic` is false), this list will include a refined version of that topic along with other related subtopics. If the initial topic was broad (`is_generic` is true), this list will contain several atomic subtopics breaking down the broader subject.",
        examples=[
            "How does education contribute to personal development?",
            "What is the role of education in societal progress?",
            "Explain the economic benefits of education for individuals.",
            "Compare formal vs. informal education systems.",
        ],
    )

class StartLearning(BaseModel):
    """Represents the initial learning goal established for a session."""
    goal: str = Field(
        ...,
        description="A concise and specific learning goal derived from the user's initial explanation of an atomic topic. This goal sets the target for the learning session.",
        examples=["Explain the process of photosynthesis in simple terms, including the inputs and outputs."]
    )
    feedback: str = Field(
        ...,
        description="Initial feedback on the user's explanation, potentially including skeptical questions or hints to guide them towards the learning goal.",
        examples= "You mentioned sunlight is an input, but what are the other necessary inputs for photosynthesis? And what are the outputs?"
    )

class ExplanationFeedback(BaseModel):
    """Provides feedback on a user's explanation and indicates if the learning goal is met."""
    is_goal_met: bool = Field(
        ...,
        description="Indicates whether the user's explanation successfully meets the established learning goal.",
    )
    feedback: str = Field(
        ...,
        description="Constructive feedback on the user's explanation, often containing skeptical questions or hints to guide further refinement if the goal is not met.",
        examples= "Your explanation is clearer now, but can you elaborate on how chlorophyll captures light energy?"
    )

# Endpoints request and response model
class GenerateAtomicRequest(BaseModel):
    """Request model for generating atomic topics."""
    given_topic: str 

class GenerateAtomicResponse(BaseModel):
    """Response model containing the generated atomic topics."""
    is_generic : bool 
    atomic_topics: list[str] 
    
class StartSessionRequest(BaseModel):
    """Request model for starting a new learning session."""
    atomic_topic: str 
    initial_explanation: str 

class StartSessionResponse(BaseModel):
    """Response model after starting a learning session, providing the initial goal and feedback."""
    goal: str 
    feedback: str 

class SubmitExplanationRequest(BaseModel):
    """Request model for submitting an explanation during a learning session."""
    explanation: str 
    goal: str 

class SubmitExplanationResponse(BaseModel):
    """Response model after submitting an explanation, providing feedback and goal status."""
    feedback: str 
    is_goal_met: bool 