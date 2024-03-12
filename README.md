# Optical Character Recognition (OCR) Web Application
#### Video Demo:  <URL https://youtu.be/n5HzDSVU3Us>
#### Description:


## Introduction

Greetings! I'm Fatemeh Saveh, a passionate Data Scientist who recently completed the renowned CS50x course. This project signifies the culmination of my journey, merging my data science expertise with newfound programming skills acquired during CS50x. The project is an Optical Character Recognition (OCR) web application developed using Python Flask, SQLAlchemy, HTML, CSS, and JavaScript. Its primary purpose is to seamlessly convert images containing text into editable and searchable data.

## Project Focus and Goals

As an experienced Python developer before undertaking CS50x, my primary objective with this final project was to solidify my understanding and application of the new skills I acquired during the course, specifically Flask for backend development, databases using SQLAlchemy, and frontend technologies like HTML, CSS, and JavaScript.

This OCR web application stands as a practical embodiment of those skills. Its design and interaction focus on user-friendliness while showcasing the integration of these technologies into an end-to-end project. While there are various AI-based OCR solutions available, I chose to implement EasyOCR for its efficiency and capability to handle tasks like traffic sign recognition and many others.

## Utilizing EasyOCR

In this project, EasyOCR plays a central role in the conversion of images to text. EasyOCR is a versatile OCR tool supporting over 80 languages, enabling quick conversion and transcription of text from images. Its simplicity and effectiveness in tasks such as traffic sign recognition align perfectly with the project's objectives.

## Focus on Flask, Database, and Frontend Development

The primary focus of this project was not solely on the choice of OCR library but rather on the seamless integration of various technologies into a cohesive application. The utilization of Flask facilitated backend development, allowing efficient handling of HTTP requests and responses. SQLAlchemy empowered smooth database management, ensuring secure storage and retrieval of user information.

Additionally, the frontend development using HTML, CSS, and JavaScript was a significant learning curve that this project embraced. It enabled the creation of a user-friendly interface, enhancing user interaction and accessibility.

## Conclusion

This project's significance lies not only in its functionality but in its role as a learning tool. It represents the culmination of skills learned throughout the CS50x journey, serving as a testament to the application of these newfound abilities in a practical and tangible manner.



## Features

### User-Friendly Authentication
The application boasts a robust authentication system, providing a seamless onboarding experience for users. New users can securely register with unique usernames, email addresses, and passwords. Existing users can conveniently log in using their credentials, ensuring data security through password hashing.

### Image-to-Text Conversion
A pivotal aspect of this application is its capability to convert images to text effortlessly. Users can upload images in various formats ('jpg', 'jpeg', 'png', 'jfif'), the application employs the EasyOCR library for Optical Character Recognition. Extracted text is presented to users in a readable format, facilitating quick access to information stored within images.

### Seamless Database Integration
For efficient data management and user interaction, I've seamlessly integrated SQLAlchemy with a SQLite database. This integration ensures the secure storage and retrieval of user information, reinforcing the application's reliability and data security.





### Home Page (`/`)
The home page serves as an introduction, providing insights into the application's functionality and purpose in converting images to editable text.

### Sign-Up Page (`/signup`)
New users can register securely by providing essential details such as username, email, and password, ensuring a personalized and secure user experience.

### Login Page (`/login`)
Existing users can conveniently log in using their credentials, gaining access to the image-to-text conversion feature.

### Image Rendering Page (`/image_render`)
Users can easily upload images through the user-friendly interface. Once uploaded, the OCR process initiates, extracting text from the images. The extracted text is displayed in a user-friendly format, allowing easy access to the information captured within the images.



