# Testing

Back to [main README](readme.md)

## Table of content

[Tests](#tests)
  - [Unit test](#unit-test)
  - [Manual test](#manual-test)

[Validator Testing](#validator-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [JS](#javascript)
  - [Python](#python)

[Fixed bugs](#fixed-bugs)

[Unfixed bugs](#unfixed-bugs)

[Performance](#performance)


## Tests

### Unit test

### Manual test

<details>
<summary>Home page before login</summary>

Landing page / signup:

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|
| Go to the web app link | The browser shows the home page before login, with the signup and ligin buttons | Pass |
| Click on the signup button | The user is redirected to the sign up form | Pass |
| Click on the button without any information filled out | A message prompts the user to enter the required information | Pass |
| Enter the email address only, and submit the form | A message prompts the user to fill out the username | Pass |
| Enter email and username and submit | A message prompts the user to enter the password | Pass |
| Enter email, username and password | A message prompts the user to re-enter the pssowrd | Pass |
| Enter all information, but type two different password | A message informs the user that the two passwords must match | Pass |
| Enter all information, but an inavlid username | A message informs the user that the username is invalid | Pass |
| Enter all information, but an invalid email | A essage informs the user that the email is not valid | Pass |
| Enter all valid information | The form submits and the user is informed that a verification email has been sent to their email address | Pass |
| Click on the 'Go home' button | The user is redirected to the landing page | Pass |
| Try to login before verifying the email | The user is redirected to a page that informs them to check their inbox for the verification email | Pass |
| Check emails received | An email with the verification link is received | Pass |
| Click on the verification link | A new page opens in the browser, asking the user to confirm the email address | Pass |
| Click on 'confirm' button | The user is redirected to the login page, and a message informs them that the email address has been verified | Pass |
| From the login page, click on the link that redirects to the signup page | The user is redirected to the signup page | Pass |
| From the signup page, click on the link that redirects to the login page | The user is redirected back to the login page | Pass |


Login:

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|
| Try to login without entering any information | The user is asked to enter the username | Pass |
| Enter the username but not the password | The user is asked to enter the password | Pass |
| Enter an incorrect password and submit | A message informs the user that the username and/or password are incorrect | Pass |
| Enter a correct password but an incorrect username | A message informs the user that the username and/or password are incorrect | Pass |
| Enter all valid information | The user is logged in and the dashboard is displayed | Pass |
| Find the logout button and click it | A pop up opens, asking the use to log out | Pass |
| Click on sign out | The user is logged out and the landing page is displayed | Pass |
| Click on the login button | The user is redirected to the login page | Pass |
| This time enter the email adddress instead of the username, and the password | The user is logged in correctly | Pass |

Reset password:

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|
| Log out again, open the login page and click on the 'Forgot password' link | The reset password page opens up | Pass |
| Do not enter any information and submit | A message asks the user to enter the email | Pass |
| Enter an invalid email address | The user is informed that the email address is invalid | Pass |
| Enter the correct email address and submit | The user is informed that an email has been sent with the link to reset their password | Pass |
| Click on the 'go home' button | The user is redirected to the landing page | Pass |
| Check the email inbox | The reset password email has been received | Pass |
| Click on the link | The 'change password' page is opened in the browser | Pass |
| Do not enter any information and submit | The user is informed that they need to fill out the form | Pass |
| Enter just the first password and submit | The user is informed that they need to eneter the password again | Pass |
| Fill out both fields, but with different passwords | The user is informed that the passwords don't match | Pass |
| Fill out the form correctly and submit | The user is redirected to a new page that informs them that the password has been updated | Pass |
| Duplicate the tab, so that we can check both buttons | | |
| Click on the 'log in' button | The user is redirected to the login page | Pass |
| Click on the 'go home' button | The user is redirected to the landing page | Pass |
| Try and log in with the new credentials | The user is logged in correctly | Pass |

</details>


<details>
<summary>Dashboard</summary>

Dashboard general:

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|
| Check the user handle on the top left corner | The username shows correctly | Pass |
| Check the middle section of the page | Because there are no recipes added, the page shows a messag informing the user to add a new recipe | Pass |
| Click on the 'Add recipe' link in the middle of the page | The user is redirected to the 'add recipe' page | Pass |
| Click on the 'go back' arrow on the top left corner, without submitting the form | The user is redirected to the dashboard, and the same msaage appears again, since no recipe has been added yet | Pass |
| Shrink and stretch the size of the window | The menu expands or collapses every time we pass the breakpoint | Pass |
| When the menu is collapsed, and we see the hamburger menu, click on the menu icon | The side menu opens | Pass |
| Click outside the menu | The side menu closes | Pass |


Navigation:

The following actions have been performed for both navigation bar (expanded navigation and side bar)

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|
| Click on the home link | The user is redirected to the home page | Pass |
| Click on the 'all recipes' link | The user is redirected to the 'my recipes' page | Pass |
| Click on the 'add recipe' link | The user is redirected to the 'add recipe' page | Pass |
| Click on the 'prfile' link (from the side bar), or on the user handle (from the expanded menu) | The user is redirected to the 'profie' page | Pass |
| Click on the 'logout' link | The 'logout' modal opens up | Pass |


</details>


<details>
<summary>Add recipe</summary>

Enter invalid information:

| Action | Expected result | Pass/Fail |
|--------|-----------------|-----------|


</details>


[Back to the top](#table-of-content)

## Validator Testing

### HTML

Check if errors are returned when passing the final version through the official [W3C validator](https://validator.w3.org/nu/#textarea)

<details>
<summary>Home page before login</summary>

![Image](media/testing/validator/html-index-before-login.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Sign up page</summary>

![Image](media/testing/validator/html-signup.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Login page</summary>

![Image](media/testing/validator/html-login.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Reset password</summary>

![Image](media/testing/validator/html-reset-password.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Dashboard after login</summary>

![Image](media/testing/validator/html-dashboard-after-login.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>My recipes page</summary>

![Image](media/testing/validator/html-all-recipes.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Recipe detail page</summary>

![Image](media/testing/validator/html-detail-page.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Add Recipe page</summary>

![Image](media/testing/validator/html-add-recipe.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Edit Recipe</summary>

![Image](media/testing/validator/html-edit-recipe.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Profile page</summary>

![Image](media/testing/validator/html-profile-page.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Manage email page</summary>

![Image](media/testing/validator/html-email-manager.png)
</details>

- Errors: 0
- Warnings: 0


<details>
<summary>Change password page</summary>

![Image](media/testing/validator/html-change-password.png)
</details>

- Errors: 0
- Warnings: 0


[Back to the top](#table-of-content)

### CSS

4 errors are returned when passing the final version through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/validator)

Although, these errors are caused by a new css property, that is still not widely supported.
  - 2 errors are related to the container-type property.
  - 2 errors are related to the cqw values.

<details>

<summary>W3 - CSS validation screenshot</summary>

![Image](media/testing/validator/css-w3c-result.png)
</details>

These errors can be ignored, for the following reasons:

The Container-type property is actually a valid property, according to W3.

[Check on W3](https://www.w3.org/TR/css-contain-3/#propdef-container-type)

  - Accepted value: 	normal || [ size | inline-size ]
  - Applies to: All elements

Even if not supported on some browser, it does not affect the rest of the style, and it will simply be ignored when not supported.

<details>

<summary>Check browser support</summary>

![Image](media/testing/validator/css-container-type-support.png)
</details>


This property is used, in this particular instance, to make this div a 'container', so that I can use the container-relative size for some chldren elements (cqw in this case)

[Check on W3](https://www.w3.org/TR/css-contain-3/#container-lengths)

This unit is become more an more supprted, although a fallback size was provided in both instances, so that I could reach a similar result also on unsuported browsers.

<details>

<summary>Check browser support</summary>

![Image](media/testing/validator/css-cqw-support.png)
</details>

[Back to the top](#table-of-content)

### JavaScript

No errors are returned when passing the final version through the official [JsHint validator](https://jshint.com/)

<details>
  <summary>JsHint - JS validation screenshot</summary>

  ![Image](media/testing/validator/js-jshint-result.png)

</details>

[Back to the top](#table-of-content)


### Python

The final version of python files was checked using [CI Python Linter](https://pep8ci.herokuapp.com/#)

Se scrrenshots below:

<details>
  <summary>Admin.py</summary>

  ![Image](media/testing/validator/py-admin.png)

</details>


<details>
  <summary>Apps.py</summary>

  ![Image](media/testing/validator/py-apps.png)

</details>


<details>
  <summary>Filters.py</summary>

  ![Image](media/testing/validator/py-filters.png)

</details>


<details>
  <summary>Forms.py</summary>

  ![Image](media/testing/validator/py-forms.png)

</details>


<details>
  <summary>Models.py</summary>

  ![Image](media/testing/validator/py-models.png)

</details>


<details>
  <summary>Urls.py</summary>

  ![Image](media/testing/validator/py-urls.png)

</details>


<details>
  <summary>Views.py</summary>

  ![Image](media/testing/validator/py-views.png)

</details>


[Back to the top](#table-of-content)

## Fixed Bugs

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


<details>
  <summary>Username Form disappears if invalid form</summary>

  - Issue: When updating the usename form the ProfileView, if the form was invalid, the error message was displaying correctly, but the form field disappeared completely.

  ![Error missing form](media/errors/invalid-username-form-disappears-error.png)

  - Fix: To fix this error, instead of returning "super().form_invalid(form)", I opted to redirect the user to the same page.
  The field reloads correctly, and an error message informs the user that the choosen username was invalid.

</details>


<details>
  <summary>Search results not clearing if there is no value in the searchbar</summary>

  - Issue: When looking for recipes by name, the results are shown dynamically uderneatch the search bar. After some results were found, if the user tried and deleted all the charachters in the search field, the search result div was still showing the last results found.
  This was caused by the fact that all the logic was contained in the 'if' statement, which is fired only if the search string is longer then a minChar value. When deleting charachters from the search bar, the length of the search string was falling below the minChar value, so the search results array was not cleared.

  ![Search results not clearing - error](media/errors/search-result-not-clearing-error.png)

  - Fix: To solve this issue I added an else statement, that hides the search results if the search string length is less then the minChar value.

  ![Search result not clearing - fix](media/errors/search-result-not-clearing-fix.png)

[Back to the top](#table-of-content)

</details>


<details>
  <summary>Server error 500 when signing up</summary>

  - Issue: when signing up for a new account, the server was unable to load the verification email template, due to a missing tag.

  - Fix: I added the missing tag "{% load i18n %}" and the issue was resolved.

  ![Updated code](media/errors/unable-to-send-verification-email-fix.png)

</details>

## Unfixed Bugs

There are currently 0 known unfixed bugs

[Back to the top](#table-of-content)

## Performance

The website performance were measured using the Chrome built in tool __Lighthouse__

<details>
<summary>Home page before login</summary>

![Image](media/testing/lighthouse/index-before-login.png)
</details>


<details>
<summary>Sign up page</summary>

![Image](media/testing/lighthouse/signup-page.png)
</details>


<details>
<summary>Log in page</summary>

![Image](media/testing/lighthouse/login-page.png)
</details>


<details>
<summary>Password reset page</summary>

![Image](media/testing/lighthouse/password-reset.png)
</details>


<details>
<summary>Dashboard</summary>

![Image](media/testing/lighthouse/dashboard.png)
</details>


<details>
<summary>Detail page</summary>

![Image](media/testing/lighthouse/detail-page.png)
</details>


<details>
<summary>Profile page</summary>

![Image](media/testing/lighthouse/profile.png)
</details>


[Back to the top](#table-of-content)

Back to [main README](readme.md)