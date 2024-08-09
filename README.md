Description of the Banking Management System with Artificial Intelligence
Overview:
This project implements a simple banking management system that uses Java for the back-end and Python for the artificial intelligence functionality. The solution is designed to run as a desktop application, combining the robust capabilities of Java for managing banking operations with the power of Python for neural network fraud detection.

Technologies Used:

Java:

Banking Functions: Java was used to develop the core of the banking system. The Java code includes functionality for account management, transactions (such as deposit, withdrawal and transfer), and balance inquiry.
HTTP Client: Java was also used to communicate with the Python server, sending transaction data for fraud analysis.
Python:

Artificial Intelligence: We use Python to create a neural network model capable of detecting fraud in banking transactions. Keras libraries (with TensorFlow as backend) were used to create and train the model.
Flask: To integrate artificial intelligence into the Java system, Python uses Flask, a web microframework, to serve the REST API that receives transactions and returns fraud analysis.
Packaging:

PyInstaller: Used to convert the Python script into a standalone executable (.exe), ensuring that the AI ​​model and Flask API can be run on any PC, without needing to install Python.
Launch4j: Tool used to package Java code into an executable (.exe), allowing the system to be easily distributed and run in a Windows environment.
Inno Setup: Used to create a single installer that combines Python and Java executables, simplifying the installation process for the end user.
How It Was Done:

Back-End Development in Java:
The banking system was implemented in Java, ensuring high performance and security for financial operations. Classes such as ContaBancaria and Banco were created to manage accounts and transactions.

AI Model Creation in Python:
Using Keras, we developed a simple neural network to analyze transaction patterns and identify potential fraud. The model was trained with simulated data and then implemented in a Flask API.

Integration between Java and Python:
Communication between the Java system and the Python AI model was carried out via REST API. Java sends transactions to the Flask server, which processes the data using the neural network and returns whether the transaction is suspected of fraud.
