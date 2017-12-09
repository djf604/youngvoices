def quiz():
    # Collect answers from the quiz page
    example = field("example")
    example2 = field("example2")

    # Check to see if answers are correct
    if example == "blue":
        add_score(15)


# Ignore the stuff below here

_post = None
_user = None
def init(request):
    global _post
    global _user
    _post = request.POST
    _user = request.user
    _user.profile.num_quizes_taken += 1
    _user.profile.save()
def field(field_name):
    return _post.get(field_name, '')
def add_score(score):
    _user.profile.total_score += score
    _user.profile.save()

