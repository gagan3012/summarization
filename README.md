<h1 align="center">t5s</h1>

T5 Summarisation Using Pytorch Lightning, DVC, DagsHub and HuggingFace Spaces

[![pypi Version](https://img.shields.io/pypi/v/t5s.svg?logo=pypi&logoColor=white)](https://pypi.org/project/t5s/)
[![Downloads](https://static.pepy.tech/personalized-badge/t5s?period=total&units=none&left_color=grey&right_color=orange&left_text=Pip%20Downloads)](https://pepy.tech/project/t5s)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/gagan3012/summarization)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gagan3012/summarization/blob/master/notebooks/t5s.ipynb)
[![DAGSHub](https://img.shields.io/badge/%F0%9F%90%B6-Pipeline%20on%20DAGsHub-green)](https://dagshub.com/gagan3012/summarization)

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

```

t5s push_to_hf_hub

```

Next if we would like to test the model and visualise the results we can run:
```

t5s visualize

```
And this would create a streamlit app for testing

---
title: T5S
emoji: 💯
colorFrom: yellow
colorTo: red
sdk: streamlit
app_file: src/visualization/visualize.py
pinned: false
---