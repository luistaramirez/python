# Tombola de Bolos

## Overview
The Tombola de Bolos is a lottery application built using Python and Tkinter. It allows users to generate random lottery numbers, save results to an Excel file, and analyze historical data to make predictions about future draws. The application is designed to be user-friendly and provides various functionalities to enhance the lottery experience.

## Features
- Generate random lottery numbers.
- Save generated numbers and results to an Excel file.
- Predict numbers based on historical data.
- Analyze hot and cold numbers from previous draws.
- User-friendly graphical interface.

## Installation
To set up the Tombola de Bolos application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd tombola-de-bolos
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed on your system. Then, install the necessary libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command in your terminal:
```bash
python src/tombola_de_bolos.py
```

Once the application is running, you can:
- Generate random numbers by clicking the "Sacar número" button.
- Generate all numbers at once using the "Generar todos" button.
- Analyze hot and cold numbers by clicking the respective buttons.
- Predict numbers based on historical data stored in the Excel file.

## Data Storage
The application uses an Excel file (`data/numeros_generados.xlsx`) to store the generated lottery numbers and results. This file is automatically created if it does not exist and is updated with each draw.

## Contributing
Contributions are welcome! If you would like to contribute to the Tombola de Bolos project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Tkinter for the graphical user interface.
- OpenPyXL for handling Excel files.
- Matplotlib for data visualization.