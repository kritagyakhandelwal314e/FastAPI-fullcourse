from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  return {
    'data': {
      'name': 'Kritagya'
    }
  }

@app.get('/about')
def about():
  return {
    'data': 'about page'
  }

@app.get('/blog')
def blogs(limit: int=10, skip: int=0):
  return {
    'data': {
      'blogs': [{
        'id': id,
        'text': f'blog number {id}'
      } for id in range(skip, skip + limit)]
    }
  }

@app.get('/blog/{id}')
def show(id: int):
  # fetch blog with id = id
  return {
    'data': {
      'blog': {
        'id': id
      }
    }
  }

@app.get('/blog/{id}/comments')
def comments(id: int):
  # fetch blog with id = id
  return {
    'data': {
      'blog': {
        'id': id,
        'comments': [{
          'from': 'yash',
          'text': 'Nice blog'
        },{
          'from': 'kritagya',
          'text': 'Great Efforts'
        }]
      }
    }
  }