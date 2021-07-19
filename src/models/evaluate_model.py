from src.models.model import Summarization
from src.data.make_dataset import make_dataset

def evaluate_model():
    """
    Evalute model using rouge measure
    """
    test_df = make_dataset(split='test')
    model = Summarization()
    model.load_model()
    results = model.evaluate(test_df=test_df)
    return results
