# KBA-Internship
FHE enabled voting system

# FHE-Based Voting System with JWT Authentication
This project implements a voting system using Fully Homomorphic Encryption (FHE) and JWT (JSON Web Tokens) for secure user authentication. It allows encrypted voting and secure tallying, ensuring that votes remain private and tamper-proof. The system can be used in scenarios where sensitive voting data needs to remain confidential.

# Features:
FHE Encryption: Secure voting process using homomorphic encryption, which allows for computations on encrypted data without decryption.
JWT Authentication: Users are authenticated via encrypted JWT tokens to ensure secure access to the system.
Voting Mechanism: Users can vote on multiple candidates, and their votes are encrypted and processed without being decrypted at any point.
API Integration: A RESTful API is exposed to interact with the system, making it easy to integrate with other applications.
MongoDB: Used as the backend to store encrypted votes, ensuring scalability and reliability.

# Key Components:
Frontend: Simple user interface to vote securely.
Backend: Flask API to handle voting operations and retrieve results.
Security: JWT tokens for user authentication and FHE for vote encryption.

# Tech Stack:
Python (Flask)
JWT Authentication
MongoDB (for backend storage)
FHE Encryption (for secure voting)

# Basic Structure
![FHEvoting](https://github.com/user-attachments/assets/c424be29-d598-4ee2-9c8b-96d943a917a8)
