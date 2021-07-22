from datasets import load_dataset
import pandas as pd


def make_dataset(dataset='cnn_dailymail', split='train'):
    """make dataset for summarisation"""
    dataset = load_dataset(dataset, '3.0.0', split=split)
    df = pd.DataFrame()
    df['input_text'] = dataset['article']
    df['output_text'] = dataset['highlights']
    df.to_csv('C:/Users/gbhat/Documents/GitHub/summarization/data/processed/{}.csv'.format(split, split))


if __name__ == '__main__':
    make_dataset(dataset='cnn_dailymail', split='train')
    make_dataset(dataset='cnn_dailymail', split='test')
    make_dataset(dataset='cnn_dailymail', split='validation')
