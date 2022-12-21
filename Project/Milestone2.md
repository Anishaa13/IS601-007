<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Anisha Sharma (as4283)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 12:56:02 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/as4283" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/BtMR5yM/Show-valid-data-filled-in.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the valid data filled in add products page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/Q6yzvyC/Columns-id-name-description-category-stock-created-modified-unit-price-visibility-true-false.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the Products table saved in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The item function in shop.py receives the values when they are entered on<br>the add page. To determine if the action is to edit or add,<br>it looks to see if an id has been passed. This is a<br>create action since no id will be supplied; hence, an INSERT statement is<br>executed passing the values to the Products table, and if successful, a flash<br>is shown.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/BgHRNHj/Should-have-10-sample-items.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the 10 sample items in shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/s5LNMj3/Sample-items-2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the 10 sample items in shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/D1Mv8yQ/Result-should-have-more-than-1-Sample-product-shown.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the product sample shown when two different filters are applied(product<br>type, sorting)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/wYGzTgv/Ucid-and-date-should-be-in-the-code-snippet-as-a-comment.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows filter/sort logic code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>For the shop page, we first retrieve the product information from the Products<br>table, whose visibility is set to 1. and on the page, we can<br>sort by price, choose a category, or conduct a name search. Low to<br>High or High to Low When we use one or more of the<br>aforementioned search options. We proceed to the shop.py function&#39;s shop list and modify<br>the query&#39;s where condition based on the input. and then show the outcomes<br>once more.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/MckMCB7/Should-show-non-visible-products-too.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the list of products from admin account<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>Without applying any filters, we choose every field from the Products database and<br>feed it to the html page. Since no conditions are mentioned anywhere, every<br>product will be shown regardless of visibility status.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/mtfygDk/showing-the-edit-button-visible-to-the-Admin-on-the-Shop-page.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the visibility of edit button to the admin on the<br>shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/rydrKt7/showing-the-edit-button-visible-to-the-Admin-on-the-Product-Details-Page.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the edit button visibility to the admin on Product details<br>page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/bdqfQQT/showing-the-edit-button-visible-to-the-Admin-on-the-Product-list-Page.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the edit button visibility to the Admin on the Admin<br>Product list page(The admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/Z8Btqd6/Add-a-before-and-after-screenshot-of-Editing-a-Product-via-the-Admin-Edit-Product-Page-before.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/4Vzkdp7/Add-a-before-and-after-screenshot-of-Editing-a-Product-via-the-Admin-Edit-Product-Page-after.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the data after editing, where the quantity of item is<br>changed to 70 from 50<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>We check the user&#39;s login status and administrator status for the Shop in<br>shop.html at the end of each product, and if both are true, we<br>display an edit button that takes the user to the item page with<br>the product details. The edit button is displayed on the item details page<br>if the user is an admin. As only admins can view the page,<br>the admin items page by default has an edit button.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/HhCSY1R/showing-the-button-clickable-item-that-directs-the-user-to-the-Product-Details-Page.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the button for clickable item that directs the user to<br>the Product Details page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/gWYQ7yG/showing-the-result-of-the-Product-Details-Page.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the result of the Product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>For this, I made the itemdetails.html item details function. The product name has<br>been made clickable; clicking it will send the product&#39;s id to the item<br>details function, which will then retrieve all of the information from the Products<br>database using the id and display it on the item details page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/zh6stg2/screenshot-of-the-success-message-of-adding-to-cart.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the success message which is flashed after adding the item<br>to the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/Bjt83yY/screenshot-of-the-error-message-of-adding-to-cart-i-e-when-not-logged-in.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the flashed error message when user who&#39;s not logged in<br>tries to add something in cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/C0n5bz8/Screenshot-2022-12-21-at-12-37-39-AM.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the cart table saved in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user, having product_id user_id as composite unique key<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>When the amount field is provided to the cart function in shop.py by<br>clicking the ADD button, the product id is passed as a hidden field<br>and as long as the quantity is larger than 0, we insert the<br>product id, user id, desired quantity, and unit price (fetching it from products<br>table)<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/W3yjYkn/screenshot-of-the-Cart-View.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the cart of when user is logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>When we click the cart, the function checks to see if a product<br>id is being passed and, if it isn&#39;t, it recognizes that this isn&#39;t<br>an add or update function. It then moves to the SELECT block to<br>get the user id, id, product id, name, and desired quantity, calculates the<br>subtotal by multiplying the desired quantity by the unit price, and passes these<br>values to cart.html. To calculate the total, we render each item as a<br>row in a table in the HTML output, add the subtotal value for<br>each row to a variable called ns.total, and then display the total at<br>the bottom.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/Qdn9bcn/Show-a-before-screenshot-of-Cart-Quantity-update.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken before updating the quantity for particular item in cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/Gkv7Q7M/Show-after-screenshot-of-Cart-Quantity-update.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken after quantity was updated, updated the quantity for knit<br>sweater and UGG from 1 to 2.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/5236pkV/before-setting-Cart-Quantity-to-0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken before setting the quantity as 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/nfrWkWC/setting-Cart-Quantity-to-0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken after setting quantity as 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/LZ75tZy/Show-how-a-negative-quantity-is-handled.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the error message given when the quantity is set as<br>-1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>When we click the update button next to the quantity field in the<br>cart, a concealed product id is sent to the cart function. And if<br>there are any changes to the quantity or price in the code, we<br>update the quantity and price in the cart table while passing the product<br>user id. As the number is less than 0, when we enter 0<br>in the quantity field, the code moves to the DELETE block, where we<br>delete the product from the cart database while passing the product id and<br>user id. We set the minimum value for the input field in HTML<br>to 0 to handle negative values in quantity fields.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/1fKC0pk/a-before-screenshot-of-deleting-a-single-item-from-the-Cart.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken before deleting a item from cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/7jdPN9p/after-screenshot-of-deleting-a-single-item-from-the-Cart.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken after deleting an item from the cart, vaccum cleaner<br>was removed from the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://i.ibb.co/wNX1k3P/Screenshot-2022-12-21-at-12-50-24-AM.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken after clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://i.ibb.co/ZHDVMpJ/Screenshot-2022-12-21-at-12-52-04-AM.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot was taken before clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When deleting a single item from a cart, a hidden field amount of<br>-1 will be supplied next to the delete button, and the cart function<br>will process the delete query while sending the product id if the number<br>is less than zero. When clearing the entire cart, we pass the variable<br>delete all with a value of 1, and if the delete all value<br>is True in the cart method, we delete the records in the Cart<br>table while passing the user id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Anishaa13/IS601-007/pull/26">https://github.com/Anishaa13/IS601-007/pull/26</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>After being stuck for a while trying to clear the cart, a thought<br>came to me to set a variable, pass it along when clearing the<br>cart, and verify the value in code to complete the task. The other<br>issue is displaying the shop&#39;s public page when no users are logged in.<br>Initially, I neglected to include an if statement for authentication around the edit<br>button and encountered an error because the code is checking for the admin<br>role in the current user even though no users are logged in. The<br>is authenticated condition was then put around the admin condition.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-as4283-prod2.herokuapp.com/login">https://is601-as4283-prod2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/as4283" target="_blank">Grading</a></td></tr></table>