import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
import pyttsx3
import emoji
import random  # Added for randomizing suggestions for more variety

# Download necessary NLTK data (run once if needed)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

class ToneAnalyzer:
   
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize TTS engine
        # Keyword lists for finer emotion detection (original heuristic addition)
        self.angry_keywords = ['angry', 'hate', 'furious', 'mad', 'annoyed']
        self.sad_keywords = ['sad', 'depressed', 'sorry', 'hurt', 'disappointed']
        self.happy_keywords = ['happy', 'great', 'awesome', 'love', 'excited']
        self.sarcastic_keywords = ['sure', 'whatever', 'yeah right', 'oh great']

    def preprocess_text(self, text):
      
        tokens = word_tokenize(text.lower())  # Lowercase for keyword matching
        return ' '.join(tokens), tokens  # Return both processed text and tokens

    def analyze_sentiment(self, text):
       
        processed_text, tokens = self.preprocess_text(text)
        blob = TextBlob(processed_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Basic tone
        if polarity > 0.1:
            base_tone = "Positive"
        elif polarity < -0.1:
            base_tone = "Negative"
        else:
            base_tone = "Neutral"

        # Refine to more diverse emotions using keywords and polarity/subjectivity
        emotion = base_tone  # Default
        if any(word in tokens for word in self.angry_keywords) and polarity < 0:
            emotion = "Angry"
        elif any(word in tokens for word in self.sad_keywords) and polarity < 0:
            emotion = "Sad"
        elif any(word in tokens for word in self.happy_keywords) and polarity > 0:
            emotion = "Happy"
        elif any(word in tokens for word in self.happy_keywords) and subjectivity > 0.5:
            emotion = "Excited"
        elif any(word in tokens for word in self.sarcastic_keywords) and subjectivity > 0.5:
            emotion = "Sarcastic"
        # Add more conditions as needed for further diversity

        return {
            "polarity": polarity,
            "subjectivity": subjectivity,
            "tone": base_tone,
            "emotion": emotion
        }

    def suggest_improvements(self, text, sentiment):
      
        emotion = sentiment["emotion"]
        suggestions = []

        if emotion == "Angry":
            suggestions = [
                f"Soften the anger: {text.replace('hate', 'dislike').replace('mad', 'frustrated')}",
                f"Try a calmer version: Let's discuss this calmly instead.",
                f"Rephrase neutrally: {text} – perhaps add 'I feel' to express better."
            ]
        elif emotion == "Sad":
            suggestions = [
                f"Add hope: {text} but things will get better.",
                f"Make it more uplifting: Focus on positives like {text.replace('sad', 'challenging')}.",
                f"Empathetic twist: I understand, {text}."
            ]
        elif emotion == "Happy":
            suggestions = [
                "Your message is joyful already! Keep it.",
                f"Amplify the happiness: {text} 🎉",
                f"Share the vibe: Sounds fun, {text}!"
            ]
        elif emotion == "Excited":
            suggestions = [
                "Great energy! No changes needed.",
                f"Build on excitement: {text} – can't wait!",
                f"Add enthusiasm: {text} 😄"
            ]
        elif emotion == "Sarcastic":
            suggestions = [
                f"Avoid sarcasm if possible: Rephrase sincerely as {text.replace('yeah right', 'really?')}.",
                f"Clarify intent: {text} (just kidding!)",
                f"Go direct: Say what you mean without irony."
            ]
        elif sentiment["tone"] == "Negative":
            suggestions = [
                f"Consider rephrasing positively: {text.replace('bad', 'challenging').replace('hate', 'prefer not to')}",
                f"Soften it: {text} – maybe add 'please' or 'thank you'."
            ]
        elif sentiment["tone"] == "Neutral":
            suggestions = [
                f"Add some warmth: {text} 😊",
                f"Make it engaging: {text} – what do you think?"
            ]
        else:
            suggestions = ["Your message seems positive already!"]

        # Randomize for diversity (pick one randomly)
        return random.choice(suggestions)

    def add_emoji(self, sentiment):
    
        emotion = sentiment["emotion"]
        emoji_options = {
            "Angry": [":angry_face:", ":face_with_symbols_on_mouth:"],
            "Sad": [":frowning_face:", ":crying_face:"],
            "Happy": [":grinning_face:", ":smiling_face_with_hearts:"],
            "Excited": [":star-struck:", ":partying_face:"],
            "Sarcastic": [":face_with_rolling_eyes:", ":upside-down_face:"],
            "Positive": [":thumbs_up:", ":sparkles:"],
            "Negative": [":thumbs_down:", ":warning:"],
            "Neutral": [":neutral_face:", ":expressionless_face:"]
        }.get(emotion, [":neutral_face:"])

        return emoji.emojize(random.choice(emoji_options))

    def speak_message(self, text):
      
        self.engine.say(text)
        self.engine.runAndWait()

class MessageGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tone Buddy")
        self.root.geometry("600x450")  # Slightly larger for new elements

        self.analyzer = ToneAnalyzer()  # Instance of ToneAnalyzer

        # GUI Elements
        self.label = tk.Label(self.root, text="Enter your message:")
        self.label.pack(pady=10)

        self.text_entry = tk.Text(self.root, height=5, width=50)
        self.text_entry.pack(pady=10)

        self.analyze_button = tk.Button(self.root, text="Analyze Tone", command=self.analyze)
        self.analyze_button.pack(pady=5)

        self.suggest_button = tk.Button(self.root, text="Get New Suggestion", command=self.regenerate_suggestion, state=tk.DISABLED)
        self.suggest_button.pack(pady=5)

        self.speak_button = tk.Button(self.root, text="Speak Message", command=self.speak)
        self.speak_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", wraplength=500)
        self.result_label.pack(pady=10)

        # Store last sentiment for regeneration
        self.last_sentiment = None
        self.last_message = None

    def analyze(self):

        message = self.text_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message.")
            return

        sentiment = self.analyzer.analyze_sentiment(message)
        suggestion = self.analyzer.suggest_improvements(message, sentiment)
        emo = self.analyzer.add_emoji(sentiment)

        result = (
            f"Tone: {sentiment['tone']}\n"
            f"Emotion: {sentiment['emotion']}\n"
            f"Polarity: {sentiment['polarity']:.2f}\n"
            f"Subjectivity: {sentiment['subjectivity']:.2f}\n"
            f"Suggestion: {suggestion}\n"
            f"Emoji: {emo}"
        )
        self.result_label.config(text=result)

        # Store for regeneration
        self.last_sentiment = sentiment
        self.last_message = message
        self.suggest_button.config(state=tk.NORMAL)

    def regenerate_suggestion(self):
       
        if not self.last_message or not self.last_sentiment:
            messagebox.showwarning("No Analysis", "Please analyze first.")
            return

        new_suggestion = self.analyzer.suggest_improvements(self.last_message, self.last_sentiment)
        new_emo = self.analyzer.add_emoji(self.last_sentiment)

        current_text = self.result_label.cget("text")
        # Update only suggestion and emoji parts
        updated_text = current_text.split("Suggestion:")[0] + f"Suggestion: {new_suggestion}\nEmoji: {new_emo}"
        self.result_label.config(text=updated_text)

    def speak(self):
       
        message = self.text_entry.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message.")
            return
        self.analyzer.speak_message(message)

    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

# Main execution block
if __name__ == "__main__":
    app = MessageGUI()
    app.run()
