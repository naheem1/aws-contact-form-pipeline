# AWS Serverless Contact Form Pipeline

## The Problem
A local electrician in Birmingham had a website but no contact form.
Customers had to copy his email address manually — most didn't bother and called a competitor instead.

## The Solution
Built a fully serverless contact form pipeline on AWS.
Customer fills in their name, email and message — the plumber gets notified instantly in his inbox.

## Architecture
Form → API Gateway → Lambda → SES → Email Inbox

## AWS Services Used
- **API Gateway** — receives the form submission via HTTP POST
- **Lambda** — processes the request and triggers the email
- **SES (Simple Email Service)** — sends the email to the business owner

## Cost
Runs on AWS free tier. For a real business doing 50 enquiries a month the cost would be less than £1/month.

## How It Works
1. Customer submits the contact form
2. API Gateway receives the POST request and triggers Lambda
3. Lambda extracts the name, email and message
4. SES sends an email to the business owner instantly

## Files
- `lambda_function.py` — the Lambda function code
- `index.html` — the front end contact form
