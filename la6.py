# LIBER_ANATHEMA6


import streamlit as st  # imports Streamlit and gives it the short name "st"

st.title("LIBER_ANATHEMA")  # shows the title on the webpage


uploaded_file = st.file_uploader(
    "Choose Python file",  # text shown above the upload button
    type=["py"]  # only allows .py Python files
)


if uploaded_file:  # only runs the code below if the user uploads a file

    # gets the uploaded file and converts it into normal readable text
    code = uploaded_file.getvalue().decode("utf-8")


    try:  # try to check the Python code

        # checks if the uploaded code has valid Python syntax
        compile(code, uploaded_file.name, "exec")

        st.success("✔ No syntax errors")  # shows success message on webpage


    except SyntaxError as error:  # runs if Python finds a syntax error

        st.error("💥 SYNTAX ERROR")  # shows an error box

        st.write("Line:", error.lineno)  # shows the line number
        st.write("Error:", error.msg)  # shows Python's error message


        if error.text:  # if Python knows which line caused the error

            st.code(error.text.rstrip())  # shows the broken line


            if error.offset:  # if Python knows the position of the error

                # puts ^ underneath the position where Python found the problem
                st.code(" " * (error.offset - 1) + "^")


        # turns the whole uploaded code into a list of lines
        lines = code.splitlines()


        # gets the line before the error line
        previous_number = error.lineno - 2


        # keep moving backward until you find a previous line that actualy has code on it
        while previous_number >= 0 and not lines[previous_number].strip():

            previous_number -= 1


        # if there is a previous non-empty line
        if previous_number >= 0:

            st.write("Previous:")

            # shows the previous non-empty line
            st.code(lines[previous_number])


        # checks Python's error message for a missing :
        if "expected ':'" in error.msg:

            st.info("💡 Hint: You have forgotten a :")


        # checks if a bracket or parenthesis was never closed
        elif "was never closed" in error.msg:

            st.info("💡 Hint: Check your brackets or parentheses.")


        # checks for incorrect indentation
        elif "unexpected indent" in error.msg:

            st.info("💡 Hint: Check the spaces at the beginning of the line.")


        # checks for a string missing its closing quotation mark
        elif "unterminated string literal" in error.msg:

            st.info("💡 Hint: Check if it's missing a quotation mark.")


        # fallback hint if LA does not recognize the error yet
        else:

            st.info("💡 Hint: Look carefully at the line Python mentioned.")