from sqlalchemy import select
from fast_zero.models import User

def test_user_db(session):
    user = User(
        username='testusername',
        email='test@test.com',
        password='testpassword',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'test@test.com')
    )

    assert result.id == 1