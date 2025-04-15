# Tombola de Bolos

## Overview
The **Tombola de Bolos** is a lottery application built using Python and Tkinter. It allows users to generate random lottery numbers, save results to an Excel file, and analyze historical data to make predictions about future draws. The application is designed to be user-friendly and provides various functionalities for both casual users and those interested in statistical analysis.

## Features
- Generate random lottery numbers.
- Save drawn numbers to an Excel spreadsheet.
- Predict future numbers based on historical data.
- Analyze hot and cold numbers from previous draws.
- User-friendly graphical interface built with Tkinter.

## Installation
To set up the Tombola de Bolos application, follow these steps:

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/tombola-de-bolos.git
   cd tombola-de-bolos
   ```

2. **Install the required dependencies:**
   Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the dependencies listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command in your terminal:
```
python src/tombola_de_bolos.py
```

Once the application is running, you can:
- Generate random numbers by clicking the "Sacar número" button.
- View the drawn numbers in the display area.
- Analyze hot and cold numbers using the provided buttons.
- Save results to the Excel file for future reference.

## Data Storage
The application uses an Excel file (`data/numeros_generados.xlsx`) to store the generated lottery numbers and results. This file is automatically created if it does not exist.

## Contributing
Contributions are welcome! If you would like to contribute to the Tombola de Bolos project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Tkinter for the graphical user interface.
- OpenPyXL for handling Excel files.
- Matplotlib for data visualization.