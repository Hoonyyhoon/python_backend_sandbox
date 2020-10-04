# Implementing Miniter API
Reference: 
1. 깔끔한 파이썬 탄탄한 백엔드 5장, 본격적으로 API 개발하기
2. https://github.com/rampart81/python-backend-book/tree/master/chapter5

## Key features of Miniter
1. Sign up
2. Sign in
3. Tweet(less than 300 characters)
4. Follow(Other user)
5. Unfollow(Other user)
6. Timeline(Tweets of user and following users)

## Run
Since unittest will be implemented in further chapter(8), this chapter verify functionality with scripts(doesn't do any failure cases)
```terminal
# give permission to script
chmod +x ./test.sh
./test.sh
```

## Implementation
### 1) Sign up
Information for sign up
1. id
2. name
3. email
4. pwd
5. profile

### 2) Tweet 
Requirements, elements for tweet
- User can post tweet less than 300 characters.
- If tweet has more than 300 characters, endpoint answers 400 Bad Request.
- If user send tweet less than 300 chs, endpoint should save tweet so that it can read from timeline endpoint.
- Tweet endpoint receives JSON structure as follows.
```json
{
    "id" : 1,
    "tweet" : "My First Tweet"
}
```

### 3) Follow, Unfollow
- Follow/Unfollow endpoint receives JSON structure as follows.
```json
{
    "id": ${userid},
    "follow": ${target_userid}
}
```
```json
{
    "id": ${userid},
    "unfollow": ${target_userid}
}
```

### 4) Timeline
Timeline posts tweets of user, and users' tweets followed by user.
- Timeline endpoint should return JSON structure as follows.
```json
{
    "user_id": 1,
    "timeline": [
        {
            "user_id": 2,
            "tweet": "Hello, World!"
        },
        {
            "user_id": 1,
            "tweet": "My first tweet!!"
        }
    ]
}
```
