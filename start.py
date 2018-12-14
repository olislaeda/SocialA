from sources import sa, db
from sources.dbstruct.users import User
from sources.dbstruct.posts import Post
sa.run(debug=False)


@sa.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
