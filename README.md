# Dodgeball Game 🎯

A fast-paced, arcade-style dodgeball game built using Python and gamebox. Players must dodge incoming balls while eliminating opponents by throwing dodgeballs back. The game increases in difficulty with each level.

## 🎮 Game Overview

**Objective:** Avoid getting hit while eliminating all opponents and progress through increasingly difficult levels.

### Game Mechanics:
* Move left/right to dodge incoming balls
* Throw dodgeballs to eliminate opponents
* Collect food items to regain health (max 3 HP)
* Survive as long as possible!

## 🚀 Features

### Core Features
* User-controlled character movement
* Dynamic difficulty progression
* Health system with collectible power-ups
* Colorful dodgeballs and animated food items
* Multiple levels with increasing challenge

### Technical Highlights
* Built with Python and Flask
* HTML5 Canvas for game rendering
* Real-time gameplay mechanics
* Sprite animation system
* Responsive web design

## 🛠️ Project Structure
```
your-project-folder/
├── app.py                 # Flask application setup
├── main.py               # Entry point
├── README.md             # Project documentation
├── pyproject.toml        # Python dependencies
├── attached_assets/      # Game assets and engine
│   ├── gamebox.py       # Game engine library
│   ├── game.py          # Core game logic
│   ├── food-drink-00.png # Food sprite sheet
│   └── README.md        # Game documentation
└── static/              # Static assets
    ├── js/
    │   └── game.js      # Client-side game logic
    └── css/
        └── style.css    # Game styling
```

## 📋 Prerequisites
- Python 3.11 or higher
- pip (Python package installer)
- Modern web browser with HTML5 support

## 🔧 Installation & Setup

1. **Clone the Repository**
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. **Install Dependencies**
```bash
pip install flask pygame
```

3. **Run the Game**
```bash
python main.py
```

4. **Access the Game**
Open your web browser and navigate to:
```
http://localhost:8080
```

## 🎯 How to Play

### Controls
* Left Arrow (←) - Move left
* Right Arrow (→) - Move right
* D key - Throw dodgeballs
* Spacebar - Start game

### Gameplay Tips
* Dodge incoming balls from enemies
* Collect food items to restore HP (max 3)
* Clear levels by eliminating all enemies
* Watch out for increasing difficulty in higher levels

## ⚠️ Troubleshooting

### Port Issues on macOS
If you encounter a "Port 5000 in use" error:
1. The game now uses port 8080 by default
2. If needed, you can modify the port in `main.py`
3. On macOS, port 5000 is often used by AirPlay Receiver

### Common Issues
1. Missing Dependencies
```bash
pip install -r requirements.txt
```

2. Game Not Loading
- Clear browser cache
- Verify Python version (3.11+)
- Check console for error messages

## 👥 Credits and Collaboration
- This project was created in collaboration with Ben Cohen. It utilizes gamebox, an original work by Luther Tychonievich.
- Game Engine: gamebox by Luther Tychonievich
- Food Sprites: OpenMoji

## 📄 License

This project is open source and available under the [MIT License](LICENSE).