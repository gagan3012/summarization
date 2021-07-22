import dagshub

from src.models.model import Summarization
from src.data.make_dataset import make_dataset

def evaluate_model():
    """
    Evaluate model using rouge measure
    """
    test_df = make_dataset(split='test')
    model = Summarization()
    model.load_model()
    results = model.evaluate(test_df=test_df)
    with dagshub.dagshub_logger() as logger:
        logger.log_metrics(results)
    return results
