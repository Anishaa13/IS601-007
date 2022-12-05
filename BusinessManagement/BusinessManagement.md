<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Anisha Sharma (as4283)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2022 3:03:45 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/as4283" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546369-cf7efb50-ba6e-4f78-ac38-ff78e8dd1536.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home page with updated UCID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546687-a3b29a7e-1f04-4968-828d-f8fb0a4df4c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the updated code in layout.html<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546750-cfb17bc0-c85f-4ead-aa40-b80bd079f958.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot Shows the employee table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546759-f63f688c-2f68-4115-955e-0f1618f88922.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the company table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546816-9a290b01-ecbb-44c6-bdf8-45d87da7d4f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows highlighted code for flash message to be generated nothing how<br>many records were processed for employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546818-048950dd-cb5c-4a98-a4d4-b055fa52cc89.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows highlighted code for flash message to be generated nothing how<br>many records were processed for company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546822-6fa03172-ac0c-4c78-811a-d626a3f03867.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message if the particular list wasn&#39;t loaded or<br>was empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547002-ae62d074-4729-4d23-bc30-c95b68aa17c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code for company data appended as a dict to<br>company list.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547014-45e8628d-c2cd-464d-9fba-324da31d612f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code for employee data appended as a dict to<br>employee list.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547049-fcff7406-1657-4c5e-8b47-eb889e246ab2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot code for &quot;CSV file should be read from the provided stream<br>as a dict&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546383-f9c6657b-1055-43bd-a5f7-48195861f10b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this screenshot displays the error when there&#39;s no file selected to upload<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546408-81eb3337-e3d9-4a28-adb8-aeca4eaf1694.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the error message when the file is not a .csv<br>file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205557388-8ed70463-91ba-4779-90d5-eea718a19406.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the success message and count message after the file was<br>inserted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546820-2bfacc7c-1932-4329-886d-95c922c474ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the company data record in DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546751-dd7bb640-9557-4804-bdc5-443cbb38456e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the employee data record in DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547061-c820312b-5000-49c6-adf8-dff659cc0f24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the insert query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547061-c820312b-5000-49c6-adf8-dff659cc0f24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows proper flash message for missing email, first name and last<br>name, except block flash message also &quot;Code should retrieve first_name, last_name, company (id),<br>email&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546400-63a4807a-ab96-4de2-9412-8ce36fcd656b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the success message after the record is created<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546401-02ca252c-3eca-4d2c-8ece-e408adf3bfeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the error when employee record was created without adding the email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546402-b1435289-f699-4530-8ab3-b2d636002481.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the data entered before creating the employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546404-fd681b6d-3c0a-47dc-95d4-41d8fe606232.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the data without including last name while creating the record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546405-9ff6e130-006f-40e3-b256-683559130a51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without last<br>name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546406-2f556ce5-3b8d-463c-9f62-c65f7172071d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without first<br>name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546521-a4b3ad39-c661-47ef-9e37-0f1d5eca8c0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without first name to create a record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546765-8af62d88-7bd0-4624-958d-b079c425d3d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the new employee record in DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546809-ef4f30a7-351b-425d-b021-40c7a29db966.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code for append filter for first name, last name<br>and email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546811-65d0b7b6-d7f5-4e01-b502-106304b69d21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the append limit (default 10) or limit greater than 1<br>and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546814-ac1f0f74-73b0-4526-adca-6461456aa440.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for limit if its out of bound&#39;s<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547009-5e94bdb1-c9a2-4603-93e6-a6971121fbc8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code of append sorting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547106-bb6ec1bb-652c-4583-b134-776cb15c5fdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547105-70710982-88e6-43c9-9e4b-dbac0b3040d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;Check request args for fn, ln, email, company, column, order,<br>limit (exact naming is required)&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546688-00d7ba90-9035-4e4a-a2a2-bbfbb00d541c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows one asc filter applied with first name coulmn<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546690-231abadd-093c-46f9-98b6-4a4630a37997.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows one desc filter applied with last name column<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546691-8f6a1ede-d03f-400e-86ef-be0309503b62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the result with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546692-1479ae1a-3ef7-43d2-873a-773d9b18bf7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the result with first name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546694-0a227012-9163-419a-ae01-40c1f4c0dbcb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the result with last name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205565022-67c227ca-61ce-43d8-8f0f-560ead276a9a.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the result with country filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546819-e0e95810-0c09-4782-ae2f-4d1910a9bd47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the update query for employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547005-875fdb9e-cb6b-455d-b6be-2b8d8a7488f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code of flash message requiring last name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547006-07b40a79-d1c5-4e35-9dc9-0c6344704103.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows except block flash message for successfully updating the record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547008-fbc51b64-fb55-482d-9def-c7b7d3bab03f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows except block flash message for failing to update the record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547045-4b6fd779-b47d-4c6d-811a-45b296162ede.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code retrieving id (from request args)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547051-da15df4e-882d-4e16-96d4-608ef1bfbc78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547054-af7bdaf0-e572-48a9-a4a1-977b4d1aeca8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;first_name, last_name, company (id), email from form&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547058-fdbda161-59b1-49a1-8e02-96984cd61653.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;Employee data should be passed to the render_template()&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547013-1d5b4496-b7f9-4177-b00c-b42632f5f84c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547107-050467aa-2a2b-498a-9772-59903cfe7cc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547107-050467aa-2a2b-498a-9772-59903cfe7cc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message for missing last name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546517-f05d7dc7-ead6-4eaa-a4cd-5b8889c40a9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data after the edit was made<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546511-22137317-9942-45b1-9868-a650b61efa9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data before the update was made<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546508-0471ba03-0686-4bdc-896d-07807e7e97e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the success message after data was updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546765-8af62d88-7bd0-4624-958d-b079c425d3d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205583528-fea35456-c6c4-4886-8c45-908d84262a22.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the data after editing<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547209-d6637496-20fc-4016-bfc4-85c99d8b5655.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message error for country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553812-03802c99-2754-438d-89ce-7ba2d30284d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows except block flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547218-d870a965-dcf6-4e15-a243-851c3674cb52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message for missing city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553797-e2e25aef-d24f-44c4-b1d5-bbf259b1e28b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;code should retrieve form data for name, address, city, state,<br>country, zip, website&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553806-334dc9fb-ee8a-497a-962e-fa727b90f037.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553807-f89c98e2-b25d-45ed-a8bd-d7676d4f1511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the insert query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553810-b680205f-6cc6-4db6-aa1f-c692bafeb657.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message for missing state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553812-03802c99-2754-438d-89ce-7ba2d30284d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the except block flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205553813-ceed96e8-5be7-4fff-8a68-903b3a1a6675.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the except block flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547209-d6637496-20fc-4016-bfc4-85c99d8b5655.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message for missing name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546509-6e8ce12d-5e14-45d7-96d3-5d0ac7d7d55e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without address<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546510-8dafcda1-f03d-4b3e-ace4-9509b8ca24e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546514-6b88d4fd-230a-4040-a706-f11be3de228c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546516-73c6f5da-2425-4c01-99d3-1f144df7cf08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546520-d4d1b8c7-613f-44bc-8d93-f91816cdbb03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash error when attempted to create record without city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546621-fd0d28ec-4a4d-4dcc-8560-627d5628e910.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the success message after company was added successfully.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546625-29f66ace-aea3-4b92-9871-011f9eed4ad8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including the state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546626-313eb92a-8c30-4e63-9a5c-ee540ecfecb4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including the country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546627-6da9bc3d-cf13-445d-b073-a284ae2458a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including the zipcode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546628-3b26eb8e-2882-47f7-a0ab-541e2c62f8f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including the name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546630-6d8086eb-9848-4d5f-a10d-c935c4b2b8c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546631-eeb66a77-625c-4086-93e3-79b591a423bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered without including city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546623-9a197d17-02c3-4ca9-a959-5ccf8c0c8083.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data entered while creating new company record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546763-30ade67d-4601-4c4e-a257-9d6deb3855dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the new company record added in DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547041-de1f0cce-77fb-46f1-894d-47d6618a6fdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the except block flask message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547043-7c6fc2e9-8ab0-47e8-84a6-1c83b1e54cb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the error message if limit isn&#39;t a number and it<br>is out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547047-67b65da5-e5b7-49cf-a867-001c76783aa2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the append limit code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547103-19b5d933-e0c5-4f48-8a06-bb174c7a244d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;append sorting if column and order are provided and within<br>the allows columsn and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547105-70710982-88e6-43c9-9e4b-dbac0b3040d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;Check request args for name, country, state, column, order, limit&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547206-34ad83fc-5c00-43e4-ada4-0a36f1bfda2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows&quot;append a LIKE filter for name, country and state&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546632-b050f599-7cf9-4fe7-9f57-be5f26f6555f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546696-60312a32-7fac-40b5-a1ab-50bd3f3863b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546764-dbb12d19-b94e-4697-8b4b-0e3281821a06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the result with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205559258-e6dc576a-36ae-464e-9036-22e5ed98ac34.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows one asc filter applied with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205559258-e6dc576a-36ae-464e-9036-22e5ed98ac34.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows one desc filter applied with country filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547010-c5f42814-2e5b-4371-9296-cb3c7996a9b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547011-552121ff-e17b-4ce5-b963-194d256336bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547050-87236ed1-daeb-4dca-8b8f-530fa0f1e53e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code for &quot;Company data should be passed to the<br>render_template()&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547094-5db9bd6e-5965-4035-89a0-a3f8a93b53a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547097-446a75d6-711b-46e4-9ad5-23a462abcafc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547098-59b50075-e4b1-4f16-83d9-4c4199fafde7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547100-facdb60c-fe9f-4dd4-bff3-54e3790519d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547109-4497f18f-d9f9-4379-88a9-546b6bd90c19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the except block flash message for successfully updating record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547111-a68cb38d-3213-46ec-aba3-23438b37ca4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the except block flash message for failing to update record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547211-9e4ec532-a38c-4e03-bce1-17485800f6ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows &quot;Code should retrieve id (from request args)&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547216-bc1495c3-702f-451c-93b4-58d6693af8a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message for missing state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205547219-121a1e80-1ef5-4a48-b3bc-aa46ee5db3a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows&quot;name, address, city, state, country, zip, website from form&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546623-9a197d17-02c3-4ca9-a959-5ccf8c0c8083.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data after an edit was made<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546629-b77ba51d-353e-4345-b4f2-16424cf0e259.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the flash message after the data was edited successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546627-6da9bc3d-cf13-445d-b073-a284ae2458a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data before an edit was made<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546758-69545a5e-bd03-47b0-9fec-a7ebafd155bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the record in DB before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546759-f63f688c-2f68-4115-955e-0f1618f88922.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the record in DB after editing<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546749-d44cf1cc-b583-4b2c-a422-3e8a8fa1ef7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the success message code for employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546753-97cb672a-bac9-4af1-86fd-877c47a95efa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows redirect to employee search code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546825-ee760bd0-7a45-4387-9735-7e46e704a982.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the delete query where employee is deleted by id<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205560699-8a3b0266-8732-4195-9ec4-09daa5f0387b.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the success message after deleting employee record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205560698-9f36e78d-9123-4fcb-96d3-d4a2f51a81e9.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows data before deleting the employee record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113266359/205583526-6795ccec-605d-4608-b182-629ed6c9db68.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>This shows the code for&quot;delete company by id&quot;, &quot;redirect to company search&quot;, &quot;All<br>request args (minus id) are passed to the redirect route&quot; also flask message<br>for successfully deleting the employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546697-376730d5-9859-404c-a10a-5745b4e67f85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the company data before deleting <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546699-fab753be-3298-42e2-908d-bf384b139117.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flash message after successfully deleting the record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/54863474/205546757-5a3cde70-64cf-4ada-9015-f94c7b64f360.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the running state of test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>While working on this assignment, i got a lot of my concepts cleared<br>up, for example sql queries, exception how to use it properly in code,<br>there were times i got confused between the other parts of code and<br>even messed up a bit, I mostly got stuck in edit company and<br>employee code also asc and desc part in both of the codes, &lt;span<br>style=&quot;font-size: 13px;&quot;&gt;but overall it was a good learning , i look forward to<br>learning more in upcoming milestones and projects.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/as4283" target="_blank">Grading</a></td></tr></table>