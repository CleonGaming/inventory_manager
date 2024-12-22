## Inventory Management System

This is a terminal-based GUI application written in Python to manage your inventory. It allows you to add, update, delete, and search for items, track quantities, view your inventory list, generate reports, and more.

The project is designed with a simple yet effective interface, ensuring ease of use for users.

### Features

- **Add New Item**: Easily add a new item to the inventory with unique identification.
- **Update Item**: Modify the details of an existing item.
- **Delete Item**: Remove an item from the inventory permanently.
- **Search for an Item**: Quickly find an item in the inventory using search criteria.
- **Update Item Quantity**: Adjust the quantity of items in stock.
- **View Inventory**: Display the entire inventory list.
- **View by Category**: Organize and display items based on their category.
- **Sort Inventory**: Sort inventory items by name, price, or quantity for better organization.
- **Generate Reports**: Create and save reports in .txt format (with plans for future format updates).
- **Admin Mode**: Access administrative features for more control over the system.
- **Exit**: Safely exit the application.

### Technologies Used

- **Programming Language**: Python
- **Database**: MySQL, hosted locally on phpMyAdmin
- **Reports**: Generated in .txt format
- **Unique ID**: Managed using the AUTO_INCREMENT feature in MySQL

### Installation Instructions

1. **Prerequisites:**
    * Make sure you have Python (version 3.x recommended) and pip (package installer) installed on your system. You can download them from [https://www.python.org/downloads/](https://www.python.org/downloads/).
    * Install the required Python libraries:
        ```bash
        pip install mysql-connector-python
        ```
    * Or you can use:
        ```bash
        pip install -r requirements.txt
        ```

2. **Clone the repository:**
    ```bash
    git clone https://github.com/CleonGaming/inventory_manager.git
    ```

3. **Configure Database Connection:**
    * Edit the `inventory_manager.py` file located in the project root directory.
    * Update the following details with your database credentials:
        ```python
        HOST = "localhost"
        USER = "your_username"
        PASSWORD = "your_password"
        DATABASE = "ims"
        ```
        Replace the placeholders with your actual MySQL server address, username, password, and database name.

4. **Set Up MySQL Database:**
   Follow these steps to set up the MySQL database:

   - **Create a Database in MySQL**:
     1. Log in to MySQL:
        ```bash
        mysql -u [username] -p
        ```
        Replace `[username]` with your MySQL username (e.g., `root`). Enter your password when prompted.

     2. Create a new database:
        ```sql
        CREATE DATABASE ims;
        ```
        Replace `ims` with your desired database name.

     - **Use the Database**:
        ```sql
        USE ims;
        ```

     - **Import the SQL File**:
        1. If you're using MySQL command-line, run the following to import the `ims.sql` file:
           ```sql
           source /path/to/ims.sql;
           ```
           Replace `/path/to/ims.sql` with the full path to your `ims.sql` file.

        2. Alternatively, you can import the SQL file directly from the terminal:
           ```bash
           /path/to/mysql -u [username] -p ims < /path/to/ims.sql
           ```
           Replace:
           - `/path/to/mysql` with the path to your MySQL executable (e.g., `/usr/bin/mysql`).
           - `[username]` with your MySQL username (e.g., `root`).
           - `ims` with the name of your database.
           - `/path/to/ims.sql` with the full path to your SQL file.

     - **Update the Database Connection Details** in your `inventory_manager.py` file as mentioned in the previous step.

### Usage Guide

1. Navigate to the project directory using your terminal.
2. Run the application using the following command:
    ```bash
    python main.py
    ```

This will launch the Inventory Management System. Follow the on-screen prompts to interact with the different functionalities.
- **Admin Mode**: Access this mode to perform tasks that require higher privileges, such as generating reports.

### Future Improvements

- **Report Format**: Transition from .txt to .pdf or Excel format for more professional reporting.
- **GUI Enhancement**: Improve the terminal-based GUI for a more user-friendly experience.
- **Cloud Database Integration**: Option to use a cloud-based SQL server for remote access.
- **Data Backup**: Allow data backup and restore functionalities.
- **Search Filters**: Expand search functionality with advanced filters.

### Contributing Guidelines

We welcome contributions to improve this project. Feel free to fork the repository, make changes, and submit a pull request. Before contributing, please make sure to review the code style and formatting guidelines (if any).

### Resources

Throughout the development of this project, the following resources were instrumental:

- [**Python Documentation**](https://docs.python.org/)
- [**MySQL Documentation**](https://dev.mysql.com/doc/)
- [**phpMyAdmin Documentation**](https://docs.phpmyadmin.net/)
- [**Stack Overflow**](https://stackoverflow.com/) - For troubleshooting and community support.
- [**Real Python**](https://realpython.com/) - For Python tutorials and guides.
- [**W3Schools**](https://www.w3schools.com/) - For reading SQL and Python basics.
- [**GeeksforGeeks**](https://www.geeksforgeeks.org/) - For reference examples.
- [**CampusX**](https://youtube.com/@campusx-official?si=lTNShk8fkgogoTWS) - For learning Python basics.
- [**NetworkChuck**](https://youtube.com/@networkchuck?si=YbPcdIdeAXq86Roh) - For learning SQL basics.

### Feedback

If you have any feedback, please reach out to me at:

[Youtube](https://youtube.com/@cleongaming?si=Vi5hFyAE5R2iseb)

### License Information

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

We hope this Inventory Management System helps you organize your inventory effectively!
