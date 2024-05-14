**Network Configuration Manager**


**Overview**

Network Configuration Manager is a Python script designed to manage and apply different network authentication configurations on a host system. It supports various configuration tasks including setting up authentication methods, adding RADIUS users, managing MAC addresses, adding MSCHAPv2 users, and generating TLS certificates.
Features

    Apply Network Configurations: Choose from multiple pre-defined network configurations (WEP, WPA2, WPA3, etc.) and apply them to the host system.
    Add RADIUS Users: Easily add new users to the RADIUS server with specified usernames and passwords.
    Manage MAC Addresses: Add new MAC addresses to a whitelist for network access control.
    Add MSCHAPv2 Users: Add users to MSCHAPv2 authentication with specified credentials.
    Generate TLS Certificates: Create and manage TLS certificates for secure network communications.
    

**Prerequisites**

    Python 3.x
    os module (standard library)
    shutil module (standard library)
    openssl installed on the host system
    rar installed for compressing TLS keys and certificates
    

**Installation**

    Clone the repository or download the script to your local machine.
    Ensure you have the necessary permissions to execute system-level commands.
    Install any required dependencies.
    

**Usage**

    Run the Script: Execute the script using Python.

    bash

    python network_config_manager.py

    Choose an Option: Follow the on-screen prompts to choose one of the following options:
        1. Choose Authentication Method: Select and apply a network configuration from the predefined options.
        2. Add RADIUS User: Add a new user to the RADIUS server.
        3. Add MAC Address: Add a MAC address to the whitelist.
        4. Add MSCHAPv2 User: Add a new user to MSCHAPv2 authentication.
        5. Generate TLS Certificate: Generate and secure a TLS certificate for a new user.



**Configuration Files**

The script uses various configuration files stored in specific directories:

    /etc/hostapd/hostapd.conf - Hostapd configuration file.
    /home/alex/configuraciones/ - Directory containing network configuration files.
    /etc/freeradius/3.0/users - RADIUS users configuration file.
    /home/alex/macs/accept_mac.txt - MAC address whitelist file.
    /home/alex/configuraciones/eap_user2 - MSCHAPv2 users configuration file.
    /home/alex/Descargas/ - Directory for generating TLS keys and certificates.
    /home/alex/server/ - Directory containing CA certificate and key files.
    

**Contributing**

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.


**License**

This project is licensed under the MIT License. See the LICENSE file for details.
Contact


For any questions or support, please contact Alex.


This script simplifies network configuration management, allowing administrators to easily switch authentication methods and manage users and devices. Use it responsibly and ensure you have appropriate permissions before making changes to your network settings.
