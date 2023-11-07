KAMBAN BOARD
 
Video Demo: https://www.youtube.com/watch?v=cly9z34XhtE

Description: A kanban board is an agile project management tool designed to help visualize work, limit work-in-progress, and maximize efficiency (or flow).
Used for tracking tasks, can have multiple lists,each list will have system will automatically capture the card created datetime and also card last updated datetime system will also automatically capture task completed datetime.
The system will track progress over time and shows graphs trend lines etc. 

This is can be used remember and schedule tasks.
Also there is a visual indication that tells if the deadline has passed or not.

It can help both agile and DevOps teams establish order in their daily work. Kanban boards use cards, columns, and continuous improvement to help technology and service teams commit to the right amount of work, and get it done!
kanban boards can be broken down into five components: Visual signals, columns, work-in-progress limits, a commitment point, and a delivery point.

Visual Signals — One of the first things you’ll notice about a kanban board are the visual cards (stickies, tickets, or otherwise). Kanban teams write all of their projects and work items onto cards, usually one per card. For agile teams, each card could encapsulate one user story. Once on the board, these visual signals help teammates and stakeholders quickly understand what the team is working on.

Columns — Another hallmark of the kanban board are the columns. Each column represents a specific activity that together compose a “workflow”. Cards flow through the workflow until completion. Workflows can be as simple as “To Do,” “In Progress,” “Complete,” or much more complex.

Work In Progress (WIP) Limits — WIP limits are the maximum number of cards that can be in one column at any given time. A column with a WIP limit of three cannot have more than three cards in it. When the column is “maxed-out” the team needs to swarm on those cards and move them forward before new cards can move into that stage of the workflow. These WIP limits are critical for exposing bottlenecks in the workflow and maximizing flow. WIP limits give you an early warning sign that you committed to too much work.

Commitment point — Kanban teams often have a backlog for their board. This is where customers and teammates put ideas for projects that the team can pick up when they are ready. The commitment point is the moment when an idea is picked up by the team and work starts on the project.

Delivery point — The delivery point is the end of a kanban team’s workflow. For most teams, the delivery point is when the product or service is in the hands of the customer. The team’s goal is to take cards from the commitment point to the delivery point as fast as possible. The elapsed time between the two is the called Lead Time. Kanban teams are continuously improving to decrease their lead time as much as possible


TODO

- Flask for application code
- Jinja2 templates + Bootstrap for HTML generation and styling
- SQLite for data storage
- All demos should be possible on a standalone platform like replit.com and should not require setting up new servers for database and frontend management


- Used for tracking tasks
- User can have multiple lists
- Each list will have
  - ID
  - Name
- User can add one or more cards to a list. Each card will have
  - Title
  - Content
  - Deadline
  - Completed flag
  - List it belongs to
- System will automatically capture the card created datetime and also card last updated datetime
- System will also automatically capture task completed datetime
- System will track progress over time and shows graphs trend lines etc. as Summary

Terminology

- Board - Kanban board
- List - List of tasks
- Card - Each card is represented as a card
- Movement - Card can be moved from one list to another list
- Summary - Shows how the user is performing across lists based on the completed flag, time when it completed, it also shows graphs


Core Functionality

- This will be graded 
- Base requirements:
  - User login
  - Main Board with Lists
  - List management
  - Card management
  - Summary page

Core - User Login
Form for username and password

- ` `You can either use a proper login framework, or just use a field for username - we are not concerned with how secure the login or the app is
- ` `Suitable model for user

Core - Board

- Board view with lists
- Ability to add or manage a list
- Ability to add or manage a card
- Ability to move cards between tasks/lists
- Ability to identify the completed tasks visually

Core - List management

- Create a new list
- Storage should handle multiple languages - usually UTF-8 encoding is sufficient for this
- Edit a list
  - Change title
- View List on Board
- Remove a list
  - Move the cards to a different list or delete the cards too with a confirmation from the user

Core - Card management

- Create/Add a card to a list
- Edit: Change title or content
- Edit: Mark as complete
- Edit: Move the card from one list to another
- Remove/Delete a card

Styling and Aesthetics

Proper login system











