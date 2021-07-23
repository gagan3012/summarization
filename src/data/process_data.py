import pandas as pd


def process_data(split='train'):
    df = pd.read_csv('C:/Users/gbhat/Documents/GitHub/summarization/data/raw/{}.csv'.format(split))
    df.rename(columns={"article": "input_text", "highlights": "output_text"})
    print(df.shape)
    df.to_csv('C:/Users/gbhat/Documents/GitHub/summarization/data/processed/{}.csv'.format(split))


if __name__ == '__name__':
    process_data(split='train')
    process_data(split='test')
    process_data(split='validation')
