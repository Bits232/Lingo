

🌍 **Lingo**
Lingo is a multilingual, offline-first educational platform built to break language barriers and make learning accessible for everyone.

This lightweight app offers programming, science, and essential courses in local languages, including:

English

Yoruba

Spanish

Swahili

Hindi

Tagalog

It’s designed especially for communities with limited internet access, ensuring quality education is available for everyone, everywhere.

🚀 **Features**
🈚 Full Multilingual UI — The app interface and course content are localized into different languages.

📶 Offline-First — Works without an internet connection; all data is stored locally.

🧠 Smooth Navigation — Simple, intuitive back button system for easy learning flow.

🗃️ Local Storage — Language preferences are saved securely with SQLite.

📚 Dynamic Course Loading — Courses load from language-specific JSON files at runtime.


🛠 **How to Run Lingo Locally**
1. Clone the Repository
git clone https://github.com/Bits232/Lingo
cd Lingo
2. Install Dependencies
Make sure you have Python 3.10+ installed.

Install Flet:

pip install flet
(Optionally, install SQLite if it's not already included — most Python setups have it.)

3. Folder Structure

Lingo/
│
├── main.py
├── database.py
├── data_loader.py
├── home.py
├── course_page.py
├── subcategory_page.py
├── courses/
│   ├── english.json
│   ├── yoruba.json
│   ├── spanish.json
│   ├── swahili.json
│   ├── hindi.json
│   ├── tagalog.json
└── app.db (generated automatically on first run)
📁 courses/ folder contains all course content in different languages.

4. Run the App

python main.py
The app will open in your browser or as a desktop window (depending on your Flet settings).

📚 **How Lingo Works**
On the first launch, users select a language.

Their choice is saved locally using SQLite.

On future launches, Lingo remembers their language and directly loads the homepage with courses in that language.

Course content is loaded from local JSON files to ensure offline functionality.

🏆 **Built For**
Social Good Hackathons & Innovation Challenges
Empowering communities with education — anywhere, anytime, in any language.

🤝 **Contributing**
Pull requests are welcome!
If you want to add new languages or courses, feel free to fork the repo and create a PR.

📜 **License**
This project is open-source and free for educational and non-profit use.

🙌 **Thank You for Supporting Lingo!**
