import streamlit as st
import pandas as pd
import numpy as np

"""
Notes for the marker:


"""


def mark_scheme():
    st.header("Mark Scheme")
    st.markdown(
        """
    • [20 marks]: Demonstrating mastery of tables, figures and data wrangling
    • [20 marks]: Demonstrating mastery of a topic covered
    • [20 marks]: Demonstrating mastery of a second topic covered
    • [20 marks]: Demonstrating mastery of topics beyond the scope of the course
    • [10 marks]: Presentation, clarity of communication, labelling of graphics
    • [10 marks]: Neat, reproducible code
    Total: 100 marks
    """
    )

    st.header("Additional notes for the marker")
    st.markdown(
        """
    Project actively encourages to go beyond of the scope of the course & language requirement not stated. Therefore this shall be written in python & presented as an interactive tool.

    The Libraries I will be using are as follows:
    Streamlit
    * Open source library for presenting & sharing custom web pages for machine learning & data science
    API / Docs: https://docs.streamlit.io/
    About the library: See above

    Pandas - No, not the super cute white and black fuzzy bear that refuses to eat anything but bamboo
    * This will be our main data handling tool. It will convert any file format into a fast and efficient DataFrame object.
    API / Docs: https://pandas.pydata.org/docs/
    About: https://pandas.pydata.org/about/index.html

    Numpy
    Required by pandas anyway but also useful for efficient mathematical computation
    Total: 100 marks
    """
    )


# I've defined each section so that I can colapse the code whilst writing
# It will also make marking easier
def section_introduction():
    st.header("Introduction")
    st.markdown(
        """
    Content
    """
    )


def section_objectives():
    st.header("Objectives")
    st.markdown(
        """
    Content
    """
    )


def section_data():
    st.header("Data")
    st.markdown(
        """
    Content
    """
    )


def section_results():
    st.header("Results")
    st.markdown(
        """
    Content
    """
    )


def section_limitations():
    st.header("Limitations")
    st.markdown(
        """
    Content
    """
    )


def section_conclusion():
    st.header("Conclusion")
    st.markdown(
        """
    Content
    """
    )


# Typical pythonic best practice.
if __name__ == "__main__":
    section_introduction()
    section_objectives()
    section_data()
    section_results()
    section_limitations()
    section_conclusion()
