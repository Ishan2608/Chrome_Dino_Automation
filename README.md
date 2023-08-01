# Chrome's Dino Automation

Welcome to Chrome's Dino Automation! This GitHub repository hosts an exciting project that automates the gameplay of the classic Chrome Dino Game. Say goodbye to manual efforts and let this application handle the gameplay for you. Sit back, relax, and watch the dino conquer the obstacles on its own.

## Overview

Chrome's Dino Automation is an intermediate-level project that takes the hassle out of playing the popular Chrome Dino Game. Instead of manually controlling the dino, this application uses image processing techniques to detect obstacles near the dinosaur. Based on the detection results, the dino is automatically made to duck or jump to avoid obstacles and keep the gameplay going in an infinite loop.

## Technologies Used

Chrome's Dino Automation project leverages the following technologies to automate the gameplay:

- **Python:** The core language that powers the application's logic and image processing.

- **PyAutoGUI Library:** Used to capture screenshots and simulate keyboard inputs to control the dino's movements.
- **Pillow:** Used to work with images.

## How It Works

To experience Chrome's Dino Automation:

1. Clone this repository to your local machine.

2. Ensure you have Python installed on your system.

3. Install the required libraries by running:

```
pip install pyautogui
```

4. Open the Chrome Dino Game in your web browser.

5. Run the `main.py` script in your Python environment.

6. The application will start capturing screenshots of the game screen.

7. If an object is detected near the dinosaur, the application will automatically make the dino duck or jump to avoid the obstacle.

8. The automation will continue to run in an infinite loop, handling the gameplay for you.

## Important Note

Please ensure to adjust the coordinates of obstacle detection according to your own screen resolution. This step is crucial to ensure accurate detection and smooth gameplay automation.

## Contribution

We welcome contributions from intermediate-level developers interested in enhancing Chrome's Dino Automation. Whether you have ideas for improving detection accuracy, optimizing gameplay, or adding new features, your contributions are highly valued. Please feel free to raise issues and submit pull requests to contribute to the project's growth.
