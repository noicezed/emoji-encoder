import streamlit as st

# Function to encode a message into variation selectors
def encode_message_to_vs(message):
    encoded_vs = []
    
    # Convert each character of the message into its corresponding Unicode code point
    for char in message:
        code_point = ord(char)
        
        # For this example, we're using variation selectors starting from 0xFE00
        # We'll map each character's code point to a variation selector range.
        # Simple scheme: 0xFE00 to 0xFE0F, to modify the emoji appearance
        variation_selector = 0xFE00 + (code_point % 16)
        encoded_vs.append(chr(variation_selector))
    
    return "".join(encoded_vs)


# Streamlit App
def main():
    # Title of the app
    st.title("Emoji Encoding with Variation Selectors")

    # Input fields for emoji and text
    emoji_input = st.text_input("Enter an Emoji:", "😀")
    text_input = st.text_area("Enter the Text to Encode:")

    if st.button("Encode"):
        if text_input:
            # Encode the message using variation selectors
            encoded_message = encode_message_to_vs(text_input)
            # Show the encoded emoji with variation selectors
            st.write("Encoded emoji with variation selectors: ")
            Path = f"{emoji_input + encoded_message}"
            st.code(Path, language="python")
        else:
            st.write("Please enter some text to encode.")

if __name__ == "__main__":
    main()