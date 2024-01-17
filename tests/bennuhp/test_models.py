from datetime import date, time

from django.test import TestCase

from bennuhp.models.music import Music
from bennuhp.models.movie import Movie
from bennuhp.models.liveschedule import LiveSchedule


class TestBlankRecord(TestCase):
    def test_no_music_record(self):
        musics = Music.objects.all()
        self.assertEqual(musics.count(), 0)

    def test_no_movie_record(self):
        movies = Movie.objects.all()
        self.assertEqual(movies.count(), 0)

    def test_no_live_record(self):
        lives = LiveSchedule.objects.all()
        self.assertEqual(lives.count(), 0)


class TestMusicModel(TestCase):
    fixtures = ['initial_data.json']

    def test_count_musics(self):
        musics = Music.objects.all()
        self.assertEqual(musics.count(), 3)

    def test_get_music_object(self):
        music = Music.objects.get(pk='a5cf0e7beaa544dca706266b201382b3')
        self.assertEqual(music.title, "What's my love?")
        self.assertEqual(music.publish_date, date(2015, 7, 1))
        self.assertEqual(music.descriptions, "First original single, Waltz with playing the piano")
        self.assertEqual(music.url, "https://soundcloud.com/bennu1011/whats-my-love-original")
        self.assertEqual(music.image_path, "bennuhp/img/whats-my-love.png")


class TestMoviesModel(TestCase):
    fixtures = ['initial_data.json']

    def test_count_movies(self):
        movies = Movie.objects.all()
        self.assertEqual(movies.count(), 2)

    def test_get_movie_object(self):
        movie = Movie.objects.get(pk='f7dfa97e04cb4727b6576154686fc161')
        self.assertEqual(movie.title, "live@YotsuyaTenmado")
        self.assertEqual(movie.date, date(2015, 7, 8))
        self.assertEqual(movie.venue, "Yotsuya Tenmado")
        self.assertEqual(movie.descriptions, "First live movies at Yotsuya Tenmado.")
        self.assertEqual(movie.url, "https://www.youtube.com/watch?v=D2rjg39aeps")
        self.assertEqual(movie.image_path, "bennuhp/img/20150708-live.png")


class TestLivesModel(TestCase):
    fixtures = ['initial_data.json']

    def test_count_lives(self):
        lives = LiveSchedule.objects.all()
        self.assertEqual(lives.count(), 6)

    def test_get_live_object(self):
        live = LiveSchedule.objects.get(pk='36ebc8af4223414a80078cb43a0d6c60')
        self.assertEqual(live.title, "2015-07-08@Takadanobaba")
        self.assertEqual(live.descriptions, "Bennu first live")
        self.assertEqual(live.date, date(2015, 7, 8))
        self.assertEqual(live.venue, "Yotsuya Tenmado comfort")
        self.assertEqual(live.url, "http://otonami.com/comfort/map/")
        self.assertEqual(live.open_time, time(19, 0))
        self.assertEqual(live.start_time, None)
        self.assertEqual(live.price, None)
        self.assertEqual(live.with_actors, [])
        self.assertEqual(live.image_path, "bennuhp/img/20150708-live.png")
