**User Story 1: As a user, I want to input data so that the application can react to the input by executing specified jobs based on rules.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "new_order",
    "order_id": 123,
    "total_amount": 100
  }
  ```
- **Rule**: If `event` is "new_order" and `total_amount` is greater than 50, execute jobs: "Save to Database", "Send Email"

**User Story 2: As a user, I want to define rules containing instructions for executing jobs based on specific conditions.**

*Example*: 
- **Rule Definition**: 
  ```json
  {
    "event": "new_user",
    "conditions": {
      "user_type": "premium"
    },
    "jobs": ["Save to Database", "Send Welcome Email"]
  }
  ```

**User Story 3: As a user, I want to save data into a database when certain conditions are met.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "new_user",
    "user_id": 456,
    "user_type": "premium"
  }
  ```
- **Rule**: If `event` is "new_user" and `user_type` is "premium", execute job: "Save to Database"

**User Story 4: As a user, I want to send emails based on specific events and conditions.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "order_shipped",
    "order_id": 789,
    "customer_email": "customer@example.com"
  }
  ```
- **Rule**: If `event` is "order_shipped", execute job: "Send Email"

**User Story 5: As a user, I want to update data in a database when certain conditions are met.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "order_delivered",
    "order_id": 101,
    "status": "delivered"
  }
  ```
- **Rule**: If `event` is "order_delivered" and `status` is "delivered", execute job: "Update Database"

**User Story 6: As a user, I want to send events to other systems when specific events occur.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "new_comment",
    "comment_id": 567,
    "user_id": 789
  }
  ```
- **Rule**: If `event` is "new_comment", execute job: "Send Event to Other System"

**User Story 7: As a user, I want to call external APIs based on certain events and conditions.**

*Example*: 
- **User Input**: 
  ```json
  {
    "event": "payment_failed",
    "order_id": 123,
    "payment_status": "failed"
  }
  ```
- **Rule**: If `event` is "payment_failed", execute job: "Call API"

Submission Guidelines:
	
	> Begin by creating an empty GitHub repository to house your project.
	> Make your GitHub repository public to enable us to review your code.
	> Bootstrap your project with the chosen framework, database, and programming language (Python or NodeJS).
	> Initiate your project's structure and commit to the initial setup.
	> Commit regularly to meaningful messages after completing every individual API.
	> Craft clear instructions on how to run your program using the README.md file.
	> Develop a script that seeds initial test data into your chosen database.
	> Submit the Github repository public link after completion.

Please Note: You are free to choose any framework, database, and either Python or NodeJS as your programming language for this assignment.

Aspects We Value:
	
	> Demonstrate adherence to best coding practices, ensuring clean, organized, and maintainable code.
	> Employ thoughtful code comments that enhance code understanding and maintainability.
	> Showcase your ability to design an effective and efficient database structure.
	> Implement APIs following industry-standard practices for consistency and usability.

Your submission will be evaluated based on these important aspects, so please ensure your work reflects your proficiency in these areas.