# **Barbell Temple**

The purpose of this website is to highlight Barbell Temple, which is a dedicated gym that offers fitness classes tailored for beginners, intermediates, and advanced athletes, focusing on enhancing physical shape and fitness. Guided by seasoned and experienced trainers, these classes provide structured and effective workouts for all fitness levels. The gym’s website features an accessible timetable displaying available classes, their schedules, and remaining spots, facilitating easy enrolment. Each class has a detailed view explaining the class content and target fitness level. After enrolling, users can conveniently track their class schedule in the "My Barbell Classes" section, ensuring a seamless fitness journey.

[Barbell Temple Live Link](https://p4-barbell-temple-06315097a7c8.herokuapp.com/)

![Responsive Mockup](https://github.com/JoelChan13/barbell-temple/blob/main/media/barbelltemplehomepage.jpg)

This application was built using [GitHub](https://github.com/) and deployed to [Heroku](https://id.heroku.com/login).

<u>Required technologies:</u>

Python (+Django Framework), JavaScript, HTML5 and CSS3.

## **Table of content**

* [UX](#ux)
    * [Project Scope](#project-scope)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Website Structure](#website-structure)
    * [Relational Database Used](#relational-database-diagram)
    * [Design Choices](#design-choices)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [CRUD Operations](#crud-operations)
    * [Defense Design](#defense-design)
    * [Features Left to Implement](#features-left-to-implement)
* [Data Validation](#data-validation)
* [Technologies and libraries used](#technologies-and-libraries-used)
    * [Languages](#languages)
    * [Database Platform and Cloud Storage](#database-platform-and-cloud-storage)
    * [Libraries and other resources](#libraries-and-other-resources)
* [Testing](#testing)
    * [Introduction](#introduction)
    * [Testing User Stories](#testing-user-stories)
    * [Automated Testing](#automated-testing)
    * [Testing Accessibility and Performance](#testing-accessibility-and-performance)
    * [Code Validation](#code-validation)
* [Bugs during development](#bugs-during-development)
    * [Fixed Bugs and Solutions](#fixed-bugs-and-solutions)
    * [Ongoing Bugs](#ongoing-bugs)
* [Development and Deployment](#development-and-deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
* [Credits](#credits)
    * [Code](#code)

# **UX** 

## **Project Scope**

* **Functionality**

    * To be able to sign-up using an email address and secure password
    * To be able to login and logout of an account
    * To be able to create/view/edit/delete an event as site admin
    * To be able to upcoming barbell classes
    * To be able to view past barbell classes
    * To be able to enrol/unenrol from classes.
    * To be able to access a schedule of when classes are going to be held and access the selected class.
    * To be able to create/view/edit/delete user profile information as a user
    * To be able to change profile data as user, staff and superuser
    * To be able to access own data without other users being able to modify it unless they are staff or superusers
    * To be able to change own class details, without other staff members and users being able to do so.
    * To deny access to users to access admin page, unless they are staff or superusers.

* **Content Requirements**

    * Barbell Classes with clear information and details for users & staff
    * Use of forms for user input is required
    * Clear headings and information to guide users throughout website
    * Responsive and interactive website that responds to user
    * Images to provide visually appealing content

## **Strategy**

* **Site-owner goal** 

    * To provide a platform for athletes who are looking to engage in physical activity
    * To provide a platform users with differnt options to work out
    * To create a product that can be further developed with additional features to create a fitness community

* **User goals**

    * To access a user-friendly application across multiple devices
    * To discover new ways of maintaining an optimal fitness level or enhance their athletic performance

## **User Stories**


* As an **admin**, I can **access an admin profile** so that I can **create, edit and delete barbell classes with all relative information for website.**

* As an **admin**, I can **view user profiles** so that I can **modify or delete the selected user accordingly.**

* As a **first-time site visitor**, I can **view a landing page** so that I can **get relevant information about the website's purpose.**

* As a **first-time site visitor**, I can **Register/Sign-Up** so that I can **create an account to access user features.**

* As a **first-time site visitor**, I can **find the navigation bar** so that I can **navigate the website.**

* As a **first-time site visitor**, I can **view a scheduled timetable** so that I can **know when classes are held.**

* As a **first-time site visitor**, I can **view a detailed view of the barbell classes** so that I can **know what to expect from the classes and if any spots are available.**

* As a **user**, I can **sign-in and out of an account** so that I can **log-in and out of user account.**

* As a **user**, I can **view past events** so that I can **learn about previous barbell classes.**

* As a **user**, I can **view new events** so that I can **learn about forthcoming barbell classes.**

* As a **user**, I can **enrol to a barbell class** so that I can **participate in forthcoming events.**

* As a **user**, I can **view my enrolled barbell classes** so that I can **be sure to which classes I have enrolled for.**

* As a **user**, I can **get to my profile page** so that I can **see my account profile and change details if required.**


# **Design**

## **Website Structure**

* The website is structured into 10 principal pages
* All pages extend the same base therefore producing a consistent style across the application
* Pages are the following:

| Page | Description |
| --- | --- |
| **Header** | Navbar header with site logo and Login and Register links with collapsable link for media query sizes |
| **Home** | A landing page consisting of a welcome and upcoming barbell classes |
| **Timetable** | Displays all the barbell classes in a calendar, with easy access to the detailed barbell class page |
| **My Barbell Classes** | Displays the enrolled classes for a particular user when logged in |
| **New Class** | Provides a for to staff user, or super user, when logged in to create a new barbell classes   |
| **Login** | Where users can login with an account |
| **Logout** | Where users logout of an account |
| **Profile Page** | A profile dashboard displaying user information & provides ability to change details |
| **Barbell Classes** | Provides users with a brief detailed description of the particular class with the ability to enrol/unenrol, or update/delete, according to the user status accessing the page |
| **Footer** | Displays contact details |

* **Interactive Design**

    * Collapsable navbar menu for smaller media query screens

    ![responsive-toggle-example](https://github.com/JoelChan13/barbell-temple/blob/main/media/barbelltemplecollapsable.jpg)

    * Pop up modals with warnings and messages across site
    
    ![responsive-modal-example](https://github.com/JoelChan13/barbell-temple/blob/main/media/barbelltempleemptyfield.jpg)

## **Relational Database Diagram**

* The project uses a relational database (sqlite3)

**Models**

* **BarbellClass**
    * The BarbellClass model represents a barbell class with various attributes detailing the class information:
        * title: A string field for the class title, with a maximum length of 100 characters.
        * image: A Cloudinary field to handle image uploads, defaulting to a placeholder if not provided.
        * date_posted: A datetime field automatically set to the current time when the class is created, not editable.
        * author: A foreign key linking to the User model, indicating the creator of the class.
        * class_datetime: A datetime field specifying when the class will occur, with the default set to the current time.
        * duration: A text field for the class duration description.
        * difficulty: A choice field allowing selection among 'Beginner', 'Intermediate', and 'Advanced' difficulty levels, defaulting to 'Beginner'.
        * description: A text field for a detailed description of the class.
        * available_spots: An integer field indicating the number of available spots for the class.

* **Enrollment**
    * The Enrollment model manages the enrollment of users in barbell classes:
        * user: A foreign key linking to the User model, representing the enrolling user.
        * barbell_class: A foreign key linking to the BarbellClass model, representing the class the user is enrolling in.
        * date_enrolled: A datetime field automatically set to the current time when the enrollment is created.

* **Profile**
    *  the Profile model extends the default Django User model to include a profile picture, with added functionality to ensure images are appropriately sized. This model is essential for maintaining additional user information within the Barbell Class application.
    * The Profile model represents a user's profile with a one-to-one relationship to the Django User model, providing additional attributes:
        * user: A one-to-one field linking to the User model, ensuring each user has one unique profile.
        * image: An image field for storing profile pictures, with a default image if none is uploaded, and specifying the upload directory as profile_pictures.
    
## **Design Choices**

* **Wireframes**
    * Skeleton structure for website was created by hand.

* **Background**
    * Background image for webpage was created using Microsoft Copilot Image Creator by providing information related to fitness inspired by greek mythology and fitness.

## **Colour Choices**

Due to the nature of the background image, the colour choices chosen were kept as minimalist as possible not to create a busy environment which may distract users from the purpose of the website.

# **Features**

## **Existing features**

* # Interactive and collapsable navbar:

    * At the top of the website, one can find a responsive nav bar.
    * Navbar becomes collapsable when accessed from mobile or tablets.
    * Once an user has logged in, the navbar will update user links specific to authenticated users.

* # Interactive design:

    * Buttons, links and icons respond to mouse hovering across the whole website.

* # Landing Page:

    * Landing page features a title with sub-heading and the list of the barbell classes.

* # Timetable Page:

    * The timetable page features a calendar which updates with every class posted.
    * the classes display on the date scheduled and have a link to them which directs you to the respective barbell class.
    * The date of the current day has a feint yellow tint and the date is set in a bolder text to make it slightly more distinguishable, without distracting the user experience.

* # Sign Up Page:

    * The sign-up page features a form prompting the prospective user to enter a unique username and password along with their email, according to specified criteria.
    * Once Registration is completed, the page redirects users to login page 
    * Users cannot sign up with a username already in use.
    * Prompts are displayed when incorrect or missing data is entered.

* # Login Page:

    * The login page features a form prompting the user for their username and password.
    * Once logged in, users are redirected to the user profile.
    * If user enters incorrect credentials, user is not logged in and a prompt is displayed.

* # Logout Page:

    * User is signed out of the account and greeted with a message along with a link to log in again.

* # Barbell Class Detail Page:

    * Presents a class image related to the class being held.
    * Provided details for users to get an idea of what to expect.
    * Provides the number of spots available and updates the number of spots available every time a user enrols or unenrols.
    * Features an enrol or unenrol button for users, and an update or delete button for the author of the class.

* # Update Class:

    * Staff User can access update section if he or she is the author of the class.
    * Details can be changed according to what the author of the class, or the superuser, deems fit.
    * A prompt is presented when clicking the update button, providing a choice to confirm the change or cancel it.


## **CRUD Operations**

| **Operations** | All users | Auth. Users | Superusers |
| --- | --- | --- | --- |
| **View Home Page** | Yes | Yes | Yes |
| **View Barbell Classes** | Yes | Yes | Yes |
| **View Event Details** | Yes | Yes | Yes |
| **View User Details** | Yes | Yes | Yes |
| **Author Can Add/Edit/Delete Own Barbell Classes** | No | Yes | Yes |
| **Register/Deregister To Barbell Classes** | Yes | Yes | Yes |
| **Add/Edit/Delete To Barbell Classes** | No | No | Yes |
| **Add/Edit/Delete Profile** | No | Yes | Yes |
| **Login** | No | Yes | Yes |
| **Register** | Yes | No | No |

## **Defense Design**

* Delete & Update operations

    * Delete & Update Buttons summon a modal:

        * Which asks the user if they are sure to delete or update their class or enrolment respectively.
        * Which also gives them the option to return back.

    ![changes-modal](https://github.com/JoelChan13/barbell-temple/blob/main/media/modalchanges.jpg)

    ![enrolment-modal](https://github.com/JoelChan13/barbell-temple/blob/main/media/modalenrolment.jpg)

* Class Updates & Deletion

        * Barbell Class updates and/or deletion can only be made by authenticated authors or superuser.
        * Staff Users who are not the authors of the Barbell Class cannot update or delete Barbell Class.
        * Users who enrol for a particular class cannot unenrol other users' enrolled classes unless they are Staff Users or superusers. 
    
    * User Event Registration

        * Authenticated users can register and deregister to an event.
        * Registered users appear in the admin panel.
        * Admin has total control over who can attend an event.

## **Features left to implement**

* Payment system so that users can pay for barbell classes in advance.
* Ability to allow different users to privately message each other.
* Complete automated testing to 100%.
* Password Reset interface which sends an e-mail to user to change password.
* User Reviews.

# **Data Validation**

* **User Registration**

    * User cannot sign up with username which is already in use.
    * Content Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    * Password can’t be too similar to other personal information.
    * Password must contain at least 8 characters.
    * Password can’t be a commonly used password.
    * Password can’t be entirely numeric.
    * Same password must be entered when confirming password.

* **Barbell Class Creation**

    * Fields cannot be left empty.
    * Date and time of the class must be entered in the format yyyy/mm/dd hours:minutes.
    * Class description cannot be left empty.

* **Sign In Page**

    * System does not accept any username or password that is non-existent or incorrect.

# **Technologies and libraries used**

## **Languages**

The languages used are:

* [HTML](https://html.spec.whatwg.org/multipage/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

## **Database Platform, Cloud Storage & Frameworks**

* [SQLite](https://www.sqlite.org/index.html): SQL database engine used by default as part of Django Framework and used during development.
* [Cloudinary](https://cloudinary.com/home-102622): to store images and static files.
* [Heroku](https://id.heroku.com/login): to deploy and run the application.
* [Bootstrap](https://getbootstrap.com/): to aid with the website design and formulation.

## **Libraries and other resources**

This project contains the following resources:

* [Django](https://www.djangoproject.com/): Python-based framework for rapid website development. 
* [Bootstrap](https://getbootstrap.com/): CSS and JavaScript library. 
* [HTML Markup Validation](https://validator.w3.org/): used to validate HTML code syntax.
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/): used to validate CSS code syntax.
* [Python Checker](https://www.pythonchecker.com/): used to validate Python code syntax.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/): development tool supplied by Google Chrome browser to test responsive design during development.
* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): used to access website performance.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): used for comment and sign-in forms throughout website.
* [Favicon.io](https://favicon.io/): used for favicon.
* [GitHub](https://github.com/): used to store, develop and maintain project code.
* [GitPod](https://gitpod.io/) used to store, develop and maintain project code.
* [FullCalendar](https://fullcalendar.io/): to formulate a calendar.

# **Testing**

## **Introduction**

* Site has been continuously tested throughout development stages using the following features:
    * Python terminal for backend functionalities
    * Google Developer Tools 
    * Manual Testing

## **Testing User Stories**
* # Website navigation:

    * **First-Time Visitor User Stories**

        * As a **first-time site visitor**, I can **view a landing page** so that I can **get information about the website's purpose.**

        * As a **first-time site visitor**, I can **sign-up** so that I can **create an account to access user features.**

        * As a **first-time site visitor**, I can **find the navigation bar** so that I can **navigate the website.**

        * As a **first-time site visitor**, I can **view barbell classes** so that I can **get information regarding the barbell classes.**

        * As a **first-time site visitor**, I can **view the timetable schedule** so that I can **know when the barbell classes were held and are going to be held.**

    * **Admin User Stories**

        * As an **admin**, I can **access an admin profile** so that I can **create, edit and delete barbell-classes with all relative information for website.**

        * As an **admin**, I can **view user profile information** so that I can **modify any particular user detail or delete users.**

        * As an **admin**, I can **create staff users** so that I can **have multiple users creating barbell classes and users.**

        * As a **first-time site visitor**, I can **find the navigation bar** so that I can **navigate the website.**

        * As a **first-time site visitor**, I can **view barbell classes** so that I can **get information regarding the barbell classes.**

        * As an **admin**, I can **create a barbell classes** so that I can **create new barbell classes for users.**

    * **User Stories**

        * As a **user**, I can **sign-in and out of an account** so that I can **log-in and out of user account.**

        * As a **user**, I can **view barbell classes** so that I can **know when the past and next barbell classes have been held or are due to be held.**

        * As a **user**, I can **view date and details of a barbell class** so that I can **get relevant information about the barbell class.**

        * As a **user**, I can **view confirmation of my action** so that I can **be sure it has processed.**

        * As a **user**, I can **access my profile page** so that I can **see my account profile and edit my details.**

        * As a **user**, I can **enrol for a barbellclass** so that I can **participate in forthcoming barbellclasses.**

        * As a **logged in staff user**, I can **edit my barbell classes** so that I can **modify my barbell class.**


## **Testing Accessibility and Performance**

* Testing for accessibility and performance is managed using the Lighthouse tool in Chrome extension and was done for both Desktop and Mobile, obtaining satisfactory results.

    * For Desktop:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Home | 99 | 92 | 83 | 90 |
    | Timetable | 93 | 93 | 83 | 90 |
    | My Barbell Classes | 97 | 90 | 96 | 80 |
    | New Class | 99 | 100 | 96 | 89 |
    | Login | 100 | 100 | 96 | 89 |
    | User Profile | 99 | 83 | 96 | 80 |
    | Logout | 100 | 100 | 96 | 89 |
    | Register | 100 | 100 | 96 | 89 |
    | Class | 99 | 93 | 74 | 90 |

    * For Mobile devices:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Home | 97 | 100 | 96 | 87 |
    | Timetable | 90 | 95 | 96 | 78 |
    | My Barbell Classes | 97 | 93 | 96 | 80 |
    | New Class | 97 | 100 | 96 | 91 |
    | Login | 97 | 100 | 96 | 91 |
    | User Profile | 96 | 92 | 96 | 83 |
    | Logout | 96 | 100 | 96 | 91 |
    | Register | 97 | 100 | 96 | 91 |
    | Class | 99 | 93 | 74 | 90 |

## **Code Validation**

* **W3C HTML Code Validator**

    * Each page of the deployed website was run through the [HTML Markup Validation Service](https://validator.w3.org/) and returned no errors.

* **W3C CSS Jigsaw Validator**

    * CSS code was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors.

    [HTML Markup Validation Service](https://validator.w3.org/)

* **JSHint validator**

    * The custom JavaScript code was tested with [W3C CSS Validator](https://jshint.com/) via direct input and returned no errors. The remaining JavaScript written for this project was included with Bootstrap4. 

* **Python Validator**

    * Since [PEP8 Online Service](http://pep8online.com/) has been down, [Python Checker](https://www.pythonchecker.com/) was used to validate Python, with minor errors shown related to the format of the website. 

# **Bugs during development**
## **Ongoing bugs:**

*  Uncaught SyntaxError: Cannot use import statement outside a module (at main.js:6:1) caused by the imported code from FullCalendar.
* Missing favicon.ico showing in development, however not in deployed version due to it being imported in the code from FullCalendar template.

# **Development and deployment**

The development environment used for this project was initially CodeInstitute's IDE, however due to CodeInstitute migrating to a different service, GitPod was later used to compile the project. Commits and pushes to Github were performed on a regular basis to to be able to track and trace the development process of the website. The Gitpod environment for this particular project was created using a template provided by Code Institute. The project was eventually deployed to Heroku in order to make use of its optimal database maintenance capabilities.

# **Credits**

## **Code**

The following websites proved to be both insightful and helpful during development of this project:

* [W3School](https://www.w3schools.com/)
* [YouTube](https://www.youtube.com/)
* [Code Institute](https://learn.codeinstitute.net/) Boilerplate HTML Structure Code was taken from the ci-full-template found in CI GitHub