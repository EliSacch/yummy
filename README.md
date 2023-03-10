# yummy
Recipe book 


![Responsive Mockup]()

[See deployed website]()

## Table of content

- [Design and User Experience](#design-and-user-experience)
  - [Design](#design)
  - [User Stories](#user-stories)
  - [Recipes database model](#recipes-model)
  - [Wireframes](#wireframes)

- [Features](#features)
  - [Landing Page](#landing-page)
  - [Dashboard](#dashboard)

- [Testing](#testing)
  - [Tests](#tests)
  - [Validator Testing](#validator-testing)
  - [Fixed bugs](#fixed-bugs)
  - [Unfixed bugs](#unfixed-bugs)
  - [Performance](#performance)

- [Deployment](#deployment)
  - [Live Website](#live-website)
  - [Local Deployment](#local-deployment)

- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)

- [Technologies used](#technologies-used)

- [Acknowledgements](#acknowledgements)

## Design and User Experience

### Design

- Color palette:
  - Gradient:

  ![gradient](media/design/gradient-palette.png)

  - Neutral:

  ![neutral](media/design/neutral.png)

  - Contrast:

  ![contrast](media/design/contrast.png)
  ![contrast](media/design/contrast-1.png)

### User Stories

- As website owner I want:

- As a user I want:


### Recipes model

The recipes table will contain the following columns:

![Database Model](media/design/recipe-model.png)

### Wireframes

<details>
  <summary>Mobile</summary>

   ![Mobile Wireframe](media/wireframes/mobile/landing-page.png)
   ![Mobile Wireframe](media/wireframes/mobile/signup.png)
   ![Mobile Wireframe](media/wireframes/mobile/login.png)
   ![Mobile Wireframe](media/wireframes/mobile/dashboard.png)
   ![Mobile Wireframe](media/wireframes/mobile/sidebar.png)
   ![Mobile Wireframe](media/wireframes/mobile/new-recipe.png)
   ![Mobile Wireframe](media/wireframes/mobile/recipe-page-overview.png)
   ![Mobile Wireframe](media/wireframes/mobile/recipe-page-full.png)
   ![Mobile Wireframe](media/wireframes/mobile/profile.png)

</details>


<details>
  <summary>Desktop</summary>

   ![Desktop Wireframe](media/wireframes/desktop/landing-page.png)
   ![Desktop Wireframe](media/wireframes/desktop/signup.png)
   ![Desktop Wireframe](media/wireframes/desktop/dashboard.png)
   ![Desktop Wireframe](media/wireframes/desktop/new-recipe.png)
   ![Desktop Wireframe](media/wireframes/desktop/recipe-page.png)
   ![Desktop Wireframe](media/wireframes/desktop/profile.png)

</details>


## Features 


### Landing page

- __Login__

- __Signup__


### Dashboard

- __Header__

- __Search__

- __Add recipe__



## Testing 


### Tests


### Validator Testing

#### HTML

 Check if errors are returned when passing the final version through the official [W3C validator](https://validator.w3.org/nu/#textarea)

  <details>

  <summary>W3 - HTML validation screenshot</summary>

  ![Image]()
  </details>


#### CSS

 Check if Errors are returned when passing the final version through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/validator)

  <details>

  <summary>W3 - CSS validation screenshot</summary>
  
  ![Image]()
  </details>


#### JavaScript

Check if Errors are returned when passing the final version through the official [JsHint validator](https://jshint.com/), but only 4 warnings.


<details>
  <summary>JsHint - JS validation screenshot</summary>

  ![Image]()

</details>


### Fixed Bugs

<details>
  <summary> Unable to load static files on Heroku:</summary>

  - Issue: The deployed app is not loading static files correctly, because it seems to add a Cloudinary file path in the middle.

![Coudinary Error](media/errors/cloudinary-error.png)

  - Fix: After troubleshooting I could see that the issue was caused by the __DISABLE_COLLECTSTATIC__ Config Var, which I had not removed yet. After removing this Config Var the page loads correctly.

</details>

    
<details>
  <summary>Error 500 when trying to reset password from Heroku</summary>

  - Issue: When trying to reset the password from the deployed website I received Server Error 500.

![SMTP Error](media/errors/reset-password-error.png)

  - Fix: After troubleshooting I could see that the issue was caused by the Outlook SMTP credentials, and the issue was related not only to the reset password link, but to all SMTP functionalities. I decided to switch to Gmail SMTP which solved the issue.

</details>


<details>
  <summary>Select Field not displaying options in form</summary>

  - Issue: When adding the select field to the 'Add recipes' form, the options where not showing and I could only see the label.

![Select Field Error](media/errors/options-field-not-displaying.png)

  - Fix: The issue was caused by the Materialize CSS form, which requires for the select fields to be initialized via JS.

![Select Field Fix](media/errors/options-field-not-displaying-fix.png)

</details>

<details>
  <summary>Index page broke after adding function to provide suggested recipes</summary>

  - Issue: To provide the recipes suggestion, the function was filtering the results based on the user ID, so that users can see only their recipes. When I first implemented this option I was logged in as admin. After logging out I received this error.

![Anonymous User Error](media/errors/anonymous-user-error.png)

  - Fix: The issue was caused by the Materialize CSS form, which requires for the select fields to be initialized via JS.

![Anonymous User Fix](media/errors/anonymous-user-fix.png)

</details>


<details>
  <summary>Randomize icons JS error</summary>

  - Issue: I have created a custom image placehoder to display when the user does not upload an image for the recipe. The functions creates random food icons and assign a random position.

  The function was working and displaying the icons in random positions, although it was giving an error in the console.

  ![Random icons console error](media/errors/random-icons-error.png)

  This is the original code:

  ![Random icons original code](media/errors/random-icons-error-code.png)

  - Fix: To fix this issue I changed the code as follow:

  ![Random icons final code](media/errors/random-icons-fix.png)


</details>


<details>
  <summary>Update form creates new instance instead of updating the existing one</summary>

  - Issue numer 1: After creating the UpdateView for my recipes, the view was showing the correct template and pre-populating the fields with the selected recipe to be updated.
  Although when clicking on "Save", the form was crating a new instance, instead of updating the existing one.

  After investigation I could determine that the issue was created by the action url in the form, that was pointing to the add_recipe ursl, instead of edit_recipe url:
    ![Original code](media/errors/update-view-form-original-code.png)

  - Fix: to solve this issue I changed the action url so that it could point to the correct url:
  ![Update form fix 1](media/errors/update-view-fix-1.png)


  - Issue numer 2: After changing this url although I received a second error, since the edit_url requires an argument (the primary key of the recipe):
    ![Missing argument error](media/errors/update-view-reverse-match-error.png)

  - Fix: To solve this issue I had to add 'pk' as argument for the link, and I had to pass the pk also in the context.

  ![Update form fix 2](media/errors/update-view-fix-2.png)
  ![Update form fix 3](media/errors/update-view-fix-3.png)





</details>


</details>


<details>
  <summary> </summary>


</details>


### Unfixed Bugs


### Performance


## Deployment

### Deployment on Heroku

### Local Deployment
  - For a local deployment follow these steps:
    - Create a new directory on your machine, where you want do deploy the files
    - Open the existing repository in GitHub
    - Go to the "Code" tab
    - Click on the "Code" button
    - Copy the HTTPS link
    - Open your terminal and run the command __git clone 'link'__
    - use the link just copied, without quotes, instead of 'link'


## Credits 

### Code

- The code to filter the recipes by tag in the admin page is taken from [bradmontgomery](https://bradmontgomery.net/blog/django-admin-filters-arrayfields/)

- The code to dynamically add ne forms is taken from [CodingEnterpreneur tutorial](https://www.youtube.com/watch?v=s3T-w2jhDHE&t=1293s)

### Content

- The color palette was generated using [Color Space](https://mycolor.space/)
- The recipe model was drawn using [Smart Draw](https://www.smartdraw.com/)

- The icons were taken from [Font Awesome](https://fontawesome.com/) and from [Google Fonts Icons](https://fonts.google.com/icons)

- The following fonts, used for the project, are from [Google Fonts](https://fonts.google.com/):
  - Quicksand
  - Source Sans Pro


The following Images are taken from [Unsplash](https://unsplash.com/photos/_h-2jrL9cMU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

- Background image is from [Mae Mu](https://unsplash.com/@picoftasty?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) 

- Card placeholder image is from [Marisol Benitez](https://unsplash.com/@marisolbenitez?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  
  

## Technologies used

  - HTML
  - CSS
  - JavaScript and JQuery
  - Python
  - Django
  - Materialize
  - PostgreSQL

  Django libraries
  - Allauth
  - inline forms
  

## Acknowledgements

A special thank to my mentor __Dick Vlaanderen__ for his precious feedback on this project.

Tutor Ed