---
title: "Building a Multi-Protocol Texting App for Raspberry Pi"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Raspberry Pi
  - Kivy
  - Flask
  - SQLite
  - IoT
---

Welcome to the journey of creating a **multi-protocol texting app** for Raspberry Pi! This app bridges communication across devices using **TCP/IP**, **UART**, and more. In this post, we’ll explore the project's development, challenges, and future plans.

<!--more-->

## **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Implementation Details](#implementation-details)  
4. [Demo GIFs](#demo-gifs)  
5. [Challenges and Improvements](#challenges-and-improvements)  
6. [Future Plans](#future-plans)  

---

### **Project Overview**

The **Raspberry Pi Texting App** enables seamless communication between devices using protocols like **TCP/IP** and **UART**. Designed for flexibility, this app can run on various Raspberry Pi models and PCs, making it a versatile tool for IoT, embedded systems, and robotics projects.

---

### **Features**

1. **Multi-Protocol Support**  
   - **TCP/IP**: Includes both master (server) and client modes.  
   - **UART**: Basic serial communication.  

2. **User-Friendly Interface**  
   - Built with **Kivy**, providing a responsive UI for protocol management and message handling.  

3. **Message History**  
   - Stores chat history in an SQLite database for retrieval and filtering.  

4. **REST API**  
   - Flask-based API for integrating with other services or applications.

---

### **Implementation Details**

#### **1. Protocol Handlers**
- **TCP/IP Master and Client:**  
  The `EthernetMasterHandler` and `EthernetClientHandler` manage socket communication, handling multiple clients and message queues.

- **UART Communication:**  
  A simple `UARTHandler` facilitates serial communication, supporting basic `send` and `receive` operations.

#### **2. User Interface**
The app uses **Kivy** for the UI, featuring:
- Protocol selection.
- Chat history display.
- Real-time message updates.

#### **3. Database**
SQLite powers the backend, storing messages with metadata like protocol, sender, and timestamps.

#### **4. REST API**
The Flask API enables:
- Adding new messages.
- Retrieving filtered chat history.

---

### **Demo GIFs**

Here are some demos showcasing the app in action:

### **1. Laptop Ubuntu Environment**  
![Laptop Ubuntu Environment](asset/2025_01_03_pcUbuntu_output.gif)

### **2. Raspberry Pi 400 (Master Server)**  
![Raspberry Pi 400 (Master Server)](asset/2025_01_03_pi400output.gif)

### **3. Raspberry Pi 3B+ (Client)**  
![Raspberry Pi 3B+ (Client)](asset/2025_01_03_pi3bplus_output.gif)

---

### **Challenges and Improvements**

#### **Challenges**
1. **Performance on Raspberry Pi 3B+**  
   - Rendering issues and slow performance on RPI OS GUI.

2. **Manual Configuration**  
   - Requires manual edits to configure the server IP in `chatapp.py`.

#### **Planned Improvements**
1. **Raspberry Pi OS Lite**  
   - Testing the app on RPI OS Lite for better performance on Pi 3B+.

2. **User-Defined Master Server IP**  
   - Adding an input field for the user to specify the master server IP dynamically.

---

### **Future Plans**

1. **Add More Protocols:**  
   - Extend support to SPI, I2C, and CAN for IoT and robotics applications.

2. **Improve UI Performance:**  
   - Optimize Kivy rendering for low-power devices like Raspberry Pi 3B+.

3. **Cloud Integration:**  
   - Enable remote communication through a cloud-based API.

---

### **Conclusion**

This project demonstrates how Raspberry Pi can serve as a flexible communication hub for IoT and embedded systems. Whether you're connecting robots, sensors, or other devices, the **Raspberry Pi Texting App** provides a robust foundation for multi-protocol communication.

Stay tuned for updates and improvements! If you have questions or ideas for features, feel free to reach out.

