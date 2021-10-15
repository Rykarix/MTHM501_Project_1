import streamlit as st
import pandas as pd
import numpy as np


def mark_scheme():
    st.markdown(
        """
    # Mark scheme

    * [20 marks]: Demonstrating mastery of tables, figures and data wrangling
    * [20 marks]: Demonstrating mastery of a topic covered
    * [20 marks]: Demonstrating mastery of a second topic covered
    * [20 marks]: Demonstrating mastery of topics beyond the scope of the course
    * [10 marks]: Presentation, clarity of communication, labelling of graphics
    * [10 marks]: Neat, reproducible code

    * Total: 100 marks

    # Additional notes for the marker:
    Project actively encourages to go beyond of the scope of the course & language requirement not stated. Therefore this shall be written in python & presented as an interactive tool.

    ## Libraries used:
    This will be updated as I progress, purely for marker's benefit

    ### Streamlit
    Open source library for presenting & sharing custom web pages for machine learning & data science

    * API / Docs: https://docs.streamlit.io/
    * About the library: See above

    ### Pandas
    This will be our main data handling tool. It will convert any file format into a fast and efficient DataFrame object.

    * API / Docs: https://pandas.pydata.org/docs/
    * About: https://pandas.pydata.org/about/index.html

    ### Numpy
    Required by pandas anyway but also useful for efficient mathematical computation

    * API / Docs:
    * About:
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
    mark_scheme()
    section_introduction()
    section_objectives()
    section_data()
    section_results()
    section_limitations()
    section_conclusion()
