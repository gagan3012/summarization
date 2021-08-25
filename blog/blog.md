# Machine Summarization – An Open Data Science Project 
## TL;DR
We built a machine learning model that summarizes text. It only makes sense that we’ll let it summarize what this article is about.
## Model generated summary of the Article:
Deep Learning technology can be used for learning tasks related to language, such as translation, classification, entity recognition or in this case, summarization . We wanted to build a project that could be easily reproduced and customized, to make it usable for the community . The package for text summarization is available to be downloaded as a package . Using DAGHub allows us to track and manage metrics for all the different runs..In a sense, this is a template for more summarization projects. The code for training the model has been written in pytorch lightning. The script allows us to train T5, mT5 and byT5 models as well.
---

To add to this auto-summary – Two additional interesting aspects of the project are:
It is easily customizable – changing datasets and model architectures is made to be easy, which means that you can easily adapt it to your needs.
It integrates many of the best open source tools all in one – DVC, MLflow, HuggingFace, and Streamlit. This is an example of an end to end open source stack and workflow, which means it can be applicable to many other ML projects.
# Task Introduction – Machine Summarization
Natural Language Processing is one of the key areas where Machine Learning has been very effective. In fact, whereas NLP traditionally required a lot of human intervention, today, this is no longer true. Specifically, Deep Learning technology can be used for learning tasks related to language, such as translation, classification, entity recognition or in this case, summarization.

Borrowing the definition of the task from this excellent article by Luís Gonçalves: 
> Summarization is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. Since manual text summarization is a time expensive and generally laborious task, the automatization of the task is gaining increasing popularity and therefore constitutes a strong motivation for academic research.

> There are important applications for text summarization in various NLP related tasks such as text classification, question answering, legal texts summarization, news summarization, and headline generation. Moreover, the generation of summaries can be integrated into these systems as an intermediate stage which helps to reduce the length of the document.


## The Challenge – Making it easy to modify datasets and models
Typically when we are building or fine tuning a model for summarisation we need to load the model, download the data, write a fine tuning script and then we need to define our pipeline. The whole process is very intensive and often results are not reproducible by others using the pipeline. In a traditional git repository it is hard to keep track of large datasets and models which makes it even harder to track models. 

There was not a ready to use pipeline that could be easily modified with different datasets to train the same model (or the ability to customize the model, for that matter). Each time we had to change a dataset or use a different split of the dataset we would have to re-run all the steps of the pipeline which would further take up resources on the system. 

Usually, if you wanted to build a custom summarization model, you had to do all of the work we describe above from scratch, but we wanted to build a project that could be easily reproduced and customized, to make it usable for the community. In a sense, this is a template for more summarization projects


We even created a package for text summarization which is available to for being downloaded using `pip`: 

```
pip install t5s

```

Once we download the package we can use the training pipeline. But before we get into how the package works, let’s start by explaining what each stage of the pipeline does.


## The Pipeline – Providing structure to our project
The first stage of our pipeline is to download data from the Hugging Face hub. Here for training we have used the `CNN_dailymail` dataset. In order to download the dataset we use the parameter files called `data_params.yml` which defines the datasets and the split that we would like to train our data on. We run the `download_data` stage which downloads the data and then stores it as raw data which we will then process. 

Once the raw data is saved we move on to processing the data using our script to process the raw data. We change the column names and modify the data to work with our training script. Now the data is also split into three different files: `train.csv`, `validation.csv` and `test.csv` which represent training, validation and test sets, respectively. 

Now we can move on to training the model. The code for training the model has been written in pytorch lightning. The script allows us to train `T5`, `mT5` and `byT5` models as well. All the script parameters can be controlled using the `model_params.yml` file. The training stage returns the model that can be saved and also the training metrics which are logged using MLflow and DAGsHub. 

Next we need to evaluate the model that has been created and to do so we need to use the rouge metric which uses the test datasets to evaluate the model. ROUGE, or Recall-Oriented Understudy for Gisting Evaluation, is a set of metrics and a software package used for evaluating automatic summarization and machine translation software in natural language processing. The metrics compare an automatically produced summary or translation against a reference or a set of references (human-produced) summary or translation. The evaluation metrics are also saved using DAGsHub. Once we commit all the models to git we can evaluate our models from the DAGsHub repo. 




We can also visualise and test the results of the model using a streamlit app which can be accessed using Hugging Face spaces. We also have the option of running the upload script and uploading the model to Hugging Face Hub too.

## The hard part – making things reproducible and customizable
One of the biggest challenges that we faced in this project was to build a data pipeline that was reproducible and was easy to evaluate. Using DAGsHub has made this possible. DAGsHub allows us to track and manage metrics for all the different runs and allows us to have a reproducible pipeline. Logging metrics to DAGsHub is as easy as committing files to a git repo one push and we are ready to analyse the run. 

In order to use the DAGsHub logger with pytorch lightning we had to make a few changes in the logging system in our code. Since pytorch lightning is a live project and it’s always improving we need to find better ways to have real time logging. We tried using multiple logging services that can be used in the pipeline on demand too. We have implemented Weights and Biases, tensorboard and MLFlow logging. We found that MLFlow is the best logging method here because of its seamless integration with DAGsHub. 
## The `t5s` package – wrapping it up nicely
In order to run the pipeline we have setup a CLI application that will help us run the pipeline 

To install the pipeline we need to first install t5s using:

```
pip install t5s
```

Now, we need to clone the repo containing the code.
```
t5s clone 
```

We would then have to create the required directories to run the pipeline

```
t5s dirs
``` 

To define the parameters for a run we’ll use the following command:
```
t5s start  [-d DATASET] [-s SPLIT] [-n NAME] [-mt MODEL_TYPE]
                 [-m MODEL_NAME] [-e EPOCHS] [-lr LEARNING_RATE]
                 [-b BATCH_SIZE]
```
This will set all the necessary parameters, in order to automate the rest of the process, including data and model retrieval, and setting of hyperparameters for the training step.

Then we need to pull the model we chose from our DVC repo:

```
t5s pull
```

Now to run the training pipeline we can run:

```
t5s run
```

Before pushing make sure that the DVC remote is setup correctly:

```
dvc remote modify origin url https://dagshub.com/{user_name}/summarization.dvc
dvc remote modify origin --local auth basic
dvc remote modify origin --local user {user_name}
dvc remote modify origin --local password {your_token}
```
Finally to push the model to DVC

```
t5s push
```

To push this model to Hugging Face Hub for inference you can run:

```
t5s upload
```

Finally, if we would like to test the model and visualise the results we can run:

```
t5s visualize
```
This will open our Streamlit app, which in turn will let us try out our model with some custom examples. 
## Summary
In conclusion, we have built a machine summarisation pipeline that is reproducible and reusable. This project is unique because it combines a lot of open source tools like DAGsHub, DVC, PyTorch Lightning, HuggingFace Hub and Streamlit to build the model. We would love for you to try out our Machine Summarisation project yourself, and to give us feedback. It would really help us to prioritize future features, so please vote on or create issues! If you'd like to take a more active part, we have some good first issues ideas that you can start with. We'll be happy to provide guidance on the best way to do so. 
