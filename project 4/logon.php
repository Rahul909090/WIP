<?php

$EMAIL_ID = 394028589; // 9-digit integer value (i.e., 123456789)

require_once '/home/common/php/dbInterface.php'; // Add database functionality
require_once '/home/common/php/mail.php'; // Add email functionality
require_once '/home/common/php/p4Functions.php'; // Add Project 4 base functions

processPageRequest(); // Call the processPageRequest() function

// DO NOT REMOVE OR MODIFY THE CODE OR PLACE YOUR CODE ABOVE THIS LINE

function authenticateUser($username, $password) 
{
	$value = validateUser($username, $password);
	
	if(value !== NULL){
		session_start();

		$_SESSION["userId"] = $value['ID'];
		$_SESSION["displayName"] = $value['DisplayName'];
		$_SESSION["emailAddress"] = $value['Email'];

		return true;
	}else{
		return false;
	}
}

function displayLoginForm($message = "")
{
	require_once './templates/logon_form.html';
}

function processPageRequest()
{
	// DO NOT REMOVE OR MODIFY THE CODE OR PLACE YOUR CODE BELOW THIS LINE
	if(session_status() == PHP_SESSION_ACTIVE)
	{
		session_destroy();
	}
	// DO NOT REMOVE OR MODIFY THE CODE OR PLACE YOUR CODE ABOVE THIS LINE

	if($_POST){
		if(isset($_POST['action']) && $_POST['action'] === 'login'){
			$username = $_POST['username'];
			$password = $_POST['password'];

			$testValue = authenticateUser($username, $password);

			if($testValue){
				header("Location: index.php");
				exit();
			}else{
				$message = "Invalid username or password.";
				displayLoginForm("$message");
			}
		}
	}else{
		displayLoginForm();
	}
}

?>
