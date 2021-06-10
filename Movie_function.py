#[movie name, gross earning, year, rating out of 10, number of ratings]. input format
def get_name(movie_name):  # Get the movie name from the given List function
    name=movie_name[0]
    return name    # returning movie name 

def get_gross(movie): # Get the gross from the given List function
    gross=movie[1]
    return  gross        # returning gross earning

def get_rating(movie): # Get rating from the given List function
    rating = movie[3]
    return  rating        # returning rating out of 10

def get_num_ratings(movie): # Get number of ratings from the given List function
    num_rating = movie[4]
    return  num_rating            # returning number of ratings
## Better movie function ##
def better_movies(movie_name, lst):  
    better_movie = [movie for movie in lst if movie_name in movie]  #initial we are fetching complete information about input movie
    better_movie_list = [movie for movie in lst if get_rating(better_movie[0]) < get_rating(movie)] #by using get_rating function we are checking ratings 
                                                                                            #  which having more rating than inputted movie
    return better_movie_list            # Returning movies which having more ratings and related information
    
def average(category, lst):
    if category == 'rating':        #checking category is rating or not 
        index = get_rating          #Returning getrating function to get rating of the movie
    elif category == 'gross':       #checking category is gross or not
        index = get_gross           #Returning get_gross function to get gross earning of the movie
    elif category == 'number of ratings' or category == 'number of ratings'.replace(' ',''):#checking category is Number of rating 
        index = get_num_ratings     #Returning get_num_ratings function to Number of rating of the movie
    else:
        index =-1           #its not rating,gross,number of rating then this part will be take as invalid
    avg=0                   #initializing variable
    if index != -1:         #checking category is valid or not
        for i in lst:       # To get result we are looping data
            avg+=index(i)   #here storing data in avg variable
        Result = avg/len(lst)   #calculating avrage by avg value and divide by length or list
    else:
        return print("Category Not Exist.Enter Existing Category") #catrgoty is not existing then displaying message
    return "Average Of {} is {}".format(category,round(Result,2))  #Returning the results


################## If u are using module wise then Below Section Can Be Removed #########################
# input given as per the mentioned format
lst=[
    ['Avengers: Endgame',2.797,2019,8.2,532],
    ['Avengers: Infinity War',2.048,2018,7.6,474],
    ['The Avengers',1.518,2012,8.0,358],
    ['Avengers: Age of Ultron',1.405,2015,6.8,37],
    ['Black Panther',1.346,2018,8.3,515],
    ['Incredibles 2',1.246,2018,7.84,379],
    ['Iron Man 3',1.214,2013,7.0,325]
]

# This is the better movie function 
movie_name = input('Enter  Movie Name : ')
print(better_movies(movie_name,lst)) # Displaying the results from the better movie function 

category = input('Enter Category Name : ')  #input Category 
print(average(category, lst))  #Average function calling

