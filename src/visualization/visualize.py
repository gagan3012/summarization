import streamlit as st
from models import predict_model


def visualize():
    st.write('# Summarization  UI')
    st.markdown(
        '''
        *For additional questions and inquiries, please contact **Gagan Bhatia** via [LinkedIn](
        https://www.linkedin.com/in/gbhatia30/) or [Github](https://github.com/gagan3012).*
        ''')

    text = st.text_area("Enter text here")
    if st.button("Generate Summary"):
        with st.spinner("Connecting the Dots..."):
            text = predict_model(text=text)
        st.write("# Generated Summary:")
        st.write("{}".format(text))


if __name__ == "__main__":
    visualize()
