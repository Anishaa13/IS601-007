<table><tr><td> <em>Assignment: </em> M2 Python-HW</td></tr>
<tr><td> <em>Student: </em> Anisha Sharma (as4283)</td></tr>
<tr><td> <em>Generated: </em> 9/24/2022 6:21:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/m2-python-hw/grade/as4283" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you have the dev/prod branches created before starting this assignment.</p><p>Pre-req Steps if not done so yet:</p><p><ol><li>git checkout main</li><li>git checkout -b dev</li><li>git push origin dev</li><li>git checkout -b prod</li><li>git push origin prod</li></ol><div>This will ensure you have a dev and prod branch on github.</div></p><p>Setup steps:</p><ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M2-Python-HW</code></li></ol><p>You'll have 3 problems to save for this assignment.</p><p>Each problem you're given a template&nbsp;<strong>Do not edit anything in the template except where the comments tell you to</strong>.</p><p>The templates are done in such a way to make it easier to capture the output in a screenshot (if it's still not able to fit well, you can zoom out in your browser).</p><p>You'll copy each template into their own separate .py files, immediately git add, git commit these files (you can do it together) so we can capture the difference/changes between the templates and your additions. This part is required for full credit.</p><p>HW steps:</p><ol><li>Open your IDE at the root of your repository folder</li><li>In your IDE create a new folder/directory called M2</li><li>Create 3 new files in this new M2 folder (problem1.py, problem2.py, problem3.py)</li><li>Paste each template into their respective files</li><li><code>git add .</code></li><li><code>git commit -m "adding template baselines</code></li><li>Do the related work (you may do steps 8 and 9 as often as needed or you can do it all at once at the end)</li><li><code>git add .</code></li><li><code>git commit -m "completed hw"</code></li><li>When you're done push the branch<ol><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Create the Pull Request with&nbsp;<strong>dev</strong>&nbsp;as base and&nbsp;<strong>M2-Python-HW</strong>&nbsp;as compare</li><li>Create a new file in the M2 folder in your IDE called m2_submission.md</li><li>Fill out the below deliverable items, save the submission, and copy to markdown<ol><li>For this assignment you may get screenshots from your IDE output or terminal/console output</li></ol></li><li>Paste the markdown into the m2_submission.md</li><li>add/commit/push the md file<ol><li><code>git add m2_submission.md</code></li><li><code>git commit -m "adding submission file"</code></li><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Merge the pull request from step 11</li><li>On your local machine sync the changes<ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li></ol></li><li>Make a pull request from&nbsp;<strong>prod</strong>&nbsp;as base and&nbsp;<strong>dev</strong>&nbsp;as compare and immediately merge it</li><li>Submit the link to the m2_submission.md file from the prod branch to Canvas</li></ol><p><strong>Template Files</strong>&nbsp;You can find all 3 template files in this gist:&nbsp;<a href="https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e">https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e</a></p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Problem 1 - Only output Odd values of the Array under "Odds output" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 1 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/192118519-1389041c-68f7-4958-b40a-4ed307ce22c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot contains the modified code and output according to the problem definition<br>, printing all odd values of the array&#39;s. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>According to the problem definition, program should only print odd values. Here, I<br>used for loop, to iterate each num in the array and check if<br>num is not divisible by 2 and is not equal to 0 and<br>if the condition satisfies , then the number will be printed. This loop<br>will keep working until all the values are checked against the condition .<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Problem 2 - Only output the sum/total of the list values by assigning it to the 'total' variable (the number must end in 2 decimal places, if it ends in 1 it must have a 0 at the end) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 2 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/192118465-50ce5f81-e6c7-4327-b201-49ea3b5d8614.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the modified code and its output according to the task<br>needed to be done, printing total of the list of values.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>According to the task needed to be done, the code should print the<br>total of the list of values. Firstly we assigned a total variable and<br>used a for loop where the value of total variable will be updated<br>with each iteration and at the time of printing only value with 2<br>decimal places will be printed for that we have used {:.2f}.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Problem 3 - Output the given values as positive under the "Positive Output" message (the data otherwise shouldn't change) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 3 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113552842/192118253-7d4b39e9-67f6-4fab-8fe6-e599a36bb692.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot contains modified code and its respective output.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>The task is to print values as positive. i used if loop to<br>check if the value is positive or negative, suppose its negative then, multiply<br>it by -1 and convert it to positive value or else it will<br>be printed as it is, now we add next if loop to check<br>if the value is string or not and if its not string and<br>instead is a negative value, multiply it by -1 to make it positive<br>or else the value will be printed as it is. This is the<br>logic behind the code<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc Items </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Pull Request URL for M2-Python-HW to dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/2">https://github.com/Anishaa13/IS601-007/pull/2</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Talk about what you learned, any issues you had, how you resolve them</td></tr>
<tr><td> <em>Response:</em> <p>This HW covered a lot of python topics from printing to type conversion.<br>I personally struggled with the logic execution part and also typing incorrect syntax’s.<br>It took me some time to understand, build and execute the code. But<br>with right practice and learning i completed all the tasks. I look forward<br>to grow more in this technical area.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/m2-python-hw/grade/as4283" target="_blank">Grading</a></td></tr></table>