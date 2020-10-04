# Simple test script, unittest will be added following chapter(8).
trap "kill 0" EXIT

# Run flask background
FLASK_ENV=development FKAS_APP=app.py flask run &

# Add users
http -v POST localhost:5000/sign-up name=a email=a@a.com password=a
http -v POST localhost:5000/sign-up name=b email=b@b.com password=b
http -v POST localhost:5000/sign-up name=c email=c@c.com password=c
http -v POST localhost:5000/sign-up name=d email=d@d.com password=d

# Tweets
http -v POST localhost:5000/tweet id:=1 tweet="A!"
http -v POST localhost:5000/tweet id:=1 tweet="AA!"
http -v POST localhost:5000/tweet id:=2 tweet="B!"
http -v POST localhost:5000/tweet id:=2 tweet="BB!"
http -v POST localhost:5000/tweet id:=3 tweet="C!"
http -v POST localhost:5000/tweet id:=3 tweet="CC!"
http -v POST localhost:5000/tweet id:=4 tweet="D!"
http -v POST localhost:5000/tweet id:=4 tweet="DD!"

# Follows
http -v POST localhost:5000/follow id:=1 follow:=2
http -v POST localhost:5000/follow id:=2 follow:=3
http -v POST localhost:5000/follow id:=2 follow:=4
http -v POST localhost:5000/follow id:=4 follow:=1

# Timeline
http -v GET localhost:5000/timeline/1
http -v GET localhost:5000/timeline/4
