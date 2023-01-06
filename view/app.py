# program preparation // import all needed library n module
from script.openfile import *
import streamlit as st
from script.cyk import cyk


# def for program ui
def view_streamlit():
    # prepare the cnf rules
    cnf = open_file(r'cnf.txt')
    # set web background color
    web_bg = """
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #F8EDE3;
    }
    </style>
    """
    st.markdown(web_bg, unsafe_allow_html=True)

    # set side bar color
    sidebar_bg = """
    <style>
        [class="css-firdtp edgvbvh11"]{
            background-color: #967E76;
        }
    </style>
    """
    st.markdown(sidebar_bg, unsafe_allow_html=True)

    # set button color
    button_style = """
    <style>
        [class="css-firdtp edgvbvh11"]{
            background-color: #85586F;
            border-color: #85586F;   
            width : 70px;
        }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # show web title
    st.write(f"<h1 style='text-align:center;'>CFG Parsing Using CYK Algorithm</h1>", unsafe_allow_html=True)
    st.write(f"<h3 style='text-align:center; color:#874C62; '>Kelompok 4 E</h3>", unsafe_allow_html=True)

    # make side bar for cnf rules
    with st.sidebar:
        st.write(" CNF RULES :")
        st.write(cnf)

    # make container
    with st.container():
        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False
            key = "placeholder"
        # the input sentence text field
        sentences = st.text_input(
            "Masukan Kalimat",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Budi berangkat ke sekolah",
        )

        # convert sentence into list
        check_string = sentences.split(' ')
        # check button
        button = st.button('Go', type='primary')

        # action if button clicked
        if button:
            # show error when no string or just one string entered
            if len(check_string) <= 1:
                st.error("Kalimat harus lebih dari 2 kata")
            # else, process the filing table
            elif sentences != '':
                # call cyk parser function here
                # call cyk table function here
                cyk(sentences)

                # testing table
                # df = np.array([[3, 2, 1], [6, 4, 5]])

                # st.dataframe(df)  # Same as st.write(df)

                st.write("")
