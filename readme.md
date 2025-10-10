<div align="center">
<img src="https://github.com/EhudSicron/pom-orders/blob/main/img/project_pom_orders.png" alt="Project Banner" width="700"/>
<h1>POM-Orders: Enterprise-Grade Test Automation</h1>
</div>

<div align="center">

</div>

🚀 Project Overview
The POM-Orders project is a robust, scalable, and highly maintainable test automation framework built to showcase best practices in software quality assurance. Leveraging the powerful Page Object Model (POM) design pattern, this framework ensures that test code is modular, reusable, and easy to maintain, even as the application under test evolves.

This repository serves as a professional-grade example of a complete end-to-end testing solution, from writing efficient tests with Playwright and TypeScript to generating comprehensive reports with Allure Report and integrating with a continuous integration pipeline using GitHub Actions. It provides a blueprint for building a resilient automation system capable of handling complex web applications.

🎯 Project Goals
Create a Robust and Maintainable Framework: Implement a resilient test automation framework using the Page Object Model (POM) to separate test logic from page actions, ensuring a clean and scalable codebase.

Enhance Code Readability and Reusability: Utilize TypeScript to provide static typing, improving code quality, readability, and the ability to detect issues early.

Generate Insightful Test Reports: Leverage Allure Report to produce interactive and detailed test reports, offering a clear visual representation of test results, including logs, steps, and screenshots for every execution.

Establish a CI/CD Pipeline: Integrate with GitHub Actions to automate the entire testing process, from code push to test execution and report deployment, guaranteeing continuous quality assurance.

🛠️ Technologies Used
This project is built with the following cutting-edge technologies:

Playwright: The core automation framework for end-to-end testing, known for its speed, stability, and ability to run tests across all modern browsers.

TypeScript: A statically-typed language that enhances code maintainability and developer experience.

Node.js: The runtime environment for executing the automation scripts.

Allure Report: An open-source, multi-language test reporting tool that provides beautiful and informative reports.

GitHub Actions: A powerful CI/CD platform for automating workflows directly within GitHub.

⚙️ How to Install and Run
To get this project running on your local machine, follow these steps:

Clone the repository:

git clone [https://github.com/EhudSicron/pom-orders.git](https://github.com/EhudSicron/pom-orders.git)

Navigate to the project directory:

cd pom-orders

Install project dependencies:

npm install

Run the test suite:

npx playwright test

This command executes the tests and generates the Allure Report data in the allure-results directory.

Generate and view the Allure Report:
To serve the report and open it in your browser, run:

npx allure serve allure-results

📁 Folder Structure
The project's directory structure is designed for clarity and best practices:

<ul>
  <li><strong>pom-orders-main/</strong>
    <ul>
      <li><strong>.github/</strong>
        <ul>
          <li><strong>workflows/</strong>
            <ul>
              <li>main_workflow.yml</li>
            </ul>
          </li>
        </ul>
      </li>
      <li><strong>allure-report/</strong></li>
      <li><strong>img/</strong></li>
      <li><strong>pages/</strong> </li>
      <li><strong>tests/</strong> <ul>
          <li><strong>cart/</strong></li>
          <li><strong>checkout/</strong></li>
          <li><strong>login/</strong></li>
          <li><strong>manu/</strong></li>
          <li><strong>product/</strong></li>
          <li><strong>sort/</strong></li>
          <li>basetest.py</li>
          <li>config.ini</li>
          <li>config.py</li>
          <li>conftest.py </li>
        </ul>
      </li>
      <li>readme.md </li>
      <li>Readme.txt</li>
      <li>requirements.txt </li>
    </ul>
  </li>
</ul>

🧪 What's Tested
The test suite provides comprehensive coverage of the core functionalities of the "Pom-Orders" application, including:

User Authentication: End-to-end validation of the login process with valid credentials.

Dashboard Navigation: Verifying access and correct display of the main application dashboard.

Order Management: Testing key features such as filtering, viewing, and interacting with orders.

UI Component Integrity: Ensuring that all on-screen elements are functional, styled correctly, and behave as expected.

📈 Reports & Continuous Integration
This project is integrated with GitHub Actions to provide an automated CI/CD pipeline. Each push to the main branch triggers a full test suite run, and the results are automatically published to a professional-looking Allure Report hosted on GitHub Pages.

Allure Report (Live): https://ehudsicron.github.io/pom-orders/

<br>
<div align="center">
<img src="https://github.com/EhudSicron/pom-orders/blob/main/img/allure_logo.png" alt="Allure Report Logo" width="50" height="50">
<br>
<h4>Allure Report Screenshot</h4>
<img src="https://github.com/EhudSicron/pom-orders/blob/main/img/Allure_report.PNG" alt="Allure Report Screenshot" width="700"/>
</div>

<h4> Video - Test flow add 2 products and remove </h4>


https://github.com/user-attachments/assets/62d78a19-9c65-480d-a646-7061d9b62600


⭐ Get Involved
If you're a fellow automation enthusiast or a company looking for a robust testing solution, this project is for you!

Star this repo to show your support and help others discover it.

Send me your feedback by opening an issue or reaching out directly.

Connect with me on LinkedIn: https://www.linkedin.com/in/ehud-sicron/


Learn more about automation: https://automation.co.il/










