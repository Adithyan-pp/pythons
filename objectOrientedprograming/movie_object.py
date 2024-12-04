class Movie:

    title:str

    rating:int

    director:str

    run_time:int

    genre:str


    def set_movie(self,title,rating,director,run_time,genre):

        self.title=title

        self.rating=rating

        self.director=director

        self.run_time=run_time

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.director,self.run_time,self.genre)

set_movie1=Movie()

set_movie2=Movie()


set_movie1.set_movie("vikarm",9.7,"lokesh","3hr","action triller")
set_movie2.set_movie("anniyan",9.4,"shankar","3hr","action,drama")

set_movie1.display()

set_movie2.display()
