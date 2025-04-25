from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine 
from models import URL, Base
from utils import generate_short_code

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten")
def make_url_short(long_url: str, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    ## now we should check if the url is unique or not 
    ## as two differnt long url may have the same short url 
    ## and sometimes it could also be happens that the re-shorten url can match with another shorten url 
    while db.query(URL).filter(URL.short_url == short_code).first():
        # then make it new
        short_code = generate_short_code()

    new_url = URL(original_url=long_url, short_url=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
def getting_original(short_code: str, db: Session = Depends(get_db)):
    value = db.query(URL).filter(URL.short_url == short_code).first()

    if value:
        return RedirectResponse(url = value.original_url)
    
    # if not found 
    raise HTTPException(status_code=404, detail="URL not found")