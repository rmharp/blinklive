# BlinkLive

BlinkLive offers a pair of Python scripts designed to extend the live view functionality of Blink Security Systems without requiring a subscription. These scripts automate interactions with the Blink app interface to bypass time limits on live viewing.

## Scripts in This Repository

### `continue?.py`
- **Target Platform:** macOS
- **Functionality:** Automates interactions with the Blink app downloaded from the App Store. Utilizes RGB value recognition for the 'continue' button in the app, enabling extended live view.
- **Setup:** Users need to identify and set the RGB values of the 'continue' button specific to their system. A default value is provided, but customization may be necessary for optimal performance.

### `continue_v2.py`
- **Target Platform:** Non-macOS Systems (via BlueStacks)
- **Functionality:** Similar to `continue?.py`, but adapted for systems where the Blink app is not directly available from the App Store. It works through the BlueStacks emulator.
- **Setup:** Requires setting RGB values as per the system's display characteristics. The process for RGB value identification is the same as in `continue?.py`.

## Usage and Customization
Both scripts operate by taking periodic screenshots, identifying the 'continue' button based on RGB values, and automating mouse movements to click the button. Users need to set the RGB values and tolerance for their specific setup. Instructions for finding RGB values are provided [here](https://imagecolorpicker.com/en), with a link to an online RGB finder tool. After setting the RGB, adjust the tolerance constant as neccesary until the minimum is achieved that can accurately, reliably identify the continue? button and play button.

## Disclaimer
These scripts are intended for personal use and to enhance user experience. Users should ensure compliance with Blink's terms of service and applicable laws.
