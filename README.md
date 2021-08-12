---
title: T5S
emoji: 💯
colorFrom: yellow
colorTo: red
sdk: streamlit
app_file: src/visualization/visualize.py
pinned: false
---

<h1 align="center">t5s</h1>

T5 Summarisation Using Pytorch Lightning

[![pypi Version](https://img.shields.io/pypi/v/t5s.svg?logo=pypi&logoColor=white)](https://pypi.org/project/t5s/)
[![Downloads](https://static.pepy.tech/personalized-badge/t5s?period=total&units=none&left_color=grey&right_color=orange&left_text=Pip%20Downloads)](https://pepy.tech/project/t5s)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/gagan3012/summarization)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gagan3012/summarization/blob/master/notebooks/t5s.ipynb)

## Usage

To use and run the DVC pipeline install the `t5s` package

```

pip install t5s

```

Firstly we need to clone the repo containing the code so we can do that using:

```

t5s clone 

```

We would then have to create the required directories to run the pipeline

```

t5s dirs

``` 

Then we need to pull the models from DVC

```

t5s pull

```

Now to run the training pipeline we can run:

```

t5s run

```

Finally to push the model to DVC

```

t5s push

```

To push this model to HuggingFace Hub for inference you can run:

```shell script

t5s push_to_hf_hub

```

Next if we would like to test the model and visualise the results we can run:
```

t5s visualize

```
And this would create a streamlit app for testing

 
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make dirs` or `make clean`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── metrics.txt    <- Relevant metrics after evaluating the model.
    │   └── training_metrics.txt    <- Relevant metrics from training the model.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │   └── process_data.py
    │   │
    │   ├── models         <- Scripts to train models 
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │   └── evaluate_model.py
    │   │   └── model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
    └── data.dvc          <- Traing a model on the processed data.


--------
