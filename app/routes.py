import logging
from fastapi import APIRouter, HTTPException
from app.models import *
from app.services import generate_atomic_topics, start_session, submit_explanation

# Configure logging (ideally done once at application startup, but placing here for simplicity)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate-topics", response_model=GenerateAtomicResponse)
def generate_topics(request: GenerateAtomicRequest):
    # Input validation
    if not request.given_topic or not request.given_topic.strip():
        logger.warning("Validation failed: Given topic is empty.")
        raise HTTPException(status_code=400, detail="Given topic cannot be empty.")
    
    try:
        topic_preview = request.given_topic[:50] if request.given_topic else 'Unknown'
        logger.info(f"Generating topics for: {topic_preview}...") # Log start, truncate topic
        response = generate_atomic_topics(request)
        logger.info(f"Successfully generated topics for: {topic_preview}.")
        return response
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error generating topics for '{topic_preview}': {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred while generating topics.")

@router.post("/start-session", response_model=StartSessionResponse)
def start_learning_session(request: StartSessionRequest):
    # Input validation
    if not request.atomic_topic or not request.atomic_topic.strip():
        logger.warning("Validation failed: Atomic topic is empty.")
        raise HTTPException(status_code=400, detail="Atomic topic cannot be empty.")
    if not request.initial_explanation or not request.initial_explanation.strip():
        logger.warning("Validation failed: Initial explanation is empty.")
        raise HTTPException(status_code=400, detail="Initial explanation cannot be empty.")
    
    try:
        topic_preview = request.atomic_topic[:50] if request.atomic_topic else 'Unknown'
        logger.info(f"Starting session for topic: {topic_preview}...")
        response = start_session(request)
        logger.info(f"Successfully started session for topic: {topic_preview}.")
        return response
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error starting session for topic '{topic_preview}': {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred while starting the session.")

@router.post("/submit-explanation", response_model=SubmitExplanationResponse)
def submit_user_explanation(request: SubmitExplanationRequest):
    # Input validation
    if not request.explanation or not request.explanation.strip():
        logger.warning("Validation failed: Explanation is empty.")
        raise HTTPException(status_code=400, detail="Explanation cannot be empty.")
    if not request.goal or not request.goal.strip():
        logger.warning("Validation failed: Goal is empty.")
        raise HTTPException(status_code=400, detail="Goal cannot be empty.")
    
    try:
        goal_preview = request.goal[:50] if request.goal else 'Unknown'
        logger.info(f"Submitting explanation for goal: {goal_preview}...")
        response = submit_explanation(request)
        logger.info(f"Successfully processed explanation for goal: {goal_preview}. Goal met: {response.is_goal_met}")
        return response
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error processing explanation for goal '{goal_preview}': {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An internal server error occurred while processing the explanation.")