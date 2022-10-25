<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Anisha Sharma (as4283)</td></tr>
<tr><td> <em>Generated: </em> 10/24/2022 11:42:10 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/as4283" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197426536-dbe26d31-9e5a-4a31-888f-05b81ed91c71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the choices of container, flavor and topping considered by the<br>user, and the cost amount generated afterwards by using the logic behind.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197426554-7659f700-1b14-48e8-a3aa-c586d25af032.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows the choices of container, flavor and topping considered by the<br>user, and the cost amount generated afterwards by using the logic behind.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p><font size="2">Since we&nbsp;already&nbsp;have defined the price amount for each of the container, toppings<br>and flavors, it is easy for us to calculate the total amount after<br>taking all the input from the user. So this is how it&#39;s done,<br>for ex: The user is chose cup as a container for his IceCream,<br>cost for one cup is 1$ and for flavor its 2$(vanilla, chocolate) and<br>lastly for toppings its 0.50$(Chocolate chips, m&amp;m&#39;s). Now we&#39;&#39;ll sum it all up<br>using &quot;cost=cone_price+(number_of_scoops)<em>(flavor_price)+(number_of_toppings)</em>(toppings_price)&quot;. cost= 1+2<em>1+2</em>0.25= 3.5. The total cost for the user&#39;s IceCream will<br>be $3.5.</font><div><font size="2">The user will be asked to choose their desired container, flavor<br>and toppings, they can add more than one of those and then in<br>the end an exact price amount for the icecream will be asked as<br>input to complete the procedure.</font></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675247-5c757661-c47c-497f-9136-b7c099cb355b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for OutofStockException when checked against icecream flavors.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675333-9f9098fb-3735-41af-a5a7-44940f72e9cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for OutofStockException when checked against toppings.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675644-b98f997b-7326-430c-8efd-0b37c777028a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for InvalidChoiceExceptions when checked against icecream flavors.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675704-a479177e-74ad-430d-8547-21efe5617909.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for InvalidChoiceExceptions when checked against toppings.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675830-ecff91d1-2320-486c-a18c-c2c9f906a6d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for ExceededRemainingChoicesExceptions when checked against flavors.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197676866-2c489cd6-75e4-4ca6-a066-38d523d938d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for ExceededRemainingChoicesExceptions when checked against toppings.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197676227-00e75e29-0c79-47f7-9a86-80b8a5cc03d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197676335-e549f10f-1c8b-4a35-960a-2c3d25964052.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197676413-e6e130a5-7715-4c1f-8f9d-30e3cc1458a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for NeedsCleaningException when checked against flavors.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197675490-0ddbb689-9161-4829-b6db-57b5f2880132.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for InvalidChoiceExceptions when checked against icecream containers.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197676042-0ee538e8-2b7a-472a-932f-08c804afbd8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the output for ExceededRemainingChoicesExceptions when checked against flavors.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>OutOfStockException: This exception occurs when a particular topping or a scoop is out<br>of stock</div><div>NeedsCleaningException: This exception occurs when the machine needs to go under cleaning<br>after a certain amount of rounds</div><div>InvalidChoiceException: This exception occurs when the user enters<br>a choice which is not available in options&nbsp;</div><div>ExceededRemainingChoicesException: This exception occurs when the<br>user exceeds the number of given choices</div><div>InvalidPaymentException: This exception occurs when the user<br>puts in the wrong amount</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468285-f85d2411-d388-49e2-b8bc-ebd21cd1d594.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468319-f1c1f5c1-e576-4668-808d-7a488482f4a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468347-eeae06a2-fd2d-41b9-bbec-e858239a4ad1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468372-c89e3706-6bb5-494f-aecc-f2fe60891cc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468410-341b4f77-a7be-4415-b0db-08154cfd8ea4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468432-cab865ac-0cb8-4633-b0ad-5fcddaaff6af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468462-c92f6e0c-66f7-464d-ab46-fc981bb6b141.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468498-51298966-167b-4667-85cf-8e51c8617749.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468534-1f3366c8-7a2d-4e0f-af60-9e2d0fa564a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197468556-b2537d79-84e6-4243-9e2d-45e57be92192.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the output for test case8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test1: Container is the first selection in this case followed by flavors and<br>toppings.<div>Test2:&nbsp;<span style="font-size: 13px;">flavors can only be added if they&#39;re in stock.</span></div><div>Test3:<span style="font-size: 13px;">&nbsp;toppings<br>can only be added if they&#39;re in stock</span></div><div>Test4: user can&nbsp;<span style="font-size: 13px;">add up<br>to 3 flavors/scoops</span></div><div>Test5:User c<span style="font-size: 13px;">an add up to 3 toppings</span></div><div>Test6:&nbsp;<span style="font-size: 13px;">cost<br>is calculated properly based on the user input.</span></div><div>Test7: Sum of costs is&nbsp;<span style="font-size:<br>13px;">calculated properly</span><span style="font-size: 13px;">&nbsp;by including</span><span style="font-size: 13px;">&nbsp;a few IceCream combinations</span></div><div>Test8:<span style="font-size: 13px;">Total IceCreams<br>are properly incremented for each purchase</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/5">https://github.com/Anishaa13/IS601-007/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I had difficulties with the test cases and I could not run them<br>at first, but then i observed code and cleared my small doubts and<br>tried to implement the logic and with few attempts i resolved all the<br>errors.<div>Apart from that i learned exception handling methods and their executions, and this<br>assignment is such a good hands on experience for exception handling.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197474180-0e71ff50-06b9-4ef5-84d4-8146a39e11ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot includes successful execution of the code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/197474228-1ad89cf4-aeb6-4f1e-9036-67dc36ea3d1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot includes successful execution of the code <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/as4283" target="_blank">Grading</a></td></tr></table>