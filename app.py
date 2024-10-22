import streamlit as st
from datetime import datetime
import os

def format_list(word_list):
    formatted_list = "list_format_a = [\n"
    for i in range(0, len(word_list), 10):
        line_words = word_list[i:i + 10]
        formatted_list += '    ' + ', '.join(f'"{word}"' for word in line_words) + ',\n'
    if word_list:  # Remove the last comma if the list is not empty
        formatted_list = formatted_list[:-2] + "\n"  # Remove last comma and newline
    formatted_list += "]"
    return formatted_list

def main():
    st.title("Word List Entry")
    
    # Input area for words
    words_input = st.text_area("Enter words (or multiple words, separated by newlines):", height=200)

    # List to hold unique words
    if 'word_list' not in st.session_state:
        st.session_state.word_list = []

    # Button to add words
    if st.button("Add Words"):
        words = words_input.strip().splitlines()
        for word in words:
            word = word.strip()
            if word and word not in st.session_state.word_list:
                st.session_state.word_list.append(word)
        st.success(f"Added {len(words)} words.")

    # Button to export the list
    if st.button("Export List"):
        if not st.session_state.word_list:
            st.info("No words entered.")
            return

        # Sort the word list in alphabetical order
        sorted_word_list = sorted(st.session_state.word_list)

        # Format the list
        formatted_list = format_list(sorted_word_list)

        # Show the formatted list to the user
        st.text_area("Your List in Format B", formatted_list, height=300)

        # Prepare to save the file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"word_list_{timestamp}.txt"
        file_path = f"./{filename}"  # Save in the current working directory

        # Save the list to a file
        try:
            with open(file_path, "w") as file:
                file.write(formatted_list)
            st.success(f"List exported to {file_path}")
        except Exception as e:
            st.error(f"Export Failed: {str(e)}")

if __name__ == "__main__":
    main()
