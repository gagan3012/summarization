import streamlit as st
import yaml

from src.models.model import Summarization


def predict_model(text: str):
    """
    Predict the summary of the given text.
    """
    with open("model_params.yml") as f:
        params = yaml.safe_load(f)

    model = Summarization()
    model.load_model(model_type=params["model_type"], model_dir="gagan3012/summarsiation")
    pre_summary = model.predict(text)
    return pre_summary


def visualize():
    st.write("# Summarization  UI")
    st.markdown(
        """
        *For additional questions and inquiries, please contact **Gagan Bhatia** via [LinkedIn](
        https://www.linkedin.com/in/gbhatia30/) or [Github](https://github.com/gagan3012).*
        """
    )

    text = st.text_area("Enter text here")
    if st.button("Generate Summary"):
        with st.spinner("Connecting the Dots..."):
            sumtext = predict_model(text=text)
        st.write("# Generated Summary:")
        st.write("{}".format(sumtext))


if __name__ == "__main__":
    visualize()
