import pandas as pd


def process_data(split='train'):
    df = pd.DataFrame()
    dataset = pd.load_csv('summarization/data/raw/{}.csv'.format(split))
    df['article'] = dataset['article']
    df['highlights'] = dataset['highlights']
    df.to_csv('summarization/data/processed/{}.csv'.format(split))


if __name__ == '__name__':
    process_data(split='train')
    process_data(split='test')
    process_data(split='validation')
