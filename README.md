# Music Party

App that lets a group of users control music being played from Spotify with a voting system to skip the current song being played.

## Description

This app will let a host create a room where other guest can join. In the room is a controller system that will let a user vote to skip a song if enough votes have been counted to skip determined by the host of the room the app will skip to the next song.

## Getting Started

### Dependencies

- Python
- Node

### Installing

- Clone this Repository to your desktop
- CD into the repository and make migrations for the backend

```
cd music_controller
python manage.py migrate
```

- CD into the client folder and install all the needed dependencies

```
cd client
npm install
```

### Executing program

- from the root folder start the backend server

```
python manage.py runserver
```

- In a new terminal from the root folder move into the client folder of the project and start the webpack development server

```
cd client
npm run dev
```

-Once both servers are running you can visit localhost:8000 in your browser to view the application

## Authors

Contributors names and contact info

Joshua Hellman
[@JH3LL](https://twitter.com/JH3LL)

## License

This project is licensed under the MIT License

## Acknowledgments

some of this app was built using a tutorial by
[Tim Ruscica ](https://github.com/techwithtim)
