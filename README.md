# Customer Lifetime Value Prediction for Auto-Insurance Companies

## Business Problem
An Auto Insurance company X in the USA is facing issues in retaining its customers and wants to advertise promotional offers for its loyal customers. They are considering Customer Lifetime Value CLV as a parameter for this purpose. <br>
Customer Lifetime Value (CLV) signifies the worth of a customer to a company across a specified duration.  In the insurance sector, where competition is intense, customers consider more than just insurance premiums when making decisions.  Customer Lifetime Value (CLV), being centered on the customer, offers a strong foundation for retaining high-value clients, earning more from lower-valued clients, and improving overall customer satisfaction. Effectively leveraging CLV can result in better customer acquisition and retention, decreased churn rates, informed marketing budget planning, detailed ad performance measurement, and numerous other advantages.

## Dataset Description
The dataset represents Customer lifetime value of an Auto Insurance industry in the United States, it includes over 24 features and 9134 records to analyze the lifetime value of Customer.

Customer: Unique identifier for each customer.
State: The state where the customer resides.
Customer Lifetime Value: A measure of the total value a customer is expected to bring over their lifetime.
Response: Whether the customer responded to a marketing offer (Yes/No).
Coverage: Type of insurance coverage (e.g., Basic, Extended, Premium).
Education: Level of education of the customer.
Effective To Date: The date the policy is effective until.
EmploymentStatus: Employment status of the customer.
Gender: Gender of the customer.
Income: Annual income of the customer.
Location Code: Code representing the location of the customer (e.g., Urban, Suburban, Rural).
Marital Status: Marital status of the customer.
Monthly Premium Auto: Monthly premium amount for auto insurance.
Months Since Last Claim: Number of months since the customer last filed a claim.
Months Since Policy Inception: Number of months since the policy was first started.
Number of Open Complaints: Number of open complaints the customer has.
Number of Policies: Number of policies the customer holds.
Policy Type: Type of policy the customer has (e.g., Corporate Auto, Personal Auto).
Policy: Specific policy the customer has.
Renew Offer Type: Type of offer used to renew the policy.
Sales Channel: Channel through which the policy was sold (e.g., Agent, Call Center).
Total Claim Amount: Total amount of claims made by the customer.
Vehicle Class: Class of vehicle the customer owns (e.g., Two-Door Car, SUV).
Vehicle Size: Size of the vehicle (e.g., Medsize, Small).

We have the data of insurers from 5 states in North America — Washington, California, Arizona, Nevada, and Oregon. The data consists of 8 continuous variables and 15 categorical variables which are one-hot encoded for applying ML models. Among the variables, Customer (unique identifier) and Effective To Date are discarded as they are irrelevant to our analysis

- Data Source: [IBM Watson Marketing Customer Value Data](https://www.kaggle.com/datasets/pankajjsh06/ibm-watson-marketing-customer-value-data)
