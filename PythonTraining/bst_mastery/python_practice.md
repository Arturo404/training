# The Great Binary Adventure: Five Days of BST Mastery with OOP and MongoDB

Before running each test, it is essential to ensure a clean and consistent starting point for your treasure-related operations. To achieve this, consider adding a dedicated Flask route, /delete_all_treasures, that is designed to clear all treasures stored in your system. This route, when accessed with the DELETE method, will reset the treasures to an empty state.

## Step 1: The Quest Begins - Creating Your BST

**Set Up:**
To embark on this magical journey, set up a Flask server at the following URL: `http://127.0.0.1:5000`. The server should include two routes:

Insert Treasure:
Create a route named insert_treasure to insert new treasures into the BST. The route should accept a variable in the following structure: {'value': X}.

Get Treasures:
Create a route named get_treasures to retrieve all the treasures from the BST in the correct order. Ensure that the response should be in this structure: {"treasures": []}.

A successful response should have a status code 200. If there's an error, return a status code 400.

## Step 2: Dealing with Dark Forces - Deleting Treasures

**Set Up:**
Create a route named delete_treasure to delete a treasure from the BST. The route should accept a variable in the following structure: {'value': X}.
A successful response should have a status code 200. If there's an error, return a status code 400.

## Step 3: The Search for the Hidden Gem - Seek and You Shall Find

**Set Up:**
Make sure to Provide the value you want to search for in with the route `search_treasure`, like this: `/search_treasure?value=2`. 
The function should return a success message (`Treasure found!`) with a status code of 200 if the treasure is located, or a failure message (`Treasure not found`) with a status code of 400.

## Step 4: The Secrets of Tree Knowledge - Traversals

**Set Up:**
To enhance the functionality of your treasure management system, consider adding three new routes: /in_order_traversal, /post_order_traversal, and /pre_order_traversal. These routes will enable you to perform in-order, post-order, and pre-order traversals on your Binary Search Tree (BST). When a GET request is made to any of these routes, the corresponding traversal method should be executed on the BST, and the resulting treasures should be returned in a well-defined order. Ensure that a successful traversal operation returns a response with an HTTP status code of 200, indicating that the request was processed successfully. The response body should contain a JSON structure with the key 'traversal_result' representing the treasures in the specified order, such as {'traversal_result': […]}.

## Step 5: The Grand Finale - Validation and Visualization

**Set Up:**
To enhance the capabilities of your treasure management system, introduce a new route named /validate_bst. Upon a successful validation, the route should return a response with an HTTP status code of 200 and a JSON structure in the body, containing the key "message" with the value "BST is valid". In case the validation fails, the route should return a response with an HTTP status code of 400 and a JSON structure in the body, containing the key "message" with the value "BST is not valid".
