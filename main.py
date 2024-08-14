from fastapi import FastAPI, HTTPException
from db import Post, User, Session
from models_pyd import PostCreate, PostUpdate, UserCreate, UserUpdate

app = FastAPI()


@app.get('/')
def func():
    return 'hi'


@app.get('/posts')
def get_all_posts():
    session = Session()
    return session.query(Post).all()


@app.get('/posts/{post_id}')
def get_post(post_id: int):
    session = Session()
    try:
        post = session.query(Post).filter(Post.id == post_id).first()
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    finally:
        session.close()

@app.post('/posts')
def create_post(post: PostCreate):
    session = Session()
    title = post.title
    description = post.description
    new_post = Post(
        title=title,
        description=description
    )
    try:
        session.add(new_post)
        session.commit()

    except Exception as exp:
        raise exp

    finally:
        session.close()

    return {'created': 'success'}


@app.patch('/posts/{post_id}')
def post_update(post_id: int, post: PostUpdate):
    session = Session()
    post_obj = session.query(Post).filter(Post.id == post_id).first()
    title = post.title
    description = post.description
    post_obj.title = title
    post_obj.description = description

    try:
        session.commit()
    except Exception as exp:
        raise exp
    finally:
        session.close()

    return {'updated': 'success'}


@app.delete('/posts/{post_id}')
def delete_post(post_id: int):
    session = Session()
    post = session.query(Post).filter(Post.id == post_id).first()

    try:
        session.delete(post)
        session.commit()

    except Exception as exp:
        raise exp

    finally:
        session.close()








@app.get('/users')
def get_all_users():
    session = Session()
    return session.query(User).all()


@app.get('/users/{user_id}')
def get_user(user_id: int):
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return user

    finally:
        session.close()

@app.post('/users')
def create_user(user: UserCreate):
    session = Session()
    name = user.name
    surname = user.surname
    new_user = User(
        name=name,
        surname=surname
    )
    try:
        session.add(new_user)
        session.commit()

    except Exception as exp:
        raise exp

    finally:
        session.close()

    return {'created': 'success'}


@app.patch('/users/{user_id}')
def user_update(user_id: int, user: UserUpdate):
    session = Session()
    user_obj = session.query(User).filter(User.id == user_id).first()
    name = user.name
    surname = user.surname
    user_obj.name = name
    user_obj.surname = surname

    try:
        session.commit()
    except Exception as exp:
        raise exp
    finally:
        session.close()

    return {'updated': 'success'}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()

    try:
        session.delete(user)
        session.commit()

    except Exception as exp:
        raise exp

    finally:
        session.close()




