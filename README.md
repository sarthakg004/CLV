# Customer Lifetime Value Prediction for Auto-Insurance Companies

## Business Problem
An Auto Insurance company X in the USA is facing issues in retaining its customers and wants to advertise promotional offers for its loyal customers. They are considering Customer Lifetime Value CLV as a parameter for this purpose. <br>
Customer Lifetime Value (CLV) signifies the worth of a customer to a company across a specified duration.  In the insurance sector, where competition is intense, customers consider more than just insurance premiums when making decisions.  Customer Lifetime Value (CLV), being centered on the customer, offers a strong foundation for retaining high-value clients, earning more from lower-valued clients, and improving overall customer satisfaction. Effectively leveraging CLV can result in better customer acquisition and retention, decreased churn rates, informed marketing budget planning, detailed ad performance measurement, and numerous other advantages.

## Dataset Description
The dataset represents Customer lifetime value of an Auto Insurance industry in the United States, it includes over 24 features and 9134 records to analyze the lifetime value of Customer.

Customer: Unique identifier for the customer.

State: State of residence.

Customer Lifetime Value: The lifetime value of the customer.

Response: Response to marketing offers (Yes/No).

Coverage: Type of coverage (Basic/Extended/Premium).

Education: Level of education.

Effective To Date: Date when the policy is effective.

Employment Status: Employment status of the customer.

Gender: Gender of the customer.

Income: Annual income of the customer.

Location Code: Location code (Urban/Suburban/Rural).

Marital Status: Marital status of the customer.

Monthly Premium Auto: Monthly premium for the auto insurance.

Months Since Last Claim: Months since the customer last filed a claim.

Months Since Policy Inception: Months since the policy started.

Number of Open Complaints: Number of open complaints.

Number of Policies: Number of policies the customer holds.

Policy Type: Type of policy (Corporate/Personal Auto).

Policy: Specific policy type (e.g., Corporate L3, Personal L3).

Renew Offer Type: Type of renewal offer.

Sales Channel: Sales channel through which the policy was sold (e.g., Agent, Call Center).

Total Claim Amount: Total amount of claims.

Vehicle Class: Class of the vehicle (e.g., Two-Door Car, SUV).

Vehicle Size: Size of the vehicle (e.g., Medsize).

We have the data of insurers from 5 states in North America — Washington, California, Arizona, Nevada, and Oregon. The data consists of 8 continuous variables and 15 categorical variables which are one-hot encoded for applying ML models. Among the variables, Customer (unique identifier) and Effective To Date are discarded as they are irrelevant to our analysis

## What is CLV?
Customer lifetime value (CLV) is a business metric used to determine the amount of money customers will spend on your products or service over time.

**CLV = average order value × number of transactions × average length of the customer relationship (in years)**

For example, if someone is loyal to an auto brand whose vehicles average at $30,000 and the customer buys three cars from them in their lifetime, their CLV is $90,000. Whereas, someone who visits their local coffee chain five days a week and spends $4 on a coffee, will have a CLV of $10,400 over the course of 10 years.

## Project Goal

To address customer retention challenges faced by a US auto insurance company X by leveraging Customer Lifetime Value (CLV) prediction and analysis.

This project is divided into three major parts. They are —

1. **CLV Prediction with ML**: Analyzed the different variables that contribute to the value of a customer and paved the way to modeling a machine learning model that predicts the Customer Lifetime Value for new clients based on their unique characteristics.
   
   ![WEB APP](https://github.com/sarthakg004/CLV/blob/master/web_app/prediction_page.png)
   
2. **User Interface and Dashboard**: Developed and hosted a website where the company can easily find the CLV for an incoming client based on the model. Also, designed a dashboard that gives a glimpse of the current state of insurance clients for a bigger picture.
   
   ![DASHBOARD](https://github.com/sarthakg004/CLV/blob/master/Dashboard/Screenshot%202024-06-01%20001510.png)

3. **Large Language Model-based Q&A platform**: Implemented a ’Q&A’ interface using Google’s Gemini LLM that converts human questions to SQL queries and retrieves data from the MySQL database.

 ![CHATBOT](https://github.com/sarthakg004/CLV/blob/master/LLM_QA/chatbot_app.png)


- Data Source: [IBM Watson Marketing Customer Value Data](https://www.kaggle.com/datasets/pankajjsh06/ibm-watson-marketing-customer-value-data)
