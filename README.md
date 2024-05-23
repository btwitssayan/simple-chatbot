# Chatbot with Streamlit

This is a simple chatbot built using Python and Streamlit. The chatbot can respond to greetings, tell the current time, tell jokes, perform web searches, and play YouTube videos based on user input.

## Features

- Responds to greetings such as "hello", "hi", "hey", "howdy", "hola".
- Tells the current time.
- Tells jokes using the `pyjokes` library.
- Performs web searches using the `pywhatkit` library.
- Plays YouTube videos based on user input.

## Instructions

1. **Search a query:** Start your input with the keyword `search`. For example, `search Python tutorials`.
2. **Hear a joke:** Type `tell me a joke`.
3. **Get the current time:** Include the word `time` in your input. For example, `What is the time?`.
4. **Play a video on YouTube:** Start your input with `play`. For example, `play lo-fi music`.
5. **Greet the chatbot:** You can say `hello`, `hi`, `hey`, `howdy`, or `hola`.

## Requirements

- Python 3.7 or higher
- Streamlit
- pywhatkit
- pyjokes

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/chatbot-with-streamlit.git
    cd chatbot-with-streamlit
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Running the App

1. Run the Streamlit app:

    ```sh
    streamlit run chatbot_streamlit.py
    ```

2. Open a browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Example Usage

- **Greeting:**

    ```sh
    You: Hello
    Chatbot: Hi there!
    ```

- **Asking for the current time:**

    ```sh
    You: What is the time?
    Chatbot: The current time is 14:32:10.
    ```

- **Telling a joke:**

    ```sh
    You: Tell me a joke
    Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!
    ```

- **Searching the web:**

    ```sh
    You: Search Python tutorials
    Chatbot: Searching the web for your query...
    ```

- **Playing a YouTube video:**

    ```sh
    You: Play lo-fi music
    Chatbot: Playing on YouTube...
    ```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

