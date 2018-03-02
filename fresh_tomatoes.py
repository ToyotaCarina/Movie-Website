# -*- coding: cp1251 -*-
import webbrowser
import os
import re
import json

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script defer src="https://use.fontawesome.com/releases/v5.0.6/js/all.js"></script>
    <style media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-info_short {
             margin-bottom: 10px;    
        }
    </style>
    <script>
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        // Fills modal window with data from html attribute
        $(document).on('click', '.movie-tile', function (event) {
            var movieInfo = $(this).data('movie-info');
            var movieTitle = movieInfo.title;
            var movieStoryline = movieInfo.storyline;
            var movieDuration = movieInfo.duration + ' min';
            var trailerYouTubeId = movieInfo.trailer_youtube_url;
            var movieYear = movieInfo.year;
            var movieGenre = movieInfo.genre;
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#movie-title").text(movieTitle);
            $("#movie-storyline").text(movieStoryline);
            $("#movie-duration").text(movieDuration);
            $("#movie-year").text(movieYear);
            $("#movie-genre").text(movieGenre.join(", "));
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0,
              'allowfullscreen': 1
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-body">
              <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                  <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="Close"/>
              </a>
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title" id="movie-title">Movie name</h5>
                        <div class="row movie-info_short">
                          <div class="col-md-auto">
                              <small class="text-muted" id="movie-genre"></small>
                          </div>
                          <div class="col-md-auto">
                              <small class="text-muted">
                                  <i class="far fa-calendar-alt"></i>
                                  <span id="movie-year"></span>
                              </small> 
                          </div>
                          <div class="col-md-auto">
                              <small class="text-muted">
                                  <i class="far fa-clock"></i>
                                  <span id="movie-duration"></span>
                              </small>        
                          </div>
                        </div>
                    <p class="card-text" id="movie-storyline"></p>                    
                  </div>
                 <div class="card-image">
                     <div class="embed-responsive embed-responsive-16by9" id="trailer-video-container">
                 </div>
                    
                </div><!-- card image -->                 
                </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
        <div class="navbar navbar-dark bg-dark fixed-top navbar-expand-md" role="navigation">
            <div class="container"> <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
            </div>
        </div>
    </div>
    <div class="container">
      <div class="row">
          {movie_tiles}
      </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-movie-info='{movie_info}' data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" alt="" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

# Converts all attributes of the instance of the movie class
# to a json string. Replaces quotes with &apos; to avoid
# closing quotes situation
def attributes_to_string(movie):  
    js = json.dumps(movie.__dict__)
    js = js.replace("'", "&apos;")
    return js

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None     

        # Before put all object arguments to json string
        # trailer url temporary changes to youtube ID
        saved_trailer_url = movie.trailer_youtube_url 
        movie.trailer_youtube_url = trailer_youtube_id
        movie_attr = attributes_to_string(movie)
        movie.trailer_youtube_url = saved_trailer_url
        
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_info=movie_attr 
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible   
