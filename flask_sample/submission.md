<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Anisha Sharma (as4283)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 2:36:32 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/as4283" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/CJrpJR1/Show-invalid-password-validation.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/cb1hSQb/Show-passwords-not-much-validation.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/QbdBVh3/Show-invalid-email-validation.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows invalid email validation error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/p1W0QvQ/Show-email-not-available-validation-already-registered.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the validation for already registered email.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/526hrX1/Show-username-not-available-validation-username-is-taken.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the validation when new user tries to use username already<br>taken by another user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/pvwJV15/Show-the-form-with-valid-data-filled-in-before-the-form-is-submitted.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the prefilled data before hitting the register button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/XsCQZjW/The-valid-user-data-from-Task-1-should-be-present-in-this-screenshot-Clearly-highlight-which-row-it.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the users table in DB, where the record of recently<br>registered user is present<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">For the forms, we import something called as WTForms. It's<br>a flask extension for creating and handling forms on the application. It makes<br>it easier to manage the forms that are necessary. It also has basic<br>form validation techniques, security features, and is also responsive. With these techniques we<br>can validate the user input like modify it to take only valid data.<br>For example, password should be at least 8 characters. We also use _formhelpers,<br>which is a jinja macro. FlaskForm is the base reform. This form displays<br>and validates our forms on front and backend without any interference. The validators<br>take the input from the forms, passes it and verifies it to the<br>given criteria. If it matches with the provided criteria it validates and passes<br>the data. If it fails, it raises a validation error, or whatever the<br>exception is defined, in The validators take the input from the forms, passes<br>it and verifies it to the given criteria. If it matches with the<br>provided criteria it validates and passes the data. If it fails, it raises<br>a validation error, or whatever the exception is defined, in this case flash<br>messages. When the password is entered, a function hash is passed.</p><p class="p1" style="margin-bottom:<br>0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica<br>Neue&quot;;">The hash is a crypt algorithm where the password is encrypted with a<br>certain algorithm and makes sure the password is not directly displayed in the<br>database. It converts it into a series of letters and numbers and the<br>password is always protected. Sometimes, if two users have the same password, the<br>hashed value will still be different because of the salt values. Salt values<br>are values which are generated and added to the hashed value, so that<br>even though the passwords are similar, the hashed values are not the same.<br>The database has a table called as IS601_Users. Whenever a new user registers,<br>the data provided during the sign up is stored in it. It has<br>id, name, email, password (which would be hashed), and username as well. Once<br>all the data is validated, separate records are created for the user and<br>stored in it. It has id, name, email, password (which would be hashed),<br>and username as well. Once all the data is validated, separate records are<br>created for the user and stored in the table. While registering, it also<br>checks for duplicate data i.e., it checks if the data already exists and<br>throws a flash message.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/DGncRZK/Show-validation-based-on-non-existing-user.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot is for&quot;Show validation based on non-existing user&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/SxPzGDM/Show-password-mismatch-validation-doesn-t-match-what-s-in-the-DB.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the validation for mismatch password<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/gVvZSRM/Add-a-screenshot-of-successful-login.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message after user has logged in successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">For the forms, we are using WTforms. We first obtain<br>the username or email and password details from the user logging in through<br>form data. The data obtained is then passed onto the validation logic that<br>is present at the back end part of the application. First the data<br>is got from the forms and passed onto the validation part. Here the<br>obtained username or email got from the forms is searched with the existing<br>database through sql select query to see if it already exists. If that<br>result is found, it carries onto the next step, if not a flash<br>message is given. If the result is found in the database, the obtained<br>password from the forms is hashed using the hashing alamrit! function hac a<br>special function password check<span class="Apple-converted-space">&nbsp;</span>which validates and checks the password if it's accurate.<br>If the password doesn't match, flash message is given to the users indicating<br>that password is invalid.</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal;<br>font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">If the password is correct, then the<br>user successfully is logged in and is redirected to the landing page where<br>they can see their profile and logout as well. So when logging in,<br>user is fetched by username or email that is stored in the DB,<br>and then we use berypt to compare the existing hash with the raw<br>login password. If all the things matches, an user object is generated and<br>it is passed to login_ user in the flask_login which will carry out<br>the remaining session. We use bcrypt that has special function that takes the<br>original hash and takes the raw password, and then extracts the salt value<br>from the hash and applies it to the raw password and then generates<br>a hash. This is then compared with the existing data in the database.<br>The password is handled using a special function called hash. The hashing is<br>an encryption algorithm, which encrypts the password converting it into a series of<br>character's and string's hiding the actual password given by the user. When the<br>user is logging in, the password is hashed and then checked across the<br>database. If the password is matched, then the user can access the landing<br>page. If it's not validated, th user cannot access the landing page, and<br>they can see a flash message telling invalid password. The database is accessed<br>multiple times to check if the user is already registered with it. Select<br>query is used to check the user is present or not, and the<br>check_pasword of the hashing function checks if the password entered is the same<br>or not. When all these data is validated, the data is obtained from<br>the database displaying the user name and redirected to the landing page where<br>user can access other functions.</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch:<br>normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">All these function are majorly handled<br>by flask, flask form, and flask wtforms.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/WDpwSxN/Message-should-show-something-about-being-logged-out.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message after logging out as &quot;Successfully logged out&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/R9zMs8p/Message-should-show-something-about-not-being-logged-in.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the error when logged out tries to access login protected<br>page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">When logging in, user is fetched by username or email<br>that is stored in the DB, and then we use bcrypt to compare<br>the existing hash with the raw login password. If all the things matches,<br>an user object is generated and it is passed to login_user in the<br>flask_login which will carry out the remaining session. When the logged in user<br>tries to logout, they have a user object which already created when logged<br>in. So when the user tries to log out, this user object is<br>deleted as well as the user session via the logout_user(). It then redirects<br>the page to login page. The application knows which user is logging out,<br>because the server side session has key value pairs under special id. the<br>special id is generated by the session, on client side a cookie is<br>generated. It records a number and is sent to browser where the request<br>should be validated. if the session is present it is loaded, if not<br>a new one is created.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/7tGX07F/Message-should-show-something-about-not-being-logged-in.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the response of the app when logged out user can&#39;t<br>access a login protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/pJnbKBd/Message-should-show-something-about-not-having-proper-role-or-permission-i-e-different-than-the-not.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the after response of app when a user other than<br>admin tries to access role protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/558Y0vV/Must-have-at-least-one-valid-record-from-the-lessons-i-e-Admin.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshots shows the Roles table data from DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/svp85QD/Caption-which-is-your-admin-user.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the UserRoles table with valid data from DB, here the<br>users with role_id as -&quot;1&quot; is the admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">The auth.landing page redirects the page to the logged in<br>landing page. It uses a function called login_required. It is provided by flask<br>login. If the user is logged in it will let the route execute.<br>If the user is not logged in, it throws an error, it will<br>show unauthorised to the user. Each of the routes is protected by the<br>admin permission decorator which will trigger a 403 error when user try and<br>access the login protected page without actually logging in.</p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">The roles assigned to particular users only have access to<br>that specific roles. They can't access another roles assigned to other users or<br>any other roles which are not assigned to them. It is validated in<br>the code in the backend, and only when the validators check and pass<br>the access, only then they can access the role protected pages.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/12z7Gqk/Navigation-should-be-styled.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the styles and theme of site, including navigation, forms, and<br>data output with rows and columns.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">We are using the &lt;style&gt; attribute to display the data<br>in the required way. We can also create a separate file and then<br>invoke it. We can set the background colour, font size and test colour<br>etc. We can accordingly design an attractive form and pages so that it<br>is visible and likeable to the user.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/2NWWHHg/Show-email-not-available-validation-already-registered.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot a flash message is delivered when user tries to enter<br>already registered email id.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/6mQNJ22/Show-invalid-email-validation.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot a flash message is delivered when an invalid email is<br>entered by user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/6s1XKTv/Show-password-mismatch-validation-doesn-t-match-what-s-in-the-DB.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message delivered the password doesn&#39;t match with what&#39;s stored<br>in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">To handle the technical errors or to provide useful information<br>to the user, we are using flash messages. We use the flash() method<br>for it. It basically is used to display useful information to the user.<br>It creates a message and passes it to a template file for viewing<br>it. Then we replace our error or informative information with calls to the<br>flash function. Flask also has this as a built in function.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/rxbLbn7/Email-and-username-should-prefill-properly.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot the prefilled data under user profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">When profile is clicked, it will get a new form<br>which is a copy of the register but we will have an extra<br>field for current password. It will fetch the user_id from the current user<br>from flask login object. The profile form will check the email and username<br>via regex. Since the user id is got from the current user, the<br>pre loaded data is got from the current user id and shows up<br>without filling anything.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/fpKXBDM/Show-password-mismatch-message.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the password mismatch message, when the passwords entered by users<br>don&#39;t match while editng.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/7nShK3X/Show-password-validation-message.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the validation message after successfully editing the password for logged<br>in user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/0jc6gqS/Show-email-validation-message.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the validation message when user successfully edited the email id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/Zz9TQp5/Show-email-username-already-in-use-message.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the validation when user tries to use the already registered email<br>id by another user.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/pRx0PLy/Show-username-validation-message.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the validation message when user has successfully edited the username<br>for his profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/yY8CsBL/before-updating.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the record before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/3Mf4Rgs/after-updating.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the record after updating<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/22">https://github.com/Anishaa13/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">In the profile form, when the details are filled and<br>submitted, it will check the username/email. The username is checked via regex. If<br>all the fields of current password, new and confirmed are filled, it will<br>be validated with the current password similarly to how login method works. if<br>everything works properly,</p><p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">It updates the current password hash with the<br>new password. Every time we submit the form, username and the email is<br>updated every time even if there is no change detected. the form is<br>then refreshed with the session data of the user.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>This Milestone clearly highlighted the entire course, and it had all of the<br>elements taught to us from the beginning. I learned a lot about flask,<br>html, and sql. I can now create and deploy an app on Heroku.</div><div>I<br>realized how forms work and how data is processed in the backend. I<br>learned how to apply the roles specifically. There is transitivity between the roles<br>and users tables. I did not overly style my html pages, only the<br>essentials. I also learned how to use different data to login, such as<br>an email address or a username, and validate them. The flash messages are<br>very useful for providing users with data and any incorrect data. The flash<br>messages can be used from the most basic to the most advanced level<br>of the application, making things easier while developing as well as for the<br>user.</div><div>I also learned about password hashing. How have the passwords differed? This Milestone<br>clearly highlighted the entire course, and it had all of the elements taught<br>to us from the beginning. I learned a lot about flask, html, and<br>sql. I can now create and deploy an app on Heroku. I realized<br>how forms work and how data is processed in the backend. I learned<br>how to apply the roles specifically. There is transitivity between the roles and<br>users tables. I did not overly style my html pages, only the essentials.<br>I also learned how to use different data to login, such as an<br>email address or a username, and validate them. The flash messages are very<br>useful for providing users with data and any incorrect data. The flash messages<br>can be used from the most basic to the most advanced level of<br>the application, making things easier while developing as well as for the user.I<br>also learned about password hashing. I had no idea the passwords had different<br>hashed values even though they contained the same characters. This milestone introduced me<br>to the concept of salt values. This milestone serves as the foundation for<br>any final projects assigned to us, making it much easier to develop them.<br>Also grasped the concept of pre-filling the form with existing user information by<br>obtaining the current user id from the form. This provided a basic understanding<br>of how to begin developing a web application and integrate it with a<br>database in the backend using SQL. I already had a basic understanding of<br>sql, but this milestone allowed me to learn even more about it.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/">https://is601-as4283-prod2.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/as4283" target="_blank">Grading</a></td></tr></table>