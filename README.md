# GoodGames
Welcome to the DRF API for GoodGames! 

GoodGames is a website where you can share the video games you're currently playing, and leave a review for each game. You can like other users' posts, reviews, and games, and leave comments on other users' "Currently Playing" posts. 

This is the backend API database, built with Django REST Framework. The deployed version of the API is HERE, and the deployed version of the full site built in React is HERE.

## Entity Relationship Diagram
In the planning stage of this project, I created this Entity Relationship Diagram (ERD) to better visualize the relationships between models in the database.
![ERD for GoodGames database](static/readme/PP5-ERD.png)

## User Stories
I have divided the functionality of the site and database into epics and user stories:

### **Epic:** Account Management

**User Stories:**
- As a **user** I can **sign up for an account** so that I can **make and like posts, and add games**
- As a **user** I can **log in and out of my account** so that I can **access the site from different devices and keep my account secure**
- As a **user** I can **add a profile photo and description** so that **I can personalise my profile**
- As a **user** I can **request to reset my password via email** so that **I can log back in to my account if I forget my login details**
- As a **user** I can **delete my profile** so that **my personal details are not saved if I don't want to use the site anymore**

### **Epic:** Managing Posts

**User Stories:**
- As a **user** I can **add a new post when I start playing a game**
- As a **user** I can **edit my posts if I need to make updates, or finish playing the game**
- As a **user** I can **delete my posts**
- As a **user** I can **like and unlike other users' posts**

### **Epic:** Managing Comments

**User Stories:**
- As a **user** I can **comment on other users' posts**
- As a **user** I can **edit comments I have made**
- As a **user** I can **delete comments I have made**

### **Epic:** Managing Games

**User Stories:**
- As a **user** I can **request to add a new game to the site's database**
- As a **user** I can **request edits to an existing game**
- As a **user** I can **request that a game be deleted from the database**
- As a **user** I can **add a review to a game**
- As a **user** I can **edit or delete my own reviews**
- As a **user** I can **like other users' reviews**

### **Epic:** Admin Capabilities

**User Stories:**
- As a **site admin** I can **add, edit, and delete games from the database**
- As a **site admin** I can **remove posts or comments if they are not appropriate or relevant**
- As a **site admin** I can **see lists of all user profiles, posts, games, reviews, likes, and comments**

## Testing 

### Manual Testing

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The default profile and default post images are from [Code Institute](https://codeinstitute.net/ie/)'s Django REST Framework walkthrough.

Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 