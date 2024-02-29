# Battleship Game

This project is a Python implementation of the classic Battleship game. 
The plan was to enhance it with a graphical interface using Pygame, but that will be tackled later on.

## Game Overview

In this implementation of Battleship, players set up their ships on a grid and then take turns guessing the locations of their opponent's ships. The goal is to sink all of the opponent's ships before they sink all of yours. This version brings an interactive console-based interface to life, enhanced with colorful output thanks to the Colorama library, making the gameplay experience more engaging and visually appealing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python (3.x or higher recommended)
- Pip (Python package manager)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
    ```bash
    git clone https://github.com/smue-smue/battleship_game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd battleship_game
    ```

3. Create a virtual environment:
    - On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python src/main.py
    ```

## Enhancement with Colorama

To make the game output more visually appealing, we utilized the Colorama library. This addition allows us to output text in various colors and styles, enhancing the overall user experience and making the game interface more intuitive and engaging.


## Structure

The project is structured as follows:

- `docs/`: Documentation related to the project.
- `src/`: Contains the source code for the game.
- `tests/`: Test scripts for the game.
- `venv/`: Virtual environment for managing dependencies.


## Authors

- **Alexandra** - [Nebulaleaf](https://github.com/Nebulaleaf)
- **Sandra** - [smue-smue](https://github.com/smue-smue)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement

We would like to thank [PyLadies Vienna](https://pyladies.at/) for offering the beginners course in Autumn 2023, which helped us start our journey into Python programming. This Battleship game project, a collaborative effort between [Nebulaleaf](https://github.com/Nebulaleaf) and [smue-smue](https://github.com/smue-smue), serves as our final assignment for the course. We appreciate the guidance, knowledge, and support provided by the PyLadies Vienna team, essential in helping us reach this milestone. Special thanks to the mentors and fellow PyLadies of Autumn 2023 for their encouragement and advice throughout the course.

PyLadies is an international mentorship group with a focus on helping more women become active participants and leaders in the Python open-source community. Their mission is to promote, educate and advance a diverse Python community through outreach, education, conferences, events and social gatherings.