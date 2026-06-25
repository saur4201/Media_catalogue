class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'


class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def get_movies(self):
        """Returns only strict instances of the Movie parent class."""
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        """Returns only instances of the TVSeries child class."""
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
                
        if series:
            result += '=== TV SERIES ===\n'
            for i, tv_item in enumerate(series, 1):
                result += f'{i}. {tv_item}\n'    
                
        return result


# ==========================================
# EXECUTION & DEMONSTRATION EXAMPLES
# ==========================================

if __name__ == '__main__':
    catalogue = MediaCatalogue()

    print("--- 1. Testing Valid Entries ---")
    try:
        # Base entries
        movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
        catalogue.add(movie1)
        movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
        catalogue.add(movie2)

        series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
        catalogue.add(series1)
        series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
        catalogue.add(series2)
        
        # New diverse entries
        movie3 = Movie('Arrival of a Train', 1896, 'Louis Lumière', 1)
        catalogue.add(movie3)
        series3 = TVSeries('Chernobyl', 2019, 'Craig Mazin', 60, 1, 5)
        catalogue.add(series3)

        # Print beautifully formatted catalogue
        print(catalogue)
        
    except (ValueError, MediaError) as e:
        print(f'Unexpected error during valid initialization: {e}')


    print("\n--- 2. Testing Data Validation Boundaries (ValueError) ---")
    try:
        # Trigger: Historical cinema era constraint exception
        invalid_history = Movie('Ancient Play', 1800, 'Unknown', 90)
        catalogue.add(invalid_history)
    except ValueError as e:
        print(f'Validation Error caught successfully: {e}')

    try:
        # Trigger: Empty string title validation check
        invalid_title = Movie('   ', 2023, 'Director Name', 120)
        catalogue.add(invalid_title)
    except ValueError as e:
        print(f'Validation Error caught successfully: {e}')


    print("\n--- 3. Testing Type Protection & Exception Inspection (MediaError) ---")
    # Define an external, unsupported data structure type
    class Audiobook:
        def __init__(self, title, author):
            self.title = title
            self.author = author
        def __str__(self):
            return f'{self.title} by {self.author}'

    try:
        # Trigger: Attempting to add an unsupported class instance
        unsupported_item = Audiobook('Project Hail Mary', 'Andy Weir')
        catalogue.add(unsupported_item)
    except MediaError as e:
        print(f'Media Error caught successfully: {e}')
        print(f'Unable to add {e.obj}: {type(e.obj)}')

    try:
        # Trigger: Attempting to pass a raw primitive string structure
        catalogue.add("The Dark Knight (String)")
    except MediaError as e:
        print(f'Media Error caught successfully: {e}')
        print(f'Unable to add {e.obj}: {type(e.obj)}')
