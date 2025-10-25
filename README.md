# Tone Buddy: AI-Powered Communication Tone Assistant

## Project Overview
This is a Python-based desktop application prototype developed for the 52685 Working with Data and Code assessment. The project uses natural language processing (NLP) to analyze text message tones and emotions (e.g., angry, sad, happy, excited, sarcastic), providing rephrasing suggestions, emojis, and text-to-speech playback to reduce misunderstandings in digital communication. It draws from communication principles (e.g., Mehrabian's non-verbal cues) and adapts tones for empathy, especially aiding non-native speakers.

Key features:
* Emotion detection: Refines sentiment using polarity, subjectivity, and keyword heuristics.
* Dynamic suggestions: Rule-based rephrasings with randomization for variety.
* Interactive GUI: Real-time analysis, suggestion regeneration, and audio playback.
* Original code focus: Custom classes and logic for NLP processing and UI, with acknowledgments for libraries.

This prototype emphasizes code literacy through original contributions like conditional emotion mapping and modular classes, rather than complex outputs.

## Requirements
* **Environment**: Python 3.12+ (standard installation; tested on Windows/Mac/Linux).
* **Dependencies**: `textblob` (sentiment), `nltk` (tokenization), `pyttsx3` (TTS), `emoji` (visuals), and Python's `random` module. No external assets required.
* **Hardware**: Computer with speakers for TTS.

## File Structure
* `main.py`: Core code with `ToneAnalyzer` (NLP/emotion logic) and `MessageGUI` (UI/interactions).
* `requirements.txt`: List of dependencies for pip installation.
* `versions/`: (Optional) Folder with earlier prototypes (e.g., `v1\_basic\_sentiment.py` for initial version without emotion diversity).

No additional assets (e.g., media files); all functionality generated via code and libraries. Previous versions demonstrate iteration if included.

## How to Run the Prototype
1. Clone the repository: `https://github.com/huilixie-dotcom/Tone-Buddy`.
2. Navigate to the folder: ` Tone-Buddy`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Download NLTK data (run once): Open Python and execute `import nltk; nltk.download('punkt'); nltk.download('punkt\_tab')`.
5. Run the code: `Tone-Buddy.py`.
6. Interact with the GUI: Enter text, click "Analyze Tone" for results (tone, emotion, scores, suggestion, emoji); "Get New Suggestion" for alternatives; "Speak Message" for audio.
7. Debug: Error handling for empty input; console may show traces if issues arise.

Example output: For "I hate this!", detects "Angry", suggests "I dislike this – let's discuss calmly", adds 😠, and speaks aloud.

## Acknowledgments
* TextBlob for sentiment (Loria, S. (2024). *TextBlob: Simplified text processing*. https://textblob.readthedocs.io/en/dev/).
* NLTK for preprocessing (Bird, S., Klein, E., \& Loper, E. (2009). *Natural language processing with Python*. O'Reilly Media.).
* Tkinter for GUI (Python Software Foundation. (2024). *Tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html).
* pyttsx3 for TTS (Aqrabawi, N. (2017). pyttsx3. https://github.com/nateshmbhat/pyttsx3).
* Emoji library (emoji. (2024). https://github.com/carpedm20/emoji/).
* Inspired by: Mehrabian, A. (1971). *Silent messages*; Jurafsky \& Martin (2023) on NLP.
* All original code (e.g., emotion heuristics, suggestion randomization) by Huili Xie. Borrowed elements clearly commented in source files.

## License

This project is for educational purposes. Feel free to modify, but cite if reusing.# Tone-Buddy
