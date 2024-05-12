<?php

$EMAIL_ID = 394028589; // 9-digit integer value (i.e., 123456789)
$API_KEY = "e6805246"; // API key (string) provided by Open Movie DataBase (i.e., "ab123456")

session_start(); // Connect to the existing session

require_once '/home/common/php/dbInterface.php'; // Add database functionality
require_once '/home/common/php/mail.php'; // Add email functionality
require_once '/home/common/php/p4Functions.php'; // Add Project 4 base functions

processPageRequest(); // Call the processPageRequest() function

// DO NOT REMOVE OR MODIFY THE CODE OR PLACE YOUR CODE ABOVE THIS LINE

function addMovieToCart($imdbID)
{	
	$movieID = movieExistsInDB($imdbID)
    
    if($movieID === 0){
        $result= file_get_contents('http://www.omdbapi.com/?apikey='.$GLOBALS['API_KEY'].'&i='.$imdbID.'&type=movie&r=json');
        $movieInfo = json_decode($result, true);

        $movieID = addMovie($imdbID, $movieInfo['Title'], $movieInfo['Year'], $movieInfo['Rated'], $movieInfo['Runtime'], $movieInfo['Genre'], $movieInfo['Actors'], $movieInfo['Director'], $movieInfo['Writer'], $movieInfo['Plot'], $movieInfo['Poster']);
    }

    $userID = $_SESSION['userId'];
    addMovieToShoppingCart($userID, $movieID);

    displayCart();
}

function displayCart()
{
	$userID = $_SESSION['userID'];
    $movies = getMoviesInCart($userID);

    require_once './templates/ cart_form.html';
}

function processPageRequest()
{
	if(!isset($_SESSION['displayName'])){
        header("Location: logon.php");
        exit();
    }

    if(isset($_GET['action'])){
        $action = $_GET['action'];

        switch($action){
            case 'add':
                if(isset($_GET['imdb_id'])){
                    $imdbID = $_GET['imdb_id'];
                    addMovieToCart($imdbID);

                    header("Location: index.php");
                    exit();
                }
                break;
            case 'remove':
                if(isset($_GET['movie_id'])){
                    $movieID = $_GET['movie_id'];
                    removeMovieFromCart($movieID);

                    header("Location: index.php");
                    exit();
                }
                break;
        }
    }else {
        displayCart();
    }
}

function removeMovieFromCart($movieID)
{	
	$userID = $_SESSION['userId'];
    $removed = removeMovieFromShoppingCart($userID, $movieID);

    header("Location: index.php");
    exit();
}

?>