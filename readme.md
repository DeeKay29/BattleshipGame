<!-- Project shields -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<div align="center">
  <a href="https://github.com/DeeKay29/BattleshipGame">
    <img src="./static/images/banner.png" alt="banner">
  </a>
  <br><br><br>
  <a href="https://github.com/DeeKay29/BattleshipGame">
    <img src="./static/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">DeeKay</h3>
  <p>Student | Freelance Graphic Designer</p>

</div>

***

# Battleship Game

Battleship (also known as Sea Battle) is a strategy type guessing game for two players. It is played on ruled grids on which each player's fleet of warships are marked. And here we go with python code where u can play alone in battleships. Your PC would generate a board for you and you can play without friends.

The user can choose from three difficulty modes, and then start the game against the computer. If he manages to shoot down all the ships before the end of the game, he wins, and if not, his fleet is completely sunk.

Join the great gameplay today!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

***

## Getting started

Make sure you have python minium 3.1.x installed before proceeding to the next steps.

### Prerequisites

Make sure your pip version is up to date...

```sh
python.exe -m pip install --upgrade pip
```

... then install the required libraries.

```sh
pip install beautifultable --user
```

```sh
python3 -m pip install --upgrade termcolor
```

```sh
python -m pip3 install flask
```

### Installation

1. Clone the repo.

   ```sh
   git clone https://github.com/DeeKay29/BattleshipGame.git
   ```

2. Install required libraries.

   ```sh
   pip install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

***

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

***

## Usage

In order to launch the application, the following command should be called in the terminal:

```sh
<your-python-directory-path>/python.exe <your-cloned-repo-path>/app.py
```

Launching the above file in the terminal should result in the enabling of the `localhost` server on the port of `8000`. To go to the page, use any browser and paste the link `http: //127.0.0.1: 8000/views/`. After correctly passing all the steps, you should be able to use all available functionalities. For more information, look at the <a href="#changelog">Changelog</a> section.

***

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

***

## Contact

Go ahead. Contact me. Use the links below to reach me. Although I am a beginner, I will try to answer any doubts.

Dawid Kurowski - [Follow me on LinkedIn]([linkedin-url]) - dkurowski.kontakt@gmail.com

Project link: [Battleship Game by @DeeKay29]([project-link])

<p align="right">(<a href="#readme-top">back to top</a>)</p>

***

## Changelog

Changes introduced in the last (**v.1.2**) update:

- [x] File structure restructuring (again).
- [x] Reconstruction of the program initiating the program: To start the server. **Note:** Launching the game requires access to the previous version. Currently, `app.py` is responsible for displaying the page, not launching the Battleship Game.
- [x] Setting up Flask server.
- [ ] Reconstruction of logic to launch the Battleship Game via the website.

### Previous changes

Changes introduced in the **v.1.1** update:

- [x] File structure restructuring
- [x] Fixing placing ships on board

Changes introduced in the **v.1.0** update:

- [x] Fixing bugs and making sure the program is working properly

The most important changes introduced from version **v.0.1** to version **v.0.8**:

- [x] Creating empty game board
- [x] Defining game parameters
- [x] Generating ships location
- [x] Generating ships coordinates
- [x] Placing ships on board
- [x] Converting user coordinates
- [x] Game logic

***

## Useful resources

The following materials proved to be very helpful when building the application. I will try to describe them as accurately as possible so that you can look into them in case of a problem.

1. <a href="https://www.youtube.com/watch?v=kng-mJJby8g&ab_channel=TechWithTim" target="_blank">Make A Python Website As Fast As Possible!</a> by <a href="https://www.youtube.com/@TechWithTim" target="_blank">@TechWithTim</a> on YouTube:
   - Flask setup,
   - Creating views / routes,
   - Rendering HTML,
   - Template variables,
   - URL parameters,
   - Query parameters,
   - Returning JSON,
   - Getting JSON data,
   - Redirect,
   - Adding JavaScript.
2. <a hreg="https://github.com/othneildrew/Best-README-Template" target="_blank">Best-README-Template</a> on GitHub.

<!-- Links -->
[project-link]: https://github.com/DeeKay29/BattleshipGame
[contributors-shield]: https://img.shields.io/github/contributors/DeeKay29/BattleshipGame.svg?style=for-the-badge
[contributors-url]: https://github.com/DeeKay29/BattleshipGame/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DeeKay29/BattleshipGame.svg?style=for-the-badge
[forks-url]: https://github.com/DeeKay29/BattleshipGame/network/members
[stars-shield]: https://img.shields.io/github/stars/DeeKay29/BattleshipGame.svg?style=for-the-badge
[stars-url]: https://github.com/DeeKay29/BattleshipGame/stargazers
[issues-shield]: https://img.shields.io/github/issues/DeeKay29/BattleshipGame.svg?style=for-the-badge
[issues-url]: https://github.com/DeeKay29/BattleshipGame/issues
[license-shield]: https://img.shields.io/github/license/DeeKay29/BattleshipGame.svg?style=for-the-badge
[license-url]: https://github.com/DeeKay29/BattleshipGame/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dawid-kurowski/
