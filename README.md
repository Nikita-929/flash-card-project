# flash-card-project
This is a simple Python Tkinter flashcard app designed to help you learn and memorize French-English word pairs. The app presents flashcards with French words and flips them to show the English translation after a few seconds. You can mark the words you’ve learned to focus on new ones each session.

🧩 Features
⏱️ Auto Flip: Flashcards flip after 3 seconds.

✅ Track Progress: Learned words are saved and won't reappear.

🖼️ Visual Interface: Built using Tkinter with image-based cards.

🔄 Random Selection: Words are picked randomly for better retention.

📁 Project Structure
bash
Copy code
flash-card-project/
├── data/
│   ├── french_words.csv          # Original vocabulary list
│   └── words_to_learn.csv        # Auto-generated list for tracking progress
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
├── main.py                        # Main Python script
└── README.md
💾 Requirements
Python 3.x

pandas

tkinter (comes pre-installed with most Python distributions)

Install dependencies:
bash
Copy code
pip install pandas
▶️ How to Run the App
Download or clone the repository.

Ensure french_words.csv is in the data/ folder.

Run the Python file:

bash
Copy code
python main.py
📊 How It Works
When the app launches, it loads words_to_learn.csv if available, or falls back to french_words.csv.

You see a French word → wait 3 seconds → it flips to show the English translation.

Click:

✅ if you know the word (removes it from the list).

❌ to skip (keeps it for future review).

Your progress is saved to words_to_learn.csv.

🚧 Future Improvements
Add audio pronunciation.

Support for additional languages.

Include categories (verbs, nouns, etc.).

Show progress chart.

