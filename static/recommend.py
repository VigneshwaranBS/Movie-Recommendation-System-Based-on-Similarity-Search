import requests

def load_details(my_api_key, title):
  """
  This function gets the basic details of the movie from the API (based on the name of the movie).

  Args:
    my_api_key: The API key for themoviedb.org.
    title: The name of the movie.

  Returns:
    A dictionary containing the basic details of the movie.
  """

  # Make the API request.
  response = requests.get(
    'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + title,
    headers={'Accept': 'application/json'}
  )

  # Check the response status code.
  if response.status_code != 200:
    raise Exception('Error getting movie details: ' + response.status_code)

  # Parse the JSON response.
  data = response.json()

  # Return the basic details of the movie.
  return {
    'id': data['results'][0]['id'],
    'title': data['results'][0]['original_title'],
    'poster_path': data['results'][0]['poster_path'],
    'release_date': data['results'][0]['release_date'],
    'rating': data['results'][0]['vote_average'],
    'vote_count': data['results'][0]['vote_count']
  }

def get_movie_cast(movie_id, my_api_key):
  """
  This function gets the cast information for the specified movie.

  Args:
    movie_id: The ID of the movie.
    my_api_key: The API key for themoviedb.org.

  Returns:
    A dictionary containing the cast information for the movie.
  """

  # Make the API request.
  response = requests.get(
    'https://api.themoviedb.org/3/movie/' + movie_id + '/credits?api_key=' + my_api_key,
    headers={'Accept': 'application/json'}
  )

  # Check the response status code.
  if response.status_code != 200:
    raise Exception('Error getting movie cast: ' + response.status_code)

  # Parse the JSON response.
  data = response.json()

  # Return the cast information for the movie.
  return {
    'cast': data['cast'],
    'crew': data['crew']
  }

def get_movie_posters(arr, my_api_key):
  """
  This function gets the posters for the specified movies.

  Args:
    arr: A list of movie IDs.
    my_api_key: The API key for themoviedb.org.

  Returns:
    A list of URLs for the posters of the specified movies.
  """

  # Make the API requests.
  responses = []
  for movie_id in arr:
    responses.append(requests.get(
      'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + movie_id,
      headers={'Accept': 'application/json'}
    ))

  # Check the response status codes.
  for response in responses:
    if response.status_code != 200:
      raise Exception('Error getting movie posters: ' + response.status_code)

  # Parse the JSON responses.
  data = []
  for response in responses:
    data.append(response.json())

  # Return the URLs for the posters of the specified movies.
  return [data[i]['results'][0]['poster_path'] for i in range(len(arr))]
