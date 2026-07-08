from src.entities.feedback import Feedback
from src.usecases.interfaces.feedback_repository import FeedbackRepository

class FeedbackInput:
    comment_value: str
    order_id: str

class FeedbackOutPut:
    id_feedback: str
    message: str

class CreateFeedbackUseCase:
    def __init__(self, feedbackRepo: FeedbackRepository)
        self.feedbackRepo = feedbackRepo

    def execute(self, info: FeedbackInput) -> FeedbackOutPut
        myfeedback = Feedback(info.order_id, info.comment)
        #smt need to done
        savedFb = feedbackRepo.save(myfeedback)
        # smt need to done
        return FeedbackOutput(savedFb.feedback_id, "everything ...")